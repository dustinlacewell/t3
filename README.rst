==
t3
==


.. image:: https://img.shields.io/pypi/v/t3.svg
        :target: https://pypi.python.org/pypi/t3

.. image:: https://img.shields.io/travis/dustinlacewell/t3.svg
        :target: https://travis-ci.org/dustinlacewell/t3

.. image:: https://readthedocs.org/projects/t3/badge/?version=latest
        :target: https://t3.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status





A TADS3 build and code-generation system.


* Free software: MIT license
* Documentation: https://t3.readthedocs.io.


Features
--------

* Generate TADS makefiles automatically
* Generate TADS source-code from Trizbort XML maps


Installation
------------

This is a typical Python project so use the `setup.py`:

    python setup.py install


On NixOS:

    nix-build .
    result/bin/t3

or

    nix-shell
    t3

or

    nix-env -i -f .
    t3


Overview
--------

t3 is a cli tool with two major features:

- Generates and builds TADS3 project makefiles.
- Generates TADS3 source-code from Trizbort XML maps.


This is a rewrite of an older project [t3sketch](https://github.com/dustinlacewell/t3sketch)


**Makefile Generation**

TADS3 makefiles are not the worst thing to work with but I found that each time
I wanted to start a new TADS3 experiment I had to digest it all again. t3
solves this by inspecting your source code and generating a reasonable
makefile. t3 can also build and clean the project as well.

**Source-code Generation**

[Trizbort](http://www.trizbort.com/) is a GUI app where you can draw IF worlds
and generate the corresponding code. However the support for Inform and other
systems is much more sophisticated than it is for TADS3. Unlike Trizbort which
is C#, t3 uses Python and Jinja2 templates to perform this code
generation. Jinja2 is a powerful templating system and Python is cross-platform
making things all around a bit more accessible.

Code-generation is done in a very clean and modular way. By setting the class
of objects in Trizbort, they'll inherit any custom code of those classes when
they are generated. This avoids the problem of regeneration undoing
modifications to generated code.

