"""Basic smoke tests for NumPy compatibility.

These tests are intentionally lightweight and focus on catching
import-time or very early runtime issues when using modern NumPy.
"""

import unittest

import numpy as np

# Import a few core pypet modules to ensure they load under NumPy 2
from pypet.parameter import Parameter, ArrayParameter  # noqa: F401
from pypet.storageservice import HDF5StorageService  # noqa: F401


class TestNumpyImports(unittest.TestCase):
    def test_basic_numpy_array_handling(self):
        """Ensure that ArrayParameter still supports simple NumPy arrays."""

        arr = np.array([1.0, 2.0, 3.0], dtype=float)
        param = ArrayParameter("test.array_param", arr)

        # The parameter should store the array unchanged
        self.assertTrue(np.all(param.f_get() == arr))


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
