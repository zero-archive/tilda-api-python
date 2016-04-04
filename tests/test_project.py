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

"""This module contains a object that represents Tests for TildaProject"""

import unittest
import sys
import tilda
from tests.base import BaseTest

sys.path.append('.')


class TildaProjectTest(BaseTest, unittest.TestCase):
    """This object represents Tests for TildaProject."""

    def setUp(self):
        mock_response = self.to_json("""{"status":"FOUND","result":{
            "id":"12345",
            "title":"Blog",
            "descr":"I am a professional developer",
            "customdomain":"example.com",
            "css":[
                "http:\/\/tilda.ws\/css\/tilda-grid-3.0.css",
                "http:\/\/tilda.ws\/project36354\/tilda-blocks-2.5.css"
            ],
            "js":[
                "http:\/\/tilda.ws\/js\/jquery-1.10.2.min.js",
                "http:\/\/tilda.ws\/js\/tilda-scripts-2.5.js",
                "http:\/\/tilda.ws\/project36354\/tilda-blocks-2.3.js",
                "http:\/\/tilda.ws\/js\/bootstrap.min.js"
            ]}}""")

        self.response = mock_response.get('result')

    def test_project_init_empty(self):
        """Test TildaProject.__init__() method"""
        print('Testing TildaProject.__init__() - Empty')

        project = tilda.TildaProject()

        self.assertEqual(project.id, 0)
        self.assertEqual(project.title, '')
        self.assertEqual(project.descr, '')
        self.assertEqual(project.customdomain, '')
        self.assertEqual(project.css, list())
        self.assertEqual(project.js, list())
        self.assertEqual(project.export_csspath, '')
        self.assertEqual(project.export_jspath, '')
        self.assertEqual(project.export_imgpath, '')
        self.assertEqual(project.indexpageid, 0)
        self.assertEqual(project.images, list())
        self.assertEqual(project.htaccess, '')

    def test_project_init_non_empty(self):
        """Test TildaProject.__init__() method"""
        print('Testing TildaProject.__init__() - Non empty')

        project = tilda.TildaProject(**self.response)

        self.assertEqual(project.id, 12345)
        self.assertEqual(project.title, 'Blog')
        self.assertEqual(project.descr, 'I am a professional developer')
        self.assertEqual(project.customdomain, 'example.com')
        self.assertEqual(len(project.css), 2)
        self.assertEqual(len(project.js), 4)

    def test_project_to_dict(self):
        """Test TildaProject.to_dict() method"""
        print('Testing TildaProject.to_dict()')

        project = tilda.TildaProject(**self.response)
        project_dict = project.to_dict()

        self.assertTrue(self.is_dict(project_dict))
        self.assertEqual(project_dict['id'], int(self.response['id']))
        self.assertEqual(project_dict['title'], self.response['title'])
        self.assertEqual(project_dict['descr'], self.response['descr'])
        self.assertEqual(project_dict['customdomain'],
                         self.response['customdomain'])
        self.assertEqual(project_dict['css'], self.response['css'])
        self.assertEqual(project_dict['js'], self.response['js'])

    def test_project_to_json(self):
        """Test TildaProject.to_json() method"""
        print('Testing TildaProject.to_json()')

        project = tilda.TildaProject(**self.response)

        self.assertTrue(self.is_json(project.to_json()))


if __name__ == '__main__':
    unittest.main()
