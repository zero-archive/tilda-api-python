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
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""This module contains a object that represents Tests for TildaPage"""

import unittest
import sys

sys.path.append('.')

import tilda
from tests.base import BaseTest


class TildaClientTest(BaseTest, unittest.TestCase):
    """This object represents Tests for Tilda Client."""

    def test_client_init(self):
        """Test Client.__init__() method"""
        print('Testing Client.__init__()')

        self.assertNotEqual(self._client.public, None)
        self.assertNotEqual(self._client.secret, None)

    def test_client_request(self):
        """Test Client._request() method"""
        print('Testing Client._request()')

        try:
            self._client._request(method='/test/')
        except Exception as e:
            self.assertTrue(isinstance(e, tilda.TildaError))
            self.assertNotEqual(e.status, None)
            self.assertNotEqual(e.message, None)
            self.assertNotEqual(e.errorside, None)

    def test_client_methods(self):
        """Test Client API methods"""
        print('Test Client API methods')

        project = self._client.get_projects_list()[0]
        self.assertNotEqual(project.id, 0)
        project = self._client.get_project(project_id=project.id)
        self.assertNotEqual(project.id, 0)
        project = self._client.get_project_export(project_id=project.id)
        self.assertNotEqual(project.id, 0)

        page = self._client.get_pages_list(project_id=project.id)[0]
        self.assertNotEqual(page.id, 0)
        page = self._client.get_page(page_id=page.id)
        self.assertNotEqual(page.id, 0)
        page = self._client.get_page_full(page_id=page.id)
        self.assertNotEqual(page.id, 0)
        page = self._client.get_page_export(page_id=page.id)
        self.assertNotEqual(page.id, 0)
        page = self._client.get_page_full_export(page_id=page.id)
        self.assertNotEqual(page.id, 0)


if __name__ == '__main__':
    unittest.main()
