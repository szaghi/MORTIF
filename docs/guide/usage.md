---
title: Usage
---

# Usage

All examples use `use mortif` and the standard `iso_fortran_env` integer kinds.

## 3D Encoding

Pass three `integer(int32)` indexes to `morton3D`. It returns an `integer(int64)` Morton code.

```fortran
use, intrinsic :: iso_fortran_env, only : int32, int64
use mortif

integer(int64) :: code

code = morton3D(i=0_int32, j=1_int32, k=0_int32)
print '(A,I20)', "Morton code of {0,1,0}: ", code   ! 2
```

The Z-order code is constructed by interleaving the binary representations of `i`, `j`, and `k`, with `i` in bit position 0, `j` in bit position 1, and `k` in bit position 2.

## 3D Decoding

Pass a 64-bit Morton code to `demorton3D`. The three decoded `integer(int32)` indexes are returned through `intent(inout)` arguments.

```fortran
use, intrinsic :: iso_fortran_env, only : int32, int64
use mortif

integer(int32) :: i, j, k

call demorton3D(code=2_int64, i=i, j=j, k=k)
print '(A,3(I0,1X))', "Decoded indexes of code 2: ", i, j, k   ! 0 1 0
```

::: tip
`demorton3D` is the exact inverse of `morton3D` — encoding then decoding (or vice versa) returns the original values, provided the indexes stay within the 21-bit limit per axis.
:::

## 2D Encoding

```fortran
use, intrinsic :: iso_fortran_env, only : int32, int64
use mortif

integer(int64) :: code

code = morton2D(i=3_int32, j=1_int32)
print '(A,I20)', "Morton code of {3,1}: ", code   ! 11
```

For 2D, `i` bits occupy even positions and `j` bits occupy odd positions of the 64-bit result.

## 2D Decoding

```fortran
use, intrinsic :: iso_fortran_env, only : int32, int64
use mortif

integer(int32) :: i, j

call demorton2D(code=11_int64, i=i, j=j)
print '(A,2(I0,1X))', "Decoded indexes of code 11: ", i, j   ! 3 1
```

## Elemental Use on Arrays

Because all four procedures are `elemental`, you can apply them directly to conformable arrays:

```fortran
use, intrinsic :: iso_fortran_env, only : int32, int64
use mortif

integer(int32) :: ix(4) = [0_int32, 1_int32, 2_int32, 3_int32]
integer(int32) :: iy(4) = [0_int32, 0_int32, 1_int32, 1_int32]
integer(int64) :: codes(4)
integer(int32) :: di(4), dj(4)

! Encode all 4 points at once
codes = morton2D(i=ix, j=iy)
print *, codes   ! 0 1 4 5

! Decode all 4 codes at once
call demorton2D(code=codes, i=di, j=dj)
print *, di      ! 0 1 2 3
print *, dj      ! 0 0 1 1
```

## Optional `b` Parameter

All four procedures accept an optional `b` argument (`integer(int16)`) that limits encoding to `b` significant bits per axis. Allowed values: 2, 4, 8, 16, 32.

This is useful when you know your indexes fit within a smaller range and want to keep only the relevant bits:

```fortran
use, intrinsic :: iso_fortran_env, only : int32, int64
use mortif

integer(int64) :: code

! Encode using only the lowest 8 bits of each index
code = morton3D(i=5_int32, j=3_int32, k=1_int32, b=8_int16)
```

::: warning 3D bit limit
For 3D encoding the Morton code fits in 64 bits only if each axis index has at most **21 significant bits** (values up to 2 097 151). Exceeding this limit produces a silently incorrect result — no runtime error is raised.
:::

::: warning 2D bit limit
For 2D encoding each axis may have at most **32 significant bits** (values up to 2³² − 1).
:::
