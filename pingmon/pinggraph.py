#!/usr/bin/env python
#
# Copyright 2020 Mark Duffield
#
# Licensed under the Apache License, Version 2.0 (the "License"). You may not use this file
# except in compliance with the License. A copy of the License is located at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# or in the "license" file accompanying this file. This file is distributed on an "AS IS"
# BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations under the License.
#

import sys, os
import argparse
from .pmonClass import PingMonitor

progname = 'pinggraph'


def arg_parse():
    parser = argparse.ArgumentParser(prog=progname,
                                     description='Graph output from pingmon CSV file',
                                     epilog='pinggraph -f CSV_FILE -c -d',
                                     )
    req_group = parser.add_argument_group('required arguments')

    parser.add_argument('-c', '--create-file',
                        dest='c_value',
                        action='store_true',
                        help='PNG file is created, instead of displayed '
                        )

    parser.add_argument('-d', '--full-day',
                        dest='d_value',
                        action='store_true',
                        help="Show full Day on graph (00:00 to 23:59)"
                        )

    # required arguments
    req_group.add_argument('-f',
                           dest='f_value',
                           metavar='CSV_FILE',
                           help="CSV file to graph",
                           required=True,
                           type=str
                           )

    return parser.parse_args()


def main():

    pmon = PingMonitor()

    args = arg_parse()
    cr_file=args.c_value
    full_day_graph=args.d_value

    csv_file = args.f_value
    title = "Ping results from file  {0}".format(csv_file)

    try:
        pmon.build_graph(csv_file, title, cr_file=cr_file, full_day_graph=full_day_graph)
    except Exception as e:
        raise ValueError(e)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print('\nReceived Keyboard interrupt. Exiting...')
        sys.exit(0)
    except ValueError as e:
        print(e)
    sys.exit(0)

