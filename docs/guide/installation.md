---
title: Installation
---

# Installation

## Prerequisites

A Fortran 2003 compiler. MORTIF is tested on every push with gfortran 16.2; the fobos also has modes for the Intel
compilers (`*-intel`), not tested recently. MORTIF is developed on GNU/Linux.

## One-line install

```bash
curl -fsSL https://github.com/szaghi/MORTIF/releases/latest/download/install.sh | bash
```

It installs the latest release into `~/.local` with the build system you choose among those MORTIF ships
(`--build fobis|fpm`: a menu asks when you do not say), the compiler you name (`--fc`, `--gnu`, `--intel`), one install
per compiler (`lib/mortif/<compiler>-<version>/`, `include/mortif/<compiler>-<version>/`), and makes it usable through
pkg-config (`pkg-config --cflags --libs mortif`, with `PKG_CONFIG_PATH=$HOME/.local/lib/pkgconfig`). The release
carries PENF. Pass options after `bash -s --`, e.g. `... | bash -s -- --build fpm --prefix /opt/mortif`; `--help`
lists them all, `--uninstall` removes the install. The installer is FoBiS's
([One-line installer](https://szaghi.github.io/FoBiS/cookbook/installer)).

## Download

```bash
git clone https://github.com/szaghi/MORTIF
cd MORTIF
```

### Third-Party Dependencies

MORTIF has one dependency: [PENF](https://github.com/szaghi/PENF), which provides portable numeric kind parameters (`I4P`, `I8P`, `R4P`, etc.).

FoBiS fetches it (the dependency is declared in `fobos`), fpm too (it is declared in `fpm.toml`):

```bash
fobis fetch
```

## Build with FoBiS (recommended)

[FoBiS](https://github.com/szaghi/FoBiS) is the primary build system and is used by the CI pipeline.

```bash
pip install FoBiS.py
```

### List all build modes

```bash
fobis build --lmodes
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
fobis build --mode tests-gnu
./scripts/run_tests.sh
```

Compiled test executables are placed in `./exe/`.

### Build the library

```bash
# Static library (GNU gfortran)
fobis build --mode static-gnu

# Shared library (GNU gfortran)
fobis build --mode shared-gnu

# Static library (Intel Fortran)
fobis build --mode static-intel
```

### Coverage and documentation

```bash
fobis rule --ex makecoverage     # build + run tests + gcov report
fobis rule --ex makedoc          # build ford API documentation
```

Documentation generation requires `formal` and Node.js (VitePress).

## Build with fpm

```bash
fpm build                         # the library; fpm fetches PENF
fpm test                          # the correctness test
```

As a dependency of your fpm project:

```toml
[dependencies]
MORTIF = { git = "https://github.com/szaghi/MORTIF" }
```
