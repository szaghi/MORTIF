---
title: Features
---

# Features

## Encoding

- Encode a pair of 32-bit integer indexes into a single 64-bit Morton code with `morton2D`
- Encode three 32-bit integer indexes into a single 64-bit Morton code with `morton3D`
- Optional `b` parameter to restrict the encoding to 2, 4, 8, 16, or 32 significant bits per axis
- Returns a standard `integer(int64)` Morton code — no custom types required

## Decoding

- Decode a 64-bit Morton code back into two 32-bit indexes with `demorton2D`
- Decode a 64-bit Morton code back into three 32-bit indexes with `demorton3D`
- Fully symmetric with encoding — `demorton*` are the exact inverse of `morton*`

## Elemental Interface

All four public procedures are declared `elemental`. This means they work on:

- Scalars (`integer(int32)` arguments)
- Conformable arrays with no extra code — pass arrays of indexes, receive arrays of codes

```fortran
use mortif
use, intrinsic :: iso_fortran_env, only : int32, int64

integer(int32) :: ix(4) = [0, 1, 2, 3]
integer(int32) :: iy(4) = [0, 0, 1, 1]
integer(int64) :: codes(4)

! Encode an entire array of 2D points at once
codes = morton2D(i=ix, j=iy)
```

## Encoding Limitations

Because Morton codes are stored in a 64-bit integer, the following bit limits apply:

| Dimension | Max significant bits per axis | Max index value |
|-----------|------------------------------|-----------------|
| 2D | 32 | 2³² − 1 ≈ 4.3 × 10⁹ |
| 3D | 21 | 2²¹ − 1 = 2 097 151 |

::: warning
No range check is performed at runtime to avoid computational overhead. It is the caller's responsibility to stay within the 21-bit limit for 3D indexes.
:::

## Compiler Support

| Compiler | Status |
|----------|--------|
| GNU gfortran ≥ 6.1 | Supported |
| Intel Fortran ≥ 16.x | Supported |
| IBM XL Fortran | Not tested |
| g95 | Not tested |
| NAG Fortran | Not tested |
| PGI / NVIDIA | Not tested |

## Design Principles

- **Pure Fortran** — no C extensions, no system calls, no external libraries beyond PENF
- **Elemental** — all procedures are declared `elemental`, enabling array-at-a-time use
- **KISS** — the entire library is a single 194-line Fortran module
- **TDD** — developed test-first; correctness tests cover encoding and round-trip decoding
- **Free & Open Source** — multi-licensed for both FOSS and commercial use
