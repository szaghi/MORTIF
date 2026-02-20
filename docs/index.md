---
layout: home

hero:
  name: MORTIF
  text: Morton Indexer (Z-order)
  tagline: A pure Fortran 2003+ library to encode and decode multidimensional integer indexes into Morton's Z-order.
  actions:
    - theme: brand
      text: Guide
      link: /guide/
    - theme: alt
      text: API Reference
      link: /api/
    - theme: alt
      text: View on GitHub
      link: https://github.com/szaghi/MORTIF

features:
  - icon: 📐
    title: 2D Encoding & Decoding
    details: Map a pair of 32-bit integer indexes to a single 64-bit Morton code and back with morton2D / demorton2D.
  - icon: 📦
    title: 3D Encoding & Decoding
    details: Map three integer indexes to a 64-bit Morton code with morton3D / demorton3D. Supports up to 21 significant bits per axis.
  - icon: ⚡
    title: Elemental Procedures
    details: All four public procedures are elemental — apply them to scalars or entire arrays with no extra code.
  - icon: 🔧
    title: Multi Build System
    details: Build with FoBiS.py, GNU Make, or CMake. A fobos file covers all modes for GNU gfortran and Intel Fortran.
  - icon: 🧪
    title: Pure Fortran / TDD
    details: No C extensions, no external dependencies beyond PENF. Developed test-first with a correctness test suite.
  - icon: 🆓
    title: Free & Open Source
    details: Multi-licensed — GPLv3 for FOSS projects, BSD 2/3-Clause or MIT for commercial use. Fortran 2003+ standard compliant.
---

## Quick start

Encode a 3D index tuple and decode it back:

```fortran
use, intrinsic :: iso_fortran_env, only : int32, int64
use mortif

integer(int32) :: i, j, k
integer(int64) :: code

! Encode
code = morton3D(i=1_int32, j=2_int32, k=3_int32)
print '(A,I20)', "Morton code of {1,2,3}: ", code

! Decode
call demorton3D(code=code, i=i, j=j, k=k)
print '(A,3(I0,1X))', "Decoded indexes: ", i, j, k
```

```fortran
use, intrinsic :: iso_fortran_env, only : int32, int64
use mortif

integer(int64) :: code

! 2D example
code = morton2D(i=0_int32, j=1_int32)
print '(A,I20)', "Morton code of {0,1}: ", code   ! 2
```

## Authors

- Stefano Zaghi — [@szaghi](https://github.com/szaghi)

Contributions are welcome — see the [Contributing](/guide/contributing) page.

## Copyrights

MORTIF is distributed under a multi-licensing system:

| Use case | License |
|----------|---------|
| FOSS projects | [GPL v3](http://www.gnu.org/licenses/gpl-3.0.html) |
| Closed source / commercial | [BSD 2-Clause](http://opensource.org/licenses/BSD-2-Clause) |
| Closed source / commercial | [BSD 3-Clause](http://opensource.org/licenses/BSD-3-Clause) |
| Closed source / commercial | [MIT](http://opensource.org/licenses/MIT) |

> Anyone interested in using, developing, or contributing to MORTIF is welcome — pick the license that best fits your needs.
