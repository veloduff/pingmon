#!/usr/bin/env python
#
# Copyright 2020 Mark Duffield
#
# Licensed under the Apache License, Version 2.0 (the "License"). You may not use this file
# except in compliance with the License. A copy of the License is located at
#
#     http://aws.amazon.com/apache2.0/
#
# or in the "license" file accompanying this file. This file is distributed on an "AS IS"
# BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations under the License.
#

import sys
import pingmon.pingmon as pingmon


def main():

    if len(sys.argv) < 2:
        print("USAGE:  pinggraph <csv_file> <opt: create file - True|False>")
        exit(0)

    csv_file = sys.argv[1]
    title = "Ping results from file  {0}".format(sys.argv[1])
    cr_file = False

    try:
        if sys.argv[2]:
            cr_file = sys.argv[2]
    except IndexError:
        pass

    try:
        pingmon.build_graph(csv_file, title, cr_file=cr_file)
    except Exception as e:
        raise ValueError(e)


if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        print('\nReceived Keyboard interrupt. Exiting...')
    except ValueError as e:
        print(e)

