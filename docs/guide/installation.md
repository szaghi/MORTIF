---
title: Installation
---

# Installation

## Prerequisites

A Fortran 2003+ compliant compiler is required. The following compilers are known to work:

| Compiler | Minimum version |
|----------|----------------|
| GNU gfortran | ≥ 6.1 |
| Intel Fortran (ifort / ifx) | ≥ 16.x |

MORTIF is developed on GNU/Linux. Windows should work out of the box but is not officially tested.

## Download

MORTIF uses **git submodules** for its third-party dependencies. Clone recursively:

```bash
git clone https://github.com/szaghi/MORTIF --recursive
cd MORTIF
```

If you already have a non-recursive clone:

```bash
git submodule update --init --recursive
```

### Third-Party Dependencies

The submodules live under `src/third_party/`:

| Library | Purpose |
|---------|---------|
| [PENF](https://github.com/szaghi/PENF) | Portable numeric kind parameters (`I4P`, `I8P`, `R4P`, etc.) |
| [fortran_tester](https://github.com/pdebuyl/fortran_tester) | Lightweight assertion framework used in tests |

## Build with FoBiS.py (recommended)

[FoBiS.py](https://github.com/szaghi/FoBiS) is the primary build system and is used by the CI pipeline.

```bash
pip install FoBiS.py
```

### List all build modes

```bash
FoBiS.py build -lmodes
```

Available modes:

| Mode | Description |
|------|-------------|
| `tests-gnu` | Build all tests with gfortran (release) |
| `tests-gnu-debug` | Build all tests with gfortran (debug) |
| `tests-intel` | Build all tests with ifort (release) |
| `tests-intel-debug` | Build all tests with ifort (debug) |
| `static-gnu` | Static library with gfortran → `./static/libmortif.a` |
| `shared-gnu` | Shared library with gfortran → `./shared/libmortif.so` |
| `static-intel` | Static library with ifort |
| `shared-intel` | Shared library with ifort |

### Build and run tests

```bash
FoBiS.py build -mode tests-gnu
./scripts/run_tests.sh
```

Compiled test executables are placed in `./exe/`.

### Build the library

```bash
# Static library (GNU gfortran)
FoBiS.py build -mode static-gnu

# Shared library (GNU gfortran)
FoBiS.py build -mode shared-gnu

# Static library (Intel Fortran)
FoBiS.py build -mode static-intel
```

### Coverage and documentation

```bash
FoBiS.py rule -ex makecoverage   # build + run tests + gcov report
FoBiS.py rule -ex makedoc        # build ford API documentation
```

Documentation generation requires `ford` (`pip install ford`) and `graphviz`.

## Build with GNU Make

A makefile is provided for compatibility. It builds all tests with executables in `./exe/`:

```bash
make -j 1
```

To build only the static library:

```bash
make -j 1 STATIC=yes
```

## Build with CMake

```bash
git clone --recursive https://github.com/szaghi/MORTIF $YOUR_MORTIF_PATH
mkdir build && cd build
cmake $YOUR_MORTIF_PATH
cmake --build .
```

To run the test suite with CMake:

```bash
cmake -DMORTIF_ENABLE_TESTS=ON $YOUR_MORTIF_PATH
cmake --build .
ctest
```
