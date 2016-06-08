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

from tilda.base import TildaBase


class TildaProject(TildaBase):
    def __init__(self, *args, **kwargs):
        # Basic fields
        self.id = int(kwargs.get('id', 0))
        self.title = kwargs.get('title', '')
        self.descr = kwargs.get('descr', '')
        self.customdomain = kwargs.get('customdomain', '')
        self.css = kwargs.get('css', list())
        self.js = kwargs.get('js', list())
        # Export fields
        self.export_csspath = kwargs.get('export_csspath', '')
        self.export_jspath = kwargs.get('export_jspath', '')
        self.export_imgpath = kwargs.get('export_imgpath', '')
        self.indexpageid = int(kwargs.get('indexpageid', 0))
        self.images = kwargs.get('images', list())
        self.htaccess = kwargs.get('htaccess', '')

    def __str__(self):
        return '(%d) %s' % (self.id, self.title)

    def __repr__(self):
        return '%s(%r)' % (self.__class__, self.__dict__)
