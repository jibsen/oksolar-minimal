#!/usr/bin/env python3

# Copyright (c) 2018-2022 Joergen Ibsen
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.

"""
Substitute template strings.

Read a mapping in JSON format and convert the input by substituting template
strings.

Example:
    If the map contains {'foo': 'bar'}, all instances of $foo in the input
    will be replaced with bar in the output. Use ${foo}s to produce bars,
    and $$ to insert a literal $.

See Also:
    https://www.python.org/dev/peps/pep-0292/
"""

import argparse
import json

from string import Template
from sys import exit, stderr

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Substitute template strings.',
        epilog='Use `-\' to read from stdin and/or write to stdout.')
    parser.add_argument('mapfile', type=argparse.FileType('r', encoding='UTF-8'),
                        help='mapping in JSON format')
    parser.add_argument('infile', type=argparse.FileType('r', encoding='UTF-8'),
                        help='template file')
    parser.add_argument('outfile', type=argparse.FileType('w', encoding='UTF-8'),
                        help='output file')
    args = parser.parse_args()

    mapping = json.load(args.mapfile)
    lineno = 1
    try:
        for line in args.infile:
            args.outfile.write(Template(line).substitute(mapping))
            lineno += 1
    except KeyError as e:
        print('KeyError: {}: line {}'.format(e, lineno), file=stderr)
        exit(-1)
    except ValueError as e:
        print('ValueError: {}: line {}'.format(e, lineno), file=stderr)
        exit(-1)
