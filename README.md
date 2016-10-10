<a name="top"></a>

# MORTIF [![GitHub tag](https://img.shields.io/github/tag/szaghi/MORTIF.svg)]() [![Join the chat at https://gitter.im/szaghi/MORTIF](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/szaghi/MORTIF?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

[![License](https://img.shields.io/badge/license-GNU%20GeneraL%20Public%20License%20v3,%20GPLv3-blue.svg)]()
[![License](https://img.shields.io/badge/license-BSD2-red.svg)]()
[![License](https://img.shields.io/badge/license-BSD3-red.svg)]()
[![License](https://img.shields.io/badge/license-MIT-red.svg)]()

[![Status](https://img.shields.io/badge/status-stable-brightgreen.svg)]()
[![Build Status](https://travis-ci.org/szaghi/MORTIF.svg?branch=master)](https://travis-ci.org/szaghi/MORTIF)
[![Coverage Status](https://img.shields.io/codecov/c/github/szaghi/MORTIF.svg)](http://codecov.io/github/szaghi/MORTIF?branch=master)

### MORTIF, MORTon Indexer (Z-order) Fortran environment

A KISS pure Fortran Library to encode/decode, namely *to map*, multidimensional (integer) indexes into the Morton's index (Z-order)

- MORTIF is a pure Fortran (KISS) library for Morton's ordering;
- MORTIF is Fortran 2003+ standard compliant;
- MORTIF is OOP designed;
- MORTIF is a Free, Open Source Project.

#### Issues

[![GitHub issues](https://img.shields.io/github/issues/szaghi/MORTIF.svg)]()
[![Ready in backlog](https://badge.waffle.io/szaghi/MORTIF.png?label=ready&title=Ready)](https://waffle.io/szaghi/MORTIF)
[![In Progress](https://badge.waffle.io/szaghi/MORTIF.png?label=in%20progress&title=In%20Progress)](https://waffle.io/szaghi/MORTIF)
[![Open bugs](https://badge.waffle.io/szaghi/MORTIF.png?label=bug&title=Open%20Bugs)](https://waffle.io/szaghi/MORTIF)

#### Compiler Support

[![Compiler](https://img.shields.io/badge/GNU-v6.1.x+-brightgreen.svg)]()
[![Compiler](https://img.shields.io/badge/Intel-v16.x+-brightgreen.svg)]()
[![Compiler](https://img.shields.io/badge/IBM%20XL-not%20tested-yellow.svg)]()
[![Compiler](https://img.shields.io/badge/g95-not%20tested-yellow.svg)]()
[![Compiler](https://img.shields.io/badge/NAG-not%20tested-yellow.svg)]()
[![Compiler](https://img.shields.io/badge/PGI-not%20tested-yellow.svg)]()

---

| [What is MORTIF?](#what-is-mortif) | [Main features](#main-features) | [Copyrights](#copyrights) | [Documentation](#documentation) | [Install](#install) |

---

## What is MORTIF?

In mathematical analysis and computer science, Z-order, Morton order, or Morton code is a function which maps multidimensional data to one dimension while preserving locality of the data points. It was introduced in 1966 by G. M. Morton [[1]](#morton-1966). The z-value of a point in multidimensions is simply calculated by interleaving the binary representations of its coordinate values, see [wikipedia](). MORTIF is a pure Fortran library to encode/decode multidimensional indexes to/from Morton's order.

Go to [Top](#top)

## Main features

Here the main features are listed.

* [ ] User-friendly methods to encode/decode multidimensional indexes;
* [ ] Test Driven Developed (TDD);
* [ ] collaborative developed;
* [ ] well documented;
* [ ] free!

Any feature request is welcome.

Go to [Top](#top)

## Copyrights

MORTIF is a Free and Open Source Software (FOSS), it is distributed under a **very permissive** multi-licensing system: selectable licenses are [GPLv3](http://www.gnu.org/licenses/gpl-3.0.html), [BSD2-Clause](http://opensource.org/licenses/BSD-2-Clause), [BSD3-Clause](http://opensource.org/licenses/BSD-3-Clause) and [MIT](http://opensource.org/licenses/MIT), feel free to select the license that best matches your workflow.

> Anyone is interest to use, to develop or to contribute to MORTIF is welcome.

More details can be found on [wiki](https://github.com/szaghi/MORTIF/wiki/Copyrights).

Go to [Top](#top)

## Documentation

Besides this README file the MORTIF documentation is contained into its own [wiki](https://github.com/szaghi/MORTIF/wiki). Detailed documentation of the API is contained into the [GitHub Pages](http://szaghi.github.io/MORTIF/index.html) that can also be created locally by means of [ford tool](https://github.com/cmacmackin/ford).

### A Taste of MORTIF

To be written.

Go to [Top](#top)

## Install

MORTIF is a Fortran library composed by several modules.

> Before download and compile the library you must check the [requirements](https://github.com/szaghi/MORTIF/wiki/Requirements).

To download and build the project two main ways are available:

+ exploit the [install script](#install-script) that can be downloaded [here](https://github.com/szaghi/MORTIF/releases/latest)
+ [manually download and build](#manually-download-and-build):
  + [download](#download)
  + [build](#build)

---

### install script

MORTIF ships a bash script (downloadable from [here](https://github.com/szaghi/MORTIF/releases/latest)) that is able to automatize the download and build steps. The script `install.sh` has the following usage:

```shell
→ ./install.sh
Install script of MORTIF
Usage:

install.sh --help|-?
    Print this usage output and exit

install.sh --download|-d <arg> [--verbose|-v]
    Download the project

    --download|-d [arg]  Download the project, arg=git|wget to download with git or wget respectively
    --verbose|-v         Output verbose mode activation

install.sh --build|-b <arg> [--verbose|-v]
    Build the project

    --build|-b [arg]  Build the project, arg=fobis|make|cmake to build with FoBiS.py, GNU Make or CMake respectively
    --verbose|-v      Output verbose mode activation

Examples:

install.sh --download git
install.sh --build make
install.sh --download wget --build cmake
```

> The script does not cover all possibilities.

The script operation modes are 2 (*collapsible* into one-single-mode):

+ download a new fresh-clone of the latest master-release by means of:
  + [git](https://git-scm.com/);
  + [wget](https://www.gnu.org/software/wget/) (also [curl](https://curl.haxx.se/) is necessary);
+ build a fresh-clone project as static-linked library by means of:
  + [FoBiS.py](https://github.com/szaghi/FoBiS);
  + [GNU Make](https://www.gnu.org/software/make/);
  + [CMake](https://cmake.org/);

> you can mix any of the above combinations accordingly to the tools available.

Typical usages are:

```shell
# download and prepare the project by means of git and build with GNU Make
install.sh --dowload git --build make
# download and prepare the project by means of wget (curl) and build with CMake
install.sh --dowload wget --build cmake
# download and prepare the project by means of git and build with FoBiS.py
install.sh --dowload git --build fobis
```

---

### manually download and build

#### download

To download all the available releases and utilities (fobos, license, readme, etc...), it can be convenient to _clone_ whole the project:

```shell
git clone --recursive https://github.com/szaghi/MORTIF
cd MORTIF
git submodule update --init --recursive
```

Alternatively, you can directly download a release from GitHub server, see the [ChangeLog](https://github.com/szaghi/MORTIF/wiki/ChangeLog).

#### build

The most easy way to compile MORTIF is to use [FoBiS.py](https://github.com/szaghi/FoBiS) within the provided fobos file.

Consequently, it is strongly encouraged to install [FoBiS.py](https://github.com/szaghi/FoBiS#install).

| [Build by means of FoBiS](#build-by-means-of-fobis) | [Build by means of GNU Make](#build-by-means-of-gnu-make) | [Build by means of CMake](#build-by-means-of-cmake) |

---

#### build by means of FoBiS

FoBiS.py is a KISS tool for automatic building of modern Fortran projects. Providing very few options, FoBiS.py is able to build almost automatically complex Fortran projects with cumbersome inter-modules dependency. This removes the necessity to write complex makefile. Moreover, providing a very simple options file (in the FoBiS.py nomenclature indicated as `fobos` file) FoBiS.py can substitute the (ab)use of makefile for other project stuffs (build documentations, make project archive, etc...). MORTIF is shipped with a fobos file that can build the library in both _static_ and _shared_ forms and also build the `Test_Driver` program. The provided fobos file has several building modes.

##### listing fobos building modes
Typing:
```bash
FoBiS.py build -lmodes
```
the following message should be printed:
```bash
The fobos file defines the following modes:
 - "shared-gnu"
  - "static-gnu"
  - "test-driver-gnu"
  - "shared-gnu-debug"
  - "static-gnu-debug"
  - "test-driver-gnu-debug"
  - "shared-intel"
  - "static-intel"
  - "test-driver-intel"
  - "shared-intel-debug"
  - "static-intel-debug"
  - "test-driver-intel-debug"
```
The modes should be self-explicative: `shared`, `static` and `test-driver` are the modes for building (in release, optimized form) the shared and static versions of the library and the Test Driver program, respectively. The other 3 modes are the same, but in debug form instead of release one. `-gnu` use the `GNU gfortran` compiler while `-intel` the Intel one.

##### building the library
The `shared` or `static` directories are created accordingly to the form of the library built. The compiled objects and mod files are placed inside this directory, as well as the linked library.
###### release shared library
```bash
FoBiS.py build -mode shared-gnu
```
###### release static library
```bash
FoBiS.py build -mode static-gnu
```
###### debug shared library
```bash
FoBiS.py build -mode shared-gnu-debug
```
###### debug static library
```bash
FoBiS.py build -mode static-gnu-debug
```

##### building the Test Driver program
The `Test_Driver` directory is created. The compiled objects and mod files are placed inside this directory, as well as the linked program.
###### release test driver program
```bash
FoBiS.py build -mode test-driver-gnu
```
###### debug test driver program
```bash
FoBiS.py build -mode test-driver-gnu-debug
```

##### listing fobos rules
Typing:
```bash
FoBiS.py rule -ls
```
the following message should be printed:
```bash
The fobos file defines the following rules:
  - "makedoc" Rule for building documentation from source files
       Command => rm -rf doc/html/*
       Command => ford doc/main_page.md
       Command => cp -r doc/html/publish/* doc/html/
  - "deldoc" Rule for deleting documentation
       Command => rm -rf doc/html/*
  - "maketar" Rule for making tar archive of the project
       Command => tar -czf MORTIF.tar.gz *
  - "makecoverage" Rule for performing coverage analysis
       Command => FoBiS.py clean -mode test-driver-gnu
       Command => FoBiS.py build -mode test-driver-gnu -coverage
       Command => ./Test_Driver/Test_Driver
       Command => ./Test_Driver/Test_Driver -v
       Command => ./Test_Driver/Test_Driver -s 'Hello MORTIF' -i 2
       Command => ./Test_Driver/Test_Driver 33.0 -s 'Hello MORTIF' --integer_list 10 -3 87 -i 3 -r 64.123d0  --boolean --boolean_val .false.
  - "coverage-analysis" Rule for performing coverage analysis and saving reports in markdown
       Command => FoBiS.py clean -mode test-driver-gnu
       Command => FoBiS.py build -mode test-driver-gnu -coverage
       Command => ./Test_Driver/Test_Driver
       Command => ./Test_Driver/Test_Driver -v
       Command => ./Test_Driver/Test_Driver -s 'Hello MORTIF' -i 2
       Command => ./Test_Driver/Test_Driver 33.0 -s 'Hello MORTIF' --integer_list 10 -3 87 -i 3 -r 64.123d0  --boolean --boolean_val .false.
       Command => gcov -o Test_Driver/obj/ src/*
       Command => FoBiS.py rule -gcov_analyzer wiki/ Coverage-Analysis
       Command => rm -f *.gcov
```
The rules should be self-explicative.

---

#### build by means of GNU Make

Bad choice :-)

However, a makefile (generated by FoBiS.py...) to be used with a compatible GNU Make tool is [provided](https://github.com/szaghi/MORTIF/blob/master/makefile).

It is convenient to clone the whole MORTIF repository and run a *standard* make:

```shell
git clone --recursive https://github.com/szaghi/MORTIF
cd MORTIF
make -j 1
```

This commands build all tests (executables are in `exe/` directory). To build only the library (statically linked) type:

```shell
git clone --recursive https://github.com/szaghi/MORTIF
cd MORTIF
make -j 1 STATIC=yes
```

#### Build by means of CMake

Bad choice :-)

However, a CMake setup (kindly developed by [victorsndvg](https://github.com/victorsndvg)) is provided.

It is convenient to clone the whole MORTIF repository and run a *standard* CMake configure/build commands:

```shell
git clone --recursive https://github.com/szaghi/MORTIF $YOUR_MORTIF_PATH
mkdir build
cd build
cmake $YOUR_MORTIF_PATH
cmake --build .
```

If you want to run the tests suite type:

```shell
git clone --recursive https://github.com/szaghi/MORTIF $YOUR_MORTIF_PATH
mkdir build
cd build
cmake -DMORTIF_ENABLE_TESTS=ON $YOUR_MORTIF_PATH
cmake --build .
ctest
```

Go to [Top](#top)

### References

<a name="morton-1966"></a>[[1]](#morton-1966) *A computer Oriented Geodetic Data Base and a New Technique in File Sequencing*, Morton G.M., 1966, Technical Report IBM Ltd, Ottawa, Canada.

Go to [Top](#top)
