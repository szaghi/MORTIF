# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What is MORTIF?

MORTIF (MORTon Indexer Fortran) is a pure Fortran 2003+ library that encodes/decodes multidimensional integer indexes to/from Morton's Z-order. It exposes four elemental procedures:

- `morton2D` / `demorton2D` — encode/decode 2D indexes (up to 32 significant bits each)
- `morton3D` / `demorton3D` — encode/decode 3D indexes (up to 21 significant bits each, due to 64-bit code limit)

## VitePress Documentation

The `docs/` directory is a VitePress site. Build commands (run from `docs/`):

```bash
npm run docs:dev      # local dev server
npm run docs:build    # production build → docs/.vitepress/dist/
npm run docs:preview  # preview the built site
npm run docs:api      # regenerate API docs from Fortran sources (requires FORMAL)
```

Guide pages live in `docs/guide/`: `index.md` (About), `features.md`, `installation.md`, `usage.md`, `api-reference.md`, `contributing.md`, `coverage-analysis.md`, `changelog.md`. Auto-generated API docs are in `docs/api/`.

## Build System

The project uses [FoBiS.py](https://github.com/szaghi/FoBiS) with a `fobos` configuration file. FoBiS.py must be installed (`pip install FoBiS.py`).

### Build commands

```bash
# List available build modes
FoBiS.py build -lmodes

# Build tests (executables land in ./exe/)
FoBiS.py build -mode tests-gnu            # release, GNU gfortran
FoBiS.py build -mode tests-gnu-debug      # debug, GNU gfortran
FoBiS.py build -mode tests-intel          # release, Intel ifort
FoBiS.py build -mode tests-intel-debug    # debug, Intel ifort

# Build library only
FoBiS.py build -mode static-gnu           # static lib → ./static/libmortif.a
FoBiS.py build -mode shared-gnu           # shared lib → ./shared/libmortif.so
```

Alternative build systems (GNU Make and CMake) are supported but discouraged; see README.md for details.

### Submodules

Third-party dependencies are git submodules; initialise them after cloning:

```bash
git submodule update --init --recursive
```

Dependencies:
- `src/third_party/PENF` — Precision ENvironment for Fortran (provides `I1P`, `I2P`, `I4P`, `I8P`, `R4P`, etc.)
- `src/third_party/fortran_tester` — lightweight Fortran unit-test framework (`tester_t`)

## Running Tests

```bash
# Build then run all tests
FoBiS.py build -mode tests-gnu
./scripts/run_tests.sh

# Or run a single test executable directly
./exe/mortif_test_correctness
```

`run_tests.sh` discovers all executables in `./exe/`, runs them, and checks for `"Are all tests passed? T"` in their output. Files with `failure` in their name are expected to fail (the script inverts the pass/fail logic for those).

### Coverage analysis

```bash
FoBiS.py rule -ex makecoverage
```

This cleans, rebuilds with `-coverage`, runs tests, and runs `gcov`.

## Code Architecture

```
src/
  lib/mortif.f90          ← entire library (single module: mortif)
  tests/
    mortif_test_correctness.f90
  third_party/
    PENF/                 ← precision kinds submodule
    fortran_tester/       ← tester_t submodule
exe/                      ← compiled test executables + obj/ + mod/
```

All library logic lives in the single file `src/lib/mortif.f90`. The module has two private core routines:

- `dilatate(i, b, z)` — spreads the `b` significant bits of a 32-bit integer across a 64-bit integer by inserting `z` zeros between each bit (bit dilation).
- `contract(i, b, z, c)` — reverse of `dilatate` (bit contraction).

The public `morton2D`/`morton3D` functions call `dilatate` per axis, then combine with bit-shifts. The decode subroutines call `contract` per axis after shifting the code.

All four public procedures are `elemental`, so they work on scalars and arrays without extra code.

## Documentation

```bash
FoBiS.py rule -ex makedoc   # builds HTML docs into doc/html/ using ford
FoBiS.py rule -ex deldoc    # removes doc/html/
```

Requires `ford` (`pip install ford`) and `graphviz`.
