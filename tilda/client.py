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

import json

try:
    # python3
    from urllib.request import urlopen
    from urllib.error import URLError
    from urllib.parse import urlencode
except ImportError:
    # python2
    from urllib2 import urlopen, URLError
    from urllib import urlencode

from tilda.project import TildaProject
from tilda.page import TildaPage
from tilda.error import TildaError, NetworkError

ENDPOINT = 'http://api.tildacdn.info/v1'
STATUS_OK = 'FOUND'
STATUS_ERR = 'ERROR'


class Client(object):
    def __init__(self, public, secret):
        self.public = public
        self.secret = secret

    def _request(self, method, params=None):
        payload = {
            'publickey': self.public,
            'secretkey': self.secret
        }

        if params is not None:
            payload.update(params)

        try:
            url = ENDPOINT + method + '?' + urlencode(payload)
            response = urlopen(url)
        except URLError as e:
            response = e

        try:
            json_data = response.read()
            data = json.loads(json_data.decode('utf-8'))
        except ValueError as e:
            raise NetworkError('Invalid server response')

        if data.get('status') != STATUS_OK:
            raise TildaError(data)

        return data.get('result')

    def get_projects_list(self):
        """ Get projects list """
        try:
            result = self._request('/getprojectslist/')
            return [TildaProject(**p) for p in result]
        except NetworkError:
            return []

    def get_project(self, project_id):
        """ Get project info """
        try:
            result = self._request('/getproject/',
                                   {'projectid': project_id})
            return TildaProject(**result)
        except NetworkError:
            return []

    def get_project_export(self, project_id):
        """ Get project info for export """
        try:
            result = self._request('/getprojectexport/',
                                   {'projectid': project_id})
            return TildaProject(**result)
        except NetworkError:
            return []

    def get_pages_list(self, project_id):
        """ Get pages list """
        try:
            result = self._request('/getpageslist/',
                                   {'projectid': project_id})
            return [TildaPage(**p) for p in result]
        except NetworkError:
            return []

    def get_page(self, page_id):
        """ Get short page info and body html code """
        try:
            result = self._request('/getpage/',
                                   {'pageid': page_id})
            return TildaPage(**result)
        except NetworkError:
            return []

    def get_page_full(self, page_id):
        """ Get full page info and full html code """
        try:
            result = self._request('/getpagefull/',
                                   {'pageid': page_id})
            return TildaPage(**result)
        except NetworkError:
            return []

    def get_page_export(self, page_id):
        """ Get short page info for export and body html code """
        try:
            result = self._request('/getpageexport/',
                                   {'pageid': page_id})
            return TildaPage(**result)
        except NetworkError:
            return []

    def get_page_full_export(self, page_id):
        """ Get full page info for export and body html code """
        try:
            result = self._request('/getpagefullexport/',
                                   {'pageid': page_id})
            return TildaPage(**result)
        except NetworkError:
            return []
