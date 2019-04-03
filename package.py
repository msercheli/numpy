# -*- coding: utf-8 -*-

name = "numpy"

version = "1.16.2"

description = \
    """
    Python package for array computing.
    """

build_requires = [
    "python-2.7"
]

build_command = "pip install /home/marcelo/Dev/payload/numpy/numpy-1.16.2-cp27-cp27mu-manylinux1_x86_64.whl --prefix=/home/marcelo/packages/numpy/1.16.2"

def commands():
    env.LD_LIBRARY_PATH.prepend("{root}/lib64")
    env.PYTHONPATH.append("{root}/lib64/python2.7/site-packages/numpy")
    env.NUMPY_ROOT = '{root}'

uuid = "repository.numpy"
