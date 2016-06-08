#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2016 dotzero <mail@dotzero.ru>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""This module contains a object that represents Tests for TildaError"""

import unittest
import sys
from tilda import TildaError
from tests.base import BaseTest

sys.path.append('.')


class TildaErrorTest(BaseTest, unittest.TestCase):
    """This object represents Tests for TildaError."""

    def test_page_init(self):
        """Test TildaError.__init__() method"""
        print('Testing TildaError.__init__()')

        try:
            raise TildaError()
        except TildaError as e:
            self.assertEqual(e.status, '')
            self.assertEqual(e.message, '')
            self.assertEqual(e.errorside, '')

    def test_page_str(self):
        """Test TildaError.__str__() method"""
        print('Testing TildaError.__str__()')

        try:
            raise TildaError({
                'status': 200,
                'message': 'OK',
            })
        except TildaError as e:
            self.assertEqual(e.status, 200)
            self.assertEqual(e.message, 'OK')
            self.assertEqual(str(e), 'OK')


if __name__ == '__main__':
    unittest.main()
