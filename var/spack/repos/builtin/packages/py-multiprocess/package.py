# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyMultiprocess(PythonPackage):
    """Better multiprocessing and multithreading in Python"""

    homepage = "https://github.com/uqfoundation/multiprocess"
    url = "https://pypi.io/packages/source/m/multiprocess/multiprocess-0.70.5.zip"

    version('0.70.7', sha256='3394f1fbd0d87112690a877e49eb7917d851ee8d822294d522dd4deae12febdb')
    version('0.70.5', sha256='c4c196f3c4561dc1d78139c3e73709906a222d2fc166ef3eef895d8623df7267')
    version('0.70.4', sha256='a692c6dc8392c25b29391abb58a9fbdc1ac38bca73c6f27d787774201e68e12c')

    depends_on('python@2.6:2.8,3.1:')

    depends_on('py-setuptools@0.6:', type='build')
    depends_on('py-dill@0.2.6:', type=('build', 'run'))
    depends_on('py-dill@0.2.9:', type=('build', 'run'), when='@0.70.7:')

    def url_for_version(self, version):
        url = self.url.rsplit('/', 1)[0]
        if version >= Version('0.70.7'):
            url += '/multiprocess-{0}.tar.gz'
        else:
            url += '/multiprocess-{0}.zip'

        url = url.format(version)
        return url
