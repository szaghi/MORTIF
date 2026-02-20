---
title: About MORTIF
---

# About MORTIF

**MORTIF** (MORTon Indexer Fortran) is a pure Fortran 2003+ library to encode and decode multidimensional integer indexes into [Morton's Z-order](https://en.wikipedia.org/wiki/Z-order_curve) (also called Morton order or Morton code).

In mathematical analysis and computer science, the Z-order curve is a function that maps multidimensional data to one dimension while preserving locality of the data points. It was introduced in 1966 by G. M. Morton. The Z-value of a point in multiple dimensions is calculated by interleaving the binary representations of its coordinate values.

> Morton's code (Z-order) is a scheme to map multi-dimensional arrays onto a linear one with a great deal of spatial locality.

MORTIF exposes four elemental Fortran procedures:

| Procedure | Kind | Description |
|-----------|------|-------------|
| `morton2D` | function | Encode two 32-bit indexes → one 64-bit Morton code |
| `demorton2D` | subroutine | Decode a 64-bit Morton code → two 32-bit indexes |
| `morton3D` | function | Encode three 32-bit indexes → one 64-bit Morton code |
| `demorton3D` | subroutine | Decode a 64-bit Morton code → three 32-bit indexes |

Being `elemental`, all four procedures work transparently on scalars and conformable arrays.

## References

1. Morton, G. M. — *A Computer Oriented Geodetic Data Base and a New Technique in File Sequencing*, IBM technical report, 1966.
2. Stocco, L. J. and Schrack, G. — *On Spatial Orders and Location Codes*, IEEE Transactions on Computers, vol. 58, no. 3, March 2009.
3. Baert, J., Lagae, A. and Dutré, Ph. — *Out-of-Core Construction of Sparse Voxel Octrees*, SIGGRAPH/Eurographics High-Performance Graphics, 2013.

## Authors

- Stefano Zaghi — [@szaghi](https://github.com/szaghi)

Contributions are welcome — see the [Contributing](contributing) page.

## Copyrights

MORTIF is distributed under a multi-licensing system:

| Use case | License |
|----------|---------|
| FOSS projects | [GPL v3](http://www.gnu.org/licenses/gpl-3.0.html) |
| Closed source / commercial | [BSD 2-Clause](http://opensource.org/licenses/BSD-2-Clause) |
| Closed source / commercial | [BSD 3-Clause](http://opensource.org/licenses/BSD-3-Clause) |
| Closed source / commercial | [MIT](http://opensource.org/licenses/MIT) |

> Anyone interested in using, developing, or contributing to MORTIF is welcome — pick the license that best fits your needs.
