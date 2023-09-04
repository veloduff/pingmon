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

import sys
import requests

progname = 'getipgeo'

_FIELDS = (
    'ip',
    'ip_decimal',
    'country',
    'country_iso',
    'country_eu',
    'region_name',
    'region_code',
    'metro_code',
    'zip_code',
    'city',
    'latitude',
    'longitude',
    'time_zone',
    'asn',
    'asn_org'
)

## user agent info (for later use)
#   "user_agent": {
#     "product": "curl",
#     "version": "7.79.1",
#     "raw_value": "curl/7.79.1"
# 

def main():

    url = 'https://ifconfig.co/json'
    r = requests.get(url)

    for f in _FIELDS:
        print('  {0:>20}: {1}'.format(f, r.json()[f]))


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print('\nReceived Keyboard interrupt. Exiting...')
    except ValueError as e:
        print(e)
    sys.exit(0)

