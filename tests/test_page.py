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

"""This module contains a object that represents Tests for TildaPage"""

import unittest
import sys
import tilda
from datetime import datetime
from tests.base import BaseTest

sys.path.append('.')


class TildaPageTest(BaseTest, unittest.TestCase):
    """This object represents Tests for TildaPage."""

    def setUp(self):
        mock_response = self.to_json("""{"status":"FOUND","result":{
            "id":"54321",
            "projectid":"12345",
            "title":"Page",
            "descr":"Blog post",
            "img":"https:\/\/ucarecdn.com\/covermain.jpg",
            "featureimg":"http:\/\/ucarecdn.com\/featureimg.jpg",
            "alias":"post",
            "date":"2016-03-14 17:59:12",
            "sort":"30",
            "published":"1458049840",
            "filename":"page54321.html",
            "html":"<html>"}}""")

        self.response = mock_response.get('result')

    def test_page_init_empty(self):
        """Test TildaPage.__init__() method"""
        print('Testing TildaPage.__init__() - Empty')

        page = tilda.TildaPage()

        self.assertEqual(page.id, 0)
        self.assertEqual(page.projectid, 0)
        self.assertEqual(page.title, '')
        self.assertEqual(page.descr, '')
        self.assertEqual(page.img, '')
        self.assertEqual(page.featureimg, '')
        self.assertEqual(page.alias, '')
        self.assertEqual(page.date, None)
        self.assertEqual(page.sort, 0)
        self.assertEqual(page.published, None)
        self.assertEqual(page.filename, '')
        self.assertEqual(page.html, '')
        self.assertEqual(page.css, list())
        self.assertEqual(page.js, list())
        self.assertEqual(page.images, list())

    def test_page_init_non_empty(self):
        """Test TildaPage.__init__() method"""
        print('Testing TildaPage.__init__() - Non empty')

        page = tilda.TildaPage(**self.response)

        self.assertEqual(page.id, 54321)
        self.assertEqual(page.projectid, 12345)
        self.assertEqual(page.title, 'Page')
        self.assertEqual(page.descr, 'Blog post')
        self.assertEqual(page.img, 'https://ucarecdn.com/covermain.jpg')
        self.assertEqual(page.featureimg, 'http://ucarecdn.com/featureimg.jpg')
        self.assertEqual(page.alias, 'post')
        self.assertTrue(isinstance(page.date, datetime))
        self.assertEqual(page.sort, 30)
        self.assertTrue(isinstance(page.published, datetime))
        self.assertEqual(page.filename, 'page54321.html')
        self.assertEqual(page.html, '<html>')

    def test_page_str(self):
        """Test TildaPage.__str__() method"""
        print('Testing TildaPage.__str__()')

        page = tilda.TildaPage(**self.response)

        self.assertEqual(str(page), '(54321) Page')

    def test_page_repr(self):
        """Test TildaPage.__repr__() method"""
        print('Testing TildaPage.__repr__()')

        page = tilda.TildaPage(**self.response)

        self.assertIn('tilda.page.TildaPage', repr(page))

    def test_page_to_dict(self):
        """Test TildaPage.to_dict() method"""
        print('Testing TildaPage.to_dict()')

        page = tilda.TildaPage(**self.response)
        page_dict = page.to_dict()

        self.assertTrue(self.is_dict(page_dict))
        self.assertEqual(page_dict['id'], int(self.response['id']))
        self.assertEqual(page_dict['projectid'],
                         int(self.response['projectid']))
        self.assertEqual(page_dict['title'], self.response['title'])
        self.assertEqual(page_dict['descr'], self.response['descr'])
        self.assertEqual(page_dict['img'], self.response['img'])
        self.assertEqual(page_dict['featureimg'], self.response['featureimg'])
        self.assertEqual(page_dict['alias'], self.response['alias'])
        self.assertEqual(page_dict['date'].strftime('%Y-%m-%d %H:%M:%S'),
                         self.response['date'])
        self.assertEqual(page_dict['sort'], int(self.response['sort']))
        self.assertEqual(page_dict['published'].strftime('%s'),
                         self.response['published'])
        self.assertEqual(page_dict['filename'], self.response['filename'])
        self.assertEqual(page_dict['html'], self.response['html'])

    def test_page_to_json(self):
        """Test TildaPage.to_json() method"""
        print('Testing TildaPage.to_json()')

        page = tilda.TildaPage(**self.response)

        self.assertTrue(self.is_json(page.to_json()))


if __name__ == '__main__':
    unittest.main()
