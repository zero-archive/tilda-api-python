#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import optparse
import tilda


def parse_options(args=None, values=None):
    usage = "%prog [options] PUBLIC_KEY SECRET_KEY"
    desc = "A Python implementation of Tilda.cc API."

    parser = optparse.OptionParser(usage=usage, description=desc)
    parser.add_option('--projects', action='store_true', dest='projects', help='Get projects list')
    parser.add_option('--project', type='int', dest='project', metavar='PROJECT_ID', help='Get project info')
    parser.add_option('--pages', type='int', dest='pages', metavar='PROJECT_ID', help='Get pages list')
    parser.add_option('--page', type='int', dest='page', metavar='PAGE_ID', help='Get page info')
    parser.add_option('-o', '--output', dest='output_dir', metavar='DIR', help='Export to DIR')
    (options, args) = parser.parse_args(args, values)

    if len(args) != 2:
        print 'ERROR: No PUBLIC_KEY and SECRET_KEY'
        sys.exit(2)

    return args, options


def export_page(page, output_dir):
    filepath = output_dir + '/' + page.filename
    with open(filepath, 'w') as f:
        print('- Write file %s' % filepath)
        f.write(page.html.encode('utf-8'))


def run():
    keys, options = parse_options()

    api = tilda.Client(public=keys[0], secret=keys[1])

    if options.projects:
        print('[Get projects list]')
        for project in api.get_projects_list():
            print('- (%s) %s' % (project.id, project.title))

    if options.project:
        print('[Get project info]')
        project = api.get_project_export(options.project)
        print('- (%s) %s' % (project.id, project.title))
        print('-- %s' % (project.descr))

    if options.pages:
        print('[Get pages list]')
        for page in api.get_pages_list(options.pages):
            print('- (%s) %s' % (page.id, page.title))

    if options.page:
        print('[Get page info]')
        page = api.get_page_full(options.page)
        print('- (%s) %s' % (page.id, page.title))

        if options.output_dir:
            print('[Export to %s]' % options.output_dir)
            export_page(page, options.output_dir)


if __name__ == '__main__':
    run()
