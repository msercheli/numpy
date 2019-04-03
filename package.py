# -*- coding: utf-8 -*-

name = "numpy"

version = "1.16.2"

description = \
    """
    Python pacage for array computing.
    """

build_requires = [
    "python-2.7"
]

def commands():
    env.LD_LIBRARY_PATH.prepend("{root}/lib")
    env.NUMPY_ROOT = '{root}'

uuid = "repository.numpy"
