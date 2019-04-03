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

build_command = "py -m pip install {env.REZ_REPO_PAYLOAD_DIR}/numpy-{this.version}-cp27-cp27mu-manylinux1_x86_64.whl --prefix={root}"

def commands():
    env.LD_LIBRARY_PATH.prepend("{root}/lib")
    env.NUMPY_ROOT = '{root}'

uuid = "repository.numpy"
