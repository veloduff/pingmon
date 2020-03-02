#!/usr/bin/env python


import os
import sys
import csv
import time
import argparse
import subprocess
from datetime import datetime
import matplotlib.pyplot as plt

progname = 'pingmon'

def get_date_time(dayonly=False):

    if dayonly:
        return datetime.now().strftime("%Y%m%d")

    return datetime.now().strftime("%Y%m%d.%H%M%S")


def runcmd(cmd):
    output = subprocess.Popen(cmd,
                              stdout=subprocess.PIPE,
                              stderr=subprocess.STDOUT,
                              shell=True).communicate()[0]
    return output


def get_ping_data(count, ip):
    """
    Send one ping request and return terse (one-line) output

    :param count:
    :param ip:
    :return:
    """

    terse_info = None
    cmd = "ping -c {0} {1}".format(count, ip)
    cmd_o = runcmd(cmd)
    for l in cmd_o.decode().split('\n'):
        if l.startswith(('PING', '--- ', 'round-trip', count + ' packets transmitted')):
            pass
        elif not l:
            pass
        else:
            terse_info = l

    return cmd_o.decode().split('\n'), terse_info


def build_graph(csv_file, title, cr_file=True):

    x = []
    y = []

    with open(csv_file,'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            if row[1] == "None":
                row[1] = 0
            row[0] = datetime.strptime(row[0], '%Y%m%d.%H%M%S')
            x.append(row[0])
            y.append(float(row[1]))
    plt.figure(figsize=(20, 10), dpi=150)
    plt.plot_date(x, y, label='Ping results', linestyle='None', marker='.', linewidth=1, markersize=3)
    plt.xlabel('Day of month and Time of day (MM HH:SS)')
    plt.ylabel('Ping time (latency)')
    plt.title(title)
    plt.legend()
    plt.xticks(fontsize=8)
    plt.yticks(fontsize=8)
    if cr_file:
        plt.savefig('{0}.png'.format(csv_file), dpi=150, bbox_inches='tight', orientation='landscape')
    else:
        plt.show()


def main():

    host =  str(sys.argv[1])

    plt.xlabel('Ping (latency)')
    plt.ylabel('Time of day')

    day_today = get_date_time(dayonly=True)
    csv_file = open('ping.results.csv.{0}'.format(day_today), 'a')
    raw_file = open('ping.results.raw.{0}'.format(day_today), 'a')

    try:
        while True:
            ttl = None
            ping_time = None
            day_now = get_date_time(dayonly=True)
            if day_now != day_today:
                day_yesterday = day_today
                day_today = day_now
                csv_file.close()
                csv_file = open('ping.results.csv.{0}'.format(day_today), 'a')
                raw_file.close()
                raw_file = open('ping.results.raw.{0}'.format(day_today), 'a')
                build_graph('ping.results.csv.{0}'.format(day_yesterday), 'Date: {0}'.format(day_yesterday))
            runtime = get_date_time()
            ping_data_all,ping_data_t = get_ping_data('1', host)
            print('{0}: {1}'.format(runtime, ping_data_t))
            raw_file.write('{0},{1}\n'.format(runtime, ping_data_all))
            if ping_data_t:
                for w in ping_data_t.split():
                    if "ttl=" in w:
                        ttl = w.split("=")[1]
                    if "time=" in w:
                        ping_time = w.split("=")[1]
                time.sleep(1)
            csv_file.write('{0},{1}\n'.format(runtime, ping_time))
    except Exception as e:
        print("USAGE:  pingmon <ip_or_hostname>")
        raise ValueError(e)


if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        print('\nReceived Keyboard interrupt. Exiting...')
    except ValueError as e:
        print(e)

