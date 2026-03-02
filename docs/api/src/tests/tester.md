---
title: tester
---

# tester

> Minimal test framework replacing fortran_tester dependency.

**Source**: `src/tests/mortif_test_correctness.f90`

**Dependencies**

```mermaid
graph LR
  tester["tester"] --> iso_fortran_env["iso_fortran_env"]
```

## Contents

- [tester_t](#tester-t)
- [init](#init)
- [assert_equal_i32](#assert-equal-i32)
- [assert_equal_i64](#assert-equal-i64)
- [assert_equal_logical](#assert-equal-logical)
- [print_results](#print-results)

## Derived Types

### tester_t

#### Components

| Name | Type | Attributes | Description |
|------|------|------------|-------------|
| `n_pass` | integer(kind=int32) |  |  |
| `n_fail` | integer(kind=int32) |  |  |

#### Type-Bound Procedures

| Name | Attributes | Description |
|------|------------|-------------|
| `init` |  |  |
| `assert_equal_i32` |  |  |
| `assert_equal_i64` |  |  |
| `assert_equal_logical` |  |  |
| `assert_equal` |  |  |
| `print` |  |  |

## Subroutines

### init

```fortran
subroutine init(self)
```

**Arguments**

| Name | Type | Intent | Attributes | Description |
|------|------|--------|------------|-------------|
| `self` | class([tester_t](/api/src/tests/tester#tester-t)) | inout |  |  |

### assert_equal_i32

```fortran
subroutine assert_equal_i32(self, a, b)
```

**Arguments**

| Name | Type | Intent | Attributes | Description |
|------|------|--------|------------|-------------|
| `self` | class([tester_t](/api/src/tests/tester#tester-t)) | inout |  |  |
| `a` | integer(kind=int32) | in |  |  |
| `b` | integer(kind=int32) | in |  |  |

### assert_equal_i64

```fortran
subroutine assert_equal_i64(self, a, b)
```

**Arguments**

| Name | Type | Intent | Attributes | Description |
|------|------|--------|------------|-------------|
| `self` | class([tester_t](/api/src/tests/tester#tester-t)) | inout |  |  |
| `a` | integer(kind=int64) | in |  |  |
| `b` | integer(kind=int64) | in |  |  |

### assert_equal_logical

```fortran
subroutine assert_equal_logical(self, a, b)
```

**Arguments**

| Name | Type | Intent | Attributes | Description |
|------|------|--------|------------|-------------|
| `self` | class([tester_t](/api/src/tests/tester#tester-t)) | inout |  |  |
| `a` | logical | in |  |  |
| `b` | logical | in |  |  |

### print_results

```fortran
subroutine print_results(self)
```

**Arguments**

| Name | Type | Intent | Attributes | Description |
|------|------|--------|------------|-------------|
| `self` | class([tester_t](/api/src/tests/tester#tester-t)) | in |  |  |
