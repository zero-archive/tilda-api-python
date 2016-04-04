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
from datetime import datetime


class TildaBase(object):
    @staticmethod
    def _fromdatestring(string_date):
        """
        Args:
            string_date (string):
        Returns:
            datetime.datetime:
        """
        if not string_date:
            return None

        return datetime.strptime(string_date, '%Y-%m-%d %H:%M:%S')

    @staticmethod
    def _fromtimestamp(unixtime):
        """
        Args:
            unixtime (string):
        Returns:
            datetime.datetime:
        """
        if not unixtime:
            return None

        return datetime.fromtimestamp(int(unixtime))

    def to_json(self):
        """
        Returns:
            str:
        """
        data = dict()

        for key, value in self.__dict__.items():
            if value:
                if hasattr(value, 'to_dict'):
                    data[key] = value.to_dict()
                elif isinstance(value, datetime):
                    data[key] = value.strftime('%Y-%m-%d %H:%M:%S')
                else:
                    data[key] = value

        return json.dumps(data)

    def to_dict(self):
        """
        Returns:
            dict:
        """
        data = dict()

        for key, value in self.__dict__.items():
            if value:
                if hasattr(value, 'to_dict'):
                    data[key] = value.to_dict()
                else:
                    data[key] = value

        return data
