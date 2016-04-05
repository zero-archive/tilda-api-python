# Python Tilda.cc API

[![PyPI](https://img.shields.io/pypi/v/tilda-api.svg)](https://pypi.python.org/pypi/tilda-api)
[![Build Status](https://travis-ci.org/dotzero/tilda-api-python.svg?branch=master)](https://travis-ci.org/dotzero/tilda-api-python)
[![Coverage Status](https://coveralls.io/repos/github/dotzero/tilda-api-python/badge.svg?branch=master)](https://coveralls.io/github/dotzero/tilda-api-python?branch=master)

As complete as possible implementation of Tilda.cc API.

The project provides an almost exhaustive access to the Tilda.cc API, through an *object oriented* Python interface.

## Features

* Get projects list
* Get project info
* Get project info for export
* Get pages list
* Get short page info and body html code
* Get full page info and full html code
* Get short page info for export and body html code
* Get full page info for export and body html code

## Requires

* python >= 2.6
* python >= 3.2

## Installation

### From Pypi

You can install tilda-api-python using:

    pip install tilda-api

### From source

    git clone https://github.com/dotzero/tilda-api-python
    cd tilda-api-python
    python setup.py install

## Usage

To create an instance of the tilda.Client:

    >>> import tilda
    >>> api = tilda.Client(public='000000000000', secret='999999999999')

To get projects list:

    >>> projects = api.get_projects_list()
    >>> projects[0].to_dict()
    ... or
    >>> projects[0].id
    >>> projects[0].title

To get project info:

    >>> project = api.get_project(project_id=00000)
    >>> project.to_dict()
    ... or
    >>> project.id
    >>> project.title

To get project info for export:

    >>> project = api.get_project_export(project_id=00000)
    >>> project.to_dict()
    ... or
    >>> project.id
    >>> project.title

To get pages list:

    >>> pages = api.get_pages_list(project_id=00000)
    >>> pages[0].to_dict()
    ... or
    >>> pages[0].id
    >>> pages[0].title

To get short page info and body html code:

    >>> page = api.get_page(page_id=00000)
    >>> page.to_dict()
    ... or
    >>> page.title
    >>> page.html

To get full page info and full html code:

    >>> page = api.get_page_full(page_id=00000)
    >>> page.to_dict()
    ... or
    >>> page.title
    >>> page.html

To get short page info for export and body html code:

    >>> page = api.get_page_export(page_id=00000)
    >>> page.to_dict()
    ... or
    >>> page.title
    >>> page.html

To get full page info for export and body html code:

    >>> page = api.get_page_full_export(page_id=00000)
    >>> page.to_dict()
    ... or
    >>> page.title
    >>> page.html

