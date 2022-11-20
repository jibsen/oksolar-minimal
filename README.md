
# OKSolar Minimal Generator

This is a simple script to generate the OKSolar Minimal theme files from
templates.


## Usage

Using [Meson](http://mesonbuild.com/) and [Ninja](https://ninja-build.org/):

    mkdir build
    cd build
    meson ..
    ninja

Or manually use the Python script `subtempl.py`. For instance to generate the
dark theme `colors.less` for Atom:

    subtempl.py dark.json atom/atom.less colors.less
