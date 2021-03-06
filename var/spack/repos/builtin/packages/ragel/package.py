# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Ragel(AutotoolsPackage):
    """Ragel State Machine Compiler
    Ragel compiles executable finite state machines from regular
    languages. Ragel targets C, C++ and ASM. Ragel state machines can
    not only recognize byte sequences as regular expression machines
    do, but can also execute code at arbitrary points in the
    recognition of a regular language. Code embedding is done using
    inline operators that do not disrupt the regular language syntax.
    """
    homepage = "http://www.colm.net/open-source/ragel"
    git      = "git://colm.net/ragel.git"
    url      = "http://www.colm.net/files/ragel/ragel-6.10.tar.gz"

    version('6.10', '748cae8b50cffe9efcaa5acebc6abf0d')

    depends_on('colm', type='build')
