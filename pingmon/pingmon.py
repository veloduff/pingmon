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
import time
import argparse
from .pmonClass import PingMonitor


def main():

    pmon = PingMonitor()

    parser = argparse.ArgumentParser(description='pingmon - monitor and graph ping data')    
    parser.add_argument("-q", help="No output to STDOUT", action="store_true")
    requiredGroup = parser.add_argument_group('Required Arguments')
    requiredGroup.add_argument("-i", help = "IP address or host to ping", 
                               required=True, metavar="<ip/hostname>") 
    args = parser.parse_args()

    host = str(args.i)
    stdout = False if args.q else True

    day_today = pmon.get_date_time(dayonly=True)
    csv_file = open('ping.results.csv.{0}'.format(day_today), 'a', 1)
    raw_file = open('ping.results.raw.{0}'.format(day_today), 'a', 1)

    try:
        while True:
            ttl = None
            ping_time = None
            day_now = pmon.get_date_time(dayonly=True)
            if day_now != day_today:
                #
                # Set day and open files (or close old)
                #
                day_yesterday = day_today
                day_today = day_now
                csv_file.close()
                csv_file = open('ping.results.csv.{0}'.format(day_today), 'a', 1)
                raw_file.close()
                raw_file = open('ping.results.raw.{0}'.format(day_today), 'a', 1)
                pmon.build_graph('ping.results.csv.{0}'.format(day_yesterday),
                            'Ping results for date: {0}'.format(day_yesterday),
                            cr_file=True,
                            full_day_graph=True)
            #
            # Set time, get ping data, and write response out to files (raw and csv)
            #
            runtime = pmon.get_date_time()
            ping_data_all,ping_data_t = pmon.get_ping_data('1', host)
            if stdout:
                print('{0}: {1}'.format(runtime, ping_data_t))
            raw_file.write('{0},{1}\n'.format(runtime, ping_data_all))
            if ping_data_t:
                for w in ping_data_t.split():
                    if "ttl=" in w:
                        ttl = w.split("=")[1]
                    if "time=" in w:
                        ping_time = w.split("=")[1]
                try:                
                    # this is not the most accurate counter, but works for this
                    time.sleep(1)
                except KeyboardInterrupt:
                    print('\nReceived Keyboard interrupt. Exiting...')
                    sys.exit(0)
            csv_file.write('{0},{1}\n'.format(runtime, ping_time))
    except Exception as e:
        print("USAGE:  pingmon <ip_or_hostname>")
        raise ValueError(e)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print('\nReceived Keyboard interrupt. Exiting...')
    except ValueError as e:
        print(e)
    sys.exit(0)


