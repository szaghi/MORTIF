# MORTIF

>#### MORTon Indexer (Z-order) Fortran environment
>a pure Fortran 2003+ library to encode and decode multidimensional integer indexes into [Morton's Z-order](https://en.wikipedia.org/wiki/Z-order_curve).

[![GitHub tag](https://img.shields.io/github/v/tag/szaghi/MORTIF)](https://github.com/szaghi/MORTIF/tags)
[![GitHub issues](https://img.shields.io/github/issues/szaghi/MORTIF)](https://github.com/szaghi/MORTIF/issues)
[![CI](https://github.com/szaghi/MORTIF/actions/workflows/ci.yml/badge.svg)](https://github.com/szaghi/MORTIF/actions/workflows/ci.yml)
[![Coverage](https://img.shields.io/codecov/c/github/szaghi/MORTIF.svg)](https://app.codecov.io/gh/szaghi/MORTIF)
[![License](https://img.shields.io/badge/license-GPLv3%20%7C%20BSD%20%7C%20MIT-blue.svg)](#copyrights)

| 🔢 **2D encoding**<br>`morton2D` maps two 32-bit indexes → one 64-bit Morton code | 📐 **3D encoding**<br>`morton3D` maps three 32-bit indexes → one 64-bit code (up to 21 bits/axis) | 🔄 **Lossless decoding**<br>`demorton2D`/`demorton3D` are the exact inverse — bit-perfect round-trip | ⚡ **Elemental interface**<br>All four procedures work on scalars and conformable arrays in one call |
|:---:|:---:|:---:|:---:|
| 🧩 **Single module**<br>Entire library is a single `mortif.f90` — easy to vendor | 📏 **Configurable precision**<br>Optional `b` parameter restricts to 2/4/8/16/32 significant bits per axis | 🏎️ **Zero overhead**<br>No range checks, no allocations, no system calls | 📦 **Multiple build systems**<br>FoBiS, CMake, GNU Make |

>#### [Documentation](https://szaghi.github.io/MORTIF/)
> For full documentation (guide, API reference, examples, etc...) see the [MORTIF website](https://szaghi.github.io/MORTIF/).

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

```fortran
use, intrinsic :: iso_fortran_env, only : int32, int64
use mortif
implicit none
integer(int32) :: i, j, k
integer(int64) :: code

code = morton3D(i=0_int32, j=1_int32, k=0_int32)
print '(A,I0)', "Morton code of {0,1,0}: ", code   ! 2

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

See [`src/tests/`](src/tests/) for correctness tests including extrema and 4096-point 16×16×16 grid validation.

---

## Install

### FoBiS

**Standalone** — clone, fetch the dependency, and build:

```bash
git clone https://github.com/szaghi/MORTIF && cd MORTIF
FoBiS.py fetch                    # fetch PENF
FoBiS.py build -mode static-gnu   # build static library
```

**As a project dependency** — declare MORTIF in your `fobos` and run `fetch`:

```ini
[dependencies]
deps_dir = src/third_party
MORTIF = https://github.com/szaghi/MORTIF
```

```bash
FoBiS.py fetch           # fetch and build
FoBiS.py fetch --update  # re-fetch and rebuild
```

### CMake

```bash
git clone https://github.com/szaghi/MORTIF --recursive && cd MORTIF
cmake -B build -DMORTIF_ENABLE_TESTS=ON && cmake --build build && ctest --test-dir build
```

**As a CMake subdirectory:**

```cmake
add_subdirectory(MORTIF)
target_link_libraries(your_target MORTIF::MORTIF)
```
