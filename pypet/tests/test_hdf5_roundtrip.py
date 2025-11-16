"""HDF5 round-trip smoke test for the updated pypet fork.

This test ensures that a simple trajectory with a NumPy array parameter can
be stored to and reloaded from an HDF5 file using the Environment API.
"""

import os
import tempfile

import numpy as np

from pypet.environment import Environment


def _multiply_job(traj):
    """Tiny example job that uses a NumPy array parameter and stores a result."""

    x = traj.x
    traj.f_add_result("y", x * 2.0, comment="Doubled array")


def test_hdf5_roundtrip(tmp_path):
    """Store and reload a small trajectory containing a NumPy array parameter."""

    # Use a temporary HDF5 file under pytest's tmp_path
    hdf5_path = tmp_path / "roundtrip.hdf5"

    env = Environment(
        trajectory="roundtrip_test",
        filename=str(hdf5_path),
        file_title="roundtrip_test",
        comment="HDF5 round-trip smoke test",
        multiproc=False,
        log_stdout=False,
    )

    traj = env.trajectory

    # Add a simple NumPy array parameter
    arr = np.array([1.0, 2.0, 3.0], dtype=float)
    traj.f_add_parameter("x", arr, comment="Test NumPy array parameter")

    # Run the simulation
    env.run(_multiply_job)

    # Close environment to flush to disk
    env.disable_logging()
    env.f_finalize()

    # Reload the trajectory from disk and check content
    env_reload = Environment(
        trajectory="roundtrip_test_reload",
        filename=str(hdf5_path),
        file_title="roundtrip_test_reload",
        comment="Reloaded trajectory",
        multiproc=False,
        log_stdout=False,
        add_time=False,
        load_trajectory="roundtrip_test",
    )

    traj_loaded = env_reload.trajectory

    # Ensure the parameter and result survived the round-trip
    np.testing.assert_allclose(traj_loaded.x, arr)
    np.testing.assert_allclose(traj_loaded.y, arr * 2.0)
