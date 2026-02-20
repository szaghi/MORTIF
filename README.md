# MORTIF

**MORTon Indexer (Z-order) Fortran environment** — a pure Fortran 2003+ library to encode and decode multidimensional integer indexes into [Morton's Z-order](https://en.wikipedia.org/wiki/Z-order_curve).

[![CI](https://github.com/szaghi/MORTIF/actions/workflows/ci.yml/badge.svg)](https://github.com/szaghi/MORTIF/actions)
[![Coverage](https://img.shields.io/codecov/c/github/szaghi/MORTIF.svg)](https://app.codecov.io/gh/szaghi/MORTIF)
[![GitHub tag](https://img.shields.io/github/tag/szaghi/MORTIF.svg)](https://github.com/szaghi/MORTIF/releases)
[![License](https://img.shields.io/badge/license-GPLv3%20%7C%20BSD%20%7C%20MIT-blue.svg)](#copyrights)

---

## Features

- Encode two 32-bit indexes into a 64-bit Morton code with `morton2D`
- Encode three 32-bit indexes into a 64-bit Morton code with `morton3D` (up to 21 significant bits per axis)
- Decode Morton codes back to indexes with `demorton2D` / `demorton3D`
- All four procedures are `elemental` — apply directly to scalars or arrays
- Pure Fortran, no C extensions, single 194-line module

**[Documentation](https://szaghi.github.io/MORTIF/)** | **[API Reference](https://szaghi.github.io/MORTIF/api/)**

---

## Authors

- Stefano Zaghi — [@szaghi](https://github.com/szaghi)

Contributions are welcome — see the [Contributing](https://szaghi.github.io/MORTIF/guide/contributing) page.

## Copyrights

This project is distributed under a multi-licensing system:

- **FOSS projects**: [GPL v3](http://www.gnu.org/licenses/gpl-3.0.html)
- **Closed source / commercial**: [BSD 2-Clause](http://opensource.org/licenses/BSD-2-Clause), [BSD 3-Clause](http://opensource.org/licenses/BSD-3-Clause), or [MIT](http://opensource.org/licenses/MIT)

> Anyone interested in using, developing, or contributing to this project is welcome — pick the license that best fits your needs.

---

## Quick start

Encode a 3D index tuple and decode it back:

```fortran
use, intrinsic :: iso_fortran_env, only : int32, int64
use mortif
implicit none
integer(int32) :: i, j, k
integer(int64) :: code

code = morton3D(i=0_int32, j=1_int32, k=0_int32)
print '(A,I20)', "Morton code of {0,1,0}: ", code   ! 2

call demorton3D(code=code, i=i, j=j, k=k)
print '(A,3(I0,1X))', "Decoded: ", i, j, k          ! 0 1 0
```

Elemental use on arrays:

```fortran
use, intrinsic :: iso_fortran_env, only : int32, int64
use mortif
implicit none
integer(int32) :: ix(4) = [0, 1, 2, 3]
integer(int32) :: iy(4) = [0, 0, 1, 1]
integer(int64) :: codes(4)

codes = morton2D(i=ix, j=iy)   ! [0, 1, 4, 5]
```

---

## Install

### Clone and build with FoBiS.py

```sh
git clone https://github.com/szaghi/MORTIF --recursive
cd MORTIF
FoBiS.py build -mode tests-gnu
./scripts/run_tests.sh
```

### Build with CMake

```sh
mkdir build && cd build
cmake -DMORTIF_ENABLE_TESTS=ON ..
cmake --build . && ctest
```

| Tool | Command |
|------|---------|
| FoBiS.py | `FoBiS.py build -mode static-gnu` |
| GNU Make | `make -j 1` |
| CMake | `cmake .. && cmake --build .` |
