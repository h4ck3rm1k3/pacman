#  Copyright (c) 2006 by Aurelien Foret <orelien@chez.com>
#  Copyright (c) 2006-2014 Pacman Developmet Team <pacman-dev@archlinux.org>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.


import os

import pmtest
import tap


class pmenv(object):
    """Environment object
    """

    testcases = []
    passed = 0
    failed = 0
    expectedfail = 0
    unexpectedpass = 0

    def __init__(self, root = "root"):
        self.root = os.path.abspath(root)
        self.pacman = {
            "bin": "pacman",
            "debug": 0,
            "gdb": 0,
            "valgrind": 0,
            "nolog": 0
        }

    def __str__(self):
        return "root = %s\n" \
               "pacman = %s" \
               % (self.root, self.pacman)

    def addtest(self, testcase):
        """
        """
        if not os.path.isfile(testcase):
            raise IOError("test file %s not found" % testcase)
        test = pmtest.pmtest(testcase, self.root)
        self.testcases.append(test)

    def run(self):
        """
        """
        tap.plan(len(self.testcases))
        for t in self.testcases:
            tap.diag("Running '%s'" % t.testname)

            t.load()
            t.generate(self.pacman)
            t.run(self.pacman)

            tap.diag("==> Checking rules")
            tap.todo = t.expectfailure
            tap.subtest(lambda: t.check(), t.description)

# vim: set ts=4 sw=4 et:
