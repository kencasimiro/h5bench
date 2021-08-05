# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class H5bench(CMakePackage):
    """H5bench is a suite of parallel I/O benchmarks or kernels representing I/O patterns that 
       are commonly used in HDF5 applications on high performance computing systems."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://h5bench.readthedocs.io/en/latest/"
    git      = "https://github.com/hpc-io/h5bench.git"

    maintainers = ['houjun', 'sbyna', 'jeanbez']

    version('master', branch='master')

    variant('async', default=False, description='Build and run H5bench Async')
    # how do i get vol-async? if spack package isnt done yet for Async variant?


    depends_on('cmake')
    depends_on('mpi')
    depends_on('hdf5@develop-1.13')
    depends_on('vol-async', when='+async')

    
    def cmake_args(self):
        args = []

        if '+async' in self.spec:
            args.append('-DWITH_ASYNC_VOL:BOOL=ON -DCMAKE_C_COMPILER=h5pcc')
            # where to find the correct paths for directories?
            # -DCMAKE_C_FLAGS="-I/vol-async/src -L/vol-async/src"
        else:
            args.append('-DCMAKE_C_COMPILER=h5pcc')

        return args
