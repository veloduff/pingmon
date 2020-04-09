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
import requests

progname = 'getipgeo'

_FIELDS = (
    'city',
    'country_name',
    'region_name',
    'postal_code',
    'isp',
    'host',
    'ip',
    'rdns',
    'asn',
    'latitude',
    'longitude',
    'metro_code',
    'timezone',
    'datetime'
   )


def main():

    url = 'https://tools.keycdn.com/geo.json'
    r = requests.post(url)

    for f in _FIELDS:
        print('  {0:>20}: {1}'.format(f, r.json()['data']['geo'][f]))


if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        print('\nReceived Keyboard interrupt. Exiting...')
    except ValueError as e:
        print(e)

