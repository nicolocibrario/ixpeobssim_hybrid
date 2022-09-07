#!/usr/bin/env python
#
# Copyright (C) 2016--2018, the ixpeobssim team.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

from __future__ import print_function, division


"""Dummy unit test for the codestyle phony module.
"""


import unittest

from ixpeobssim.utils.codestyle import square


class testcodestyle(unittest.TestCase):

    """Unit test for the codestyle module.
    """

    def test_square(self):
        """Test the square function.
        """
        self.assertEqual(square(2), 4)


if __name__ == '__main__':
    unittest.main()
