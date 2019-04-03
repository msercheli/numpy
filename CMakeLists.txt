CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(RezRepository)
include(ExternalProject)

set(numpy_version ${NUMPY_VERSION})
rez_set_archive(
    numpy_path numpy/numpy-${numpy_version}-cp27-cp27mu-manylinux1_x86_64.whl
    https://files.pythonhosted.org/packages/c4/33/8ec8dcdb4ede5d453047bbdbd01916dbaccdb63e98bba60989718f5f0876/numpy-${numpy_version}-cp27-cp27mu-manylinux1_x86_64.whl)

if(${REZ_BUILD_INSTALL})
    set(install_cmd make install ${make_args})
else()
    set(install_cmd "")
endif()

ExternalProject_add(
    numpy
    URL ${numpy_path}
    PREFIX numpy
    CONFIGURE_COMMAND ""
    BUILD_COMMAND ""
    INSTALL_COMMAND "${install_cmd}"
    ALWAYS 1
    BUILD_IN_SOURCE 1
)

add_custom_target(install)
