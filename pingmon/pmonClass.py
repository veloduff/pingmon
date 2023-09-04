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

import csv
import sys
import subprocess
from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib import dates as mdates


class PingMonitor:

    def __init__(self, **kwords):
        pass

    def get_date_time(self, dayonly=False):

        if dayonly:
            return datetime.now().strftime("%Y%m%d")

        return datetime.now().strftime("%Y%m%d.%H%M%S")


    def runcmd(self, cmd):
        try:
            output = subprocess.Popen(cmd, 
                                      stdout=subprocess.PIPE,
                                      stderr=subprocess.STDOUT,
                                      shell=True).communicate()[0]
        except KeyboardInterrupt:
            print('\nReceived Keyboard interrupt. Exiting...')
            sys.exit(0)

        return output


    def get_ping_data(self, count, host):
        """
        Send one ping request and return terse (one-line) output

        :param count:
        :param host:
        :return:
        """

        timeout = '1'

        terse_info = None
        packet_size = '56'  # will be 64 bytes, because of additional ICMP data bytes
        cmd = "ping -c {0} -s {1} -t {2} {3}".format(
            count, packet_size, timeout, host)

        cmd_o = self.runcmd(cmd)
        # 20200302 [Changed - looking for miss, to looking for hit], removed this line:
        #      l.startswith('PING', '--- ', 'round-trip', count + ' packets transmitted', 'rtt min/avg/max/mdev'):
        for l in cmd_o.decode().split('\n'):
            if l.startswith('64 bytes from {0}'.format(host)):
                terse_info = l
                break
            else:
                pass

        return cmd_o.decode().split('\n'), terse_info


    def build_graph(self, csv_file, title, cr_file=True, full_day_graph=True):

        x = []
        y = []

        with open(csv_file, 'r') as csvfile:
            plots = csv.reader(csvfile, delimiter=',')
            for row in plots:
                if row[1] == "None":
                    row[1] = 0
                row[0] = datetime.strptime(row[0], '%Y%m%d.%H%M%S')
                x.append(row[0])
                y.append(float(row[1]))
        plt.figure(figsize=(9, 6), dpi=150)
        if full_day_graph:
            date_min = x[0].replace(hour=00, minute=00, second=00)
            date_max = x[-1].replace(hour=23, minute=59, second=59)
            plt.xlim(date_min, date_max)
        plt.plot_date(
            x, y,
            label='Ping results',
            linestyle='None',
            # marker='.',
            fmt='.',
            linewidth=1,
            markersize=1
        )
        x_label_date_format = mdates.DateFormatter('%H:%M')
        # plt.xlabel('Day of month and Time of day (HH:MM)')
        plt.xlabel('Ping results for {0}\n(x label is time: HH:MM)'.format(x[0].strftime("%b %d %Y")), fontsize=8)
        plt.ylabel('Ping time in ms (latency)', fontsize=8)
        plt.title(title, fontsize=9)
        x_tick_date_format = mdates.DateFormatter('%H:%M')
        plt.gca().xaxis.set_major_formatter(x_tick_date_format)
        plt.legend()
        plt.xticks(fontsize=7)
        plt.yticks(fontsize=7)
        if cr_file:
            plt.savefig('{0}.png'.format(csv_file), dpi=150,
                        bbox_inches='tight', orientation='landscape')
        else:
            plt.show()
