# pypet modernization TODO

This document tracks the work for the updated fork of `SmokinCaterpillar/pypet`.

## High-level goals

- Bring `pypet` up to date with **modern Python** (currently targeting Python >= 3.12).
- Ensure compatibility with **NumPy >= 2.3** and recent versions of SciPy, pandas, and PyTables.
- Streamline and simplify internals where possible while keeping the core feature set.
- Rebuild a focused test suite tailored to this fork.

## Near-term tasks

- [x] Add `pyproject.toml` with modern dependency versions.
- [x] Create a fork-specific README that clearly attributes the original project.
- [x] Fix obvious incompatibilities with modern NumPy (e.g., `np.float`).
- [ ] Audit for any remaining usage of deprecated NumPy aliases (`np.int`, `np.bool`, `np.complex`, `np.str`, etc.) and remove or replace them where they affect runtime behavior.
- [ ] Decide on long-term handling of `numpy.matrix` (keep support vs. migrate to pure `ndarray` flows).
- [ ] Add a minimal smoke-test suite under `pypet/tests` that:
  - [x] imports the main modules under NumPy 2,
  - [x] exercises basic parameter/result creation with NumPy arrays,
  - [ ] stores and reloads a simple trajectory to HDF5.
- [ ] Reintroduce/port selected tests from `.original/tests` that are still relevant and keep behavior stable.

## Medium-term ideas

- [ ] Review data type handling in `pypet/pypetconstants.py` for unnecessary legacy compatibility layers.
- [ ] Look for opportunities to simplify storage code paths in `pypet/storageservice.py` (especially around type dispatching and attribute metadata).
- [ ] Consider switching some internal helper patterns to more idiomatic modern Python (type hints, f-strings, etc.) while keeping public APIs stable.

## Long-term

- [ ] Decide on a stable public API surface for this fork and document any intentional divergences from the original project.
- [ ] Set up CI for this fork (Python versions, NumPy/pandas/Scipy matrix).
