---
title: API Reference
---

# API Reference

MORTIF exposes a single module:

```fortran
use mortif
```

The module uses [PENF](https://github.com/szaghi/PENF) kind parameters internally. The public interface uses standard `iso_fortran_env` kinds, but PENF aliases are accepted — `I4P` = `int32`, `I8P` = `int64`, `I2P` = `int16`.

## Public procedures

| Procedure | Kind | Description |
|-----------|------|-------------|
| [`morton2D`](#morton2d) | `elemental function` | Encode two 32-bit indexes → one 64-bit Morton code |
| [`demorton2D`](#demorton2d) | `elemental subroutine` | Decode a 64-bit Morton code → two 32-bit indexes |
| [`morton3D`](#morton3d) | `elemental function` | Encode three 32-bit indexes → one 64-bit Morton code |
| [`demorton3D`](#demorton3d) | `elemental subroutine` | Decode a 64-bit Morton code → three 32-bit indexes |

---

## `morton2D` {#morton2d}

Encodes two 32-bit integer indexes into a single 64-bit Morton code by interleaving their bits (`i` in even positions, `j` in odd positions).

**Signature:**
```fortran
code = morton2D(i, j, b)
```

| Argument | Intent | Type | Description |
|----------|--------|------|-------------|
| `i` | `in` | `integer(int32)` | First index (X axis) |
| `j` | `in` | `integer(int32)` | Second index (Y axis) |
| `b` | `in`, optional | `integer(int16)` | Significant bits per axis (2, 4, 8, 16, or 32; default 32) |
| return | — | `integer(int64)` | Morton code |

```fortran
use, intrinsic :: iso_fortran_env, only : int32, int64
use mortif

integer(int64) :: code

code = morton2D(i=0_int32, j=1_int32)          ! returns 2
code = morton2D(i=3_int32, j=1_int32)          ! returns 11
code = morton2D(i=5_int32, j=2_int32, b=8_int16)
```

::: tip
The maximum index value for 2D encoding is **2³² − 1** per axis (32 significant bits).
:::

---

## `demorton2D` {#demorton2d}

Decodes a 64-bit Morton code back into two 32-bit integer indexes. This is the exact inverse of `morton2D`.

**Signature:**
```fortran
call demorton2D(code, i, j, b)
```

| Argument | Intent | Type | Description |
|----------|--------|------|-------------|
| `code` | `in` | `integer(int64)` | Morton code to decode |
| `i` | `inout` | `integer(int32)` | Decoded first index (X axis) |
| `j` | `inout` | `integer(int32)` | Decoded second index (Y axis) |
| `b` | `in`, optional | `integer(int16)` | Significant bits per axis (2, 4, 8, 16, or 32; default 32) |

```fortran
use, intrinsic :: iso_fortran_env, only : int32, int64
use mortif

integer(int32) :: i, j

call demorton2D(code=2_int64, i=i, j=j)
print *, i, j   ! 0  1

call demorton2D(code=11_int64, i=i, j=j)
print *, i, j   ! 3  1
```

---

## `morton3D` {#morton3d}

Encodes three 32-bit integer indexes into a single 64-bit Morton code by interleaving their bits (`i` in positions 0, 3, 6, …; `j` in positions 1, 4, 7, …; `k` in positions 2, 5, 8, …).

**Signature:**
```fortran
code = morton3D(i, j, k, b)
```

| Argument | Intent | Type | Description |
|----------|--------|------|-------------|
| `i` | `in` | `integer(int32)` | First index (X axis) |
| `j` | `in` | `integer(int32)` | Second index (Y axis) |
| `k` | `in` | `integer(int32)` | Third index (Z axis) |
| `b` | `in`, optional | `integer(int16)` | Significant bits per axis (2, 4, 8, 16, or 32; default 32) |
| return | — | `integer(int64)` | Morton code |

```fortran
use, intrinsic :: iso_fortran_env, only : int32, int64
use mortif

integer(int64) :: code

code = morton3D(i=0_int32, j=1_int32, k=0_int32)   ! returns 2
code = morton3D(i=1_int32, j=0_int32, k=0_int32)   ! returns 1
code = morton3D(i=0_int32, j=0_int32, k=1_int32)   ! returns 4
```

::: warning
Due to the 64-bit code limit, each axis index must have **at most 21 significant bits** (max value 2 097 151 = 2²¹ − 1). Exceeding this silently produces an incorrect result.
:::

---

## `demorton3D` {#demorton3d}

Decodes a 64-bit Morton code back into three 32-bit integer indexes. This is the exact inverse of `morton3D`.

**Signature:**
```fortran
call demorton3D(code, i, j, k, b)
```

| Argument | Intent | Type | Description |
|----------|--------|------|-------------|
| `code` | `in` | `integer(int64)` | Morton code to decode |
| `i` | `inout` | `integer(int32)` | Decoded first index (X axis) |
| `j` | `inout` | `integer(int32)` | Decoded second index (Y axis) |
| `k` | `inout` | `integer(int32)` | Decoded third index (Z axis) |
| `b` | `in`, optional | `integer(int16)` | Significant bits per axis (2, 4, 8, 16; default 32) |

```fortran
use, intrinsic :: iso_fortran_env, only : int32, int64
use mortif

integer(int32) :: i, j, k

call demorton3D(code=2_int64, i=i, j=j, k=k)
print *, i, j, k   ! 0  1  0

call demorton3D(code=1317624576693539547_int64, i=i, j=j, k=k)
print *, i, j, k   ! 2097151  7  0
```

---

## Internal algorithm

The library uses two private elemental procedures to implement all four public routines:

- **`dilatate(i, b, z)`** — expands a 32-bit integer to 64 bits by spreading its `b` significant bits apart, inserting `z` zeros between each adjacent bit pair. This is *bit dilation*.
- **`contract(i, b, z, c)`** — the reverse: extracts every (`z+1`)-th bit from a 64-bit integer and packs them into a 32-bit result. This is *bit contraction*.

Both procedures use a sequence of bitwise AND / shift operations with pre-computed masks (stored as `parameter` constants in the module), avoiding any loops over individual bits.

For background on the algorithm see:
- Stocco & Schrack, *On Spatial Orders and Location Codes*, IEEE Trans. Computers, 2009.
- Baert, Lagae & Dutré, *Out-of-Core Construction of Sparse Voxel Octrees*, HPG 2013.
