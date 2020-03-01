# pingmon [![PyPi Status](https://badge.fury.io/py/pingmon.png)](https://badge.fury.io/py/pingmon)

Monitor, record, and display ping results


## License

This library is licensed under the Apache 2.0 License. 

## Requires

* matplotlib 

## Installation

```
pip install pingmon 
```

## What it does (creates three files)

```pingmon``` monitors a ping to a host or ip address, using ```ping -c <ip_or_hostname>``` and capturing the results. Three files are created in the directory that ```pingmon``` is run from:

* ```ping.results.csv.<YYYYMMDD>``` :  CSV data that has date.time (YYYYMMDD.HHMMSS) and the time the ping took in ms.
* ```ping.results.raw.<YYYYMMDD>``` :  The raw output with date.time and a list output from the ping command.
* ```ping.results.csv.<YYYYMMDD>.png``` : A high resolution PNG graph that is created when the day is over (23:59:59 is the last entry) that shows a plot of each ping for the entire day.


### Examples of each file:

**CSV File:**
```
20200229.161158,26.726
20200229.161159,28.684
20200229.161322,39.558
20200229.161533,26.188
20200229.161535,36.179
20200229.161940,25.488
20200229.162017,28.074
20200229.162018,32.775
20200229.170008,31.615
20200229.170044,33.969
```

**Raw file**
```
20200229.235949,['PING 8.8.8.8 (8.8.8.8): 56 data bytes', '64 bytes from 8.8.8.8: icmp_seq=0 ttl=54 time=17.110 ms', '', '--- 8.8.8.8 ping statistics ---', '1 packets transmitted, 1 packets received, 0.0% packet loss', 'round-trip min/avg/max/stddev = 17.110/17.110/17.110/0.000 ms', '']
20200229.235950,['PING 8.8.8.8 (8.8.8.8): 56 data bytes', '64 bytes from 8.8.8.8: icmp_seq=0 ttl=54 time=21.047 ms', '', '--- 8.8.8.8 ping statistics ---', '1 packets transmitted, 1 packets received, 0.0% packet loss', 'round-trip min/avg/max/stddev = 21.047/21.047/21.047/0.000 ms', '']
20200229.235951,['PING 8.8.8.8 (8.8.8.8): 56 data bytes', '64 bytes from 8.8.8.8: icmp_seq=0 ttl=54 time=30.030 ms', '', '--- 8.8.8.8 ping statistics ---', '1 packets transmitted, 1 packets received, 0.0% packet loss', 'round-trip min/avg/max/stddev = 30.030/30.030/30.030/0.000 ms', '']
20200229.235952,['PING 8.8.8.8 (8.8.8.8): 56 data bytes', '64 bytes from 8.8.8.8: icmp_seq=0 ttl=54 time=18.898 ms', '', '--- 8.8.8.8 ping statistics ---', '1 packets transmitted, 1 packets received, 0.0% packet loss', 'round-trip min/avg/max/stddev = 18.898/18.898/18.898/0.000 ms', '']
20200229.235954,['PING 8.8.8.8 (8.8.8.8): 56 data bytes', '64 bytes from 8.8.8.8: icmp_seq=0 ttl=54 time=24.082 ms', '', '--- 8.8.8.8 ping statistics ---', '1 packets transmitted, 1 packets received, 0.0% packet loss', 'round-trip min/avg/max/stddev = 24.082/24.082/24.082/0.000 ms', '']
20200229.235955,['PING 8.8.8.8 (8.8.8.8): 56 data bytes', '64 bytes from 8.8.8.8: icmp_seq=0 ttl=54 time=35.844 ms', '', '--- 8.8.8.8 ping statistics ---', '1 packets transmitted, 1 packets received, 0.0% packet loss', 'round-trip min/avg/max/stddev = 35.844/35.844/35.844/0.000 ms', '']
20200229.235956,['PING 8.8.8.8 (8.8.8.8): 56 data bytes', '64 bytes from 8.8.8.8: icmp_seq=0 ttl=54 time=28.508 ms', '', '--- 8.8.8.8 ping statistics ---', '1 packets transmitted, 1 packets received, 0.0% packet loss', 'round-trip min/avg/max/stddev = 28.508/28.508/28.508/0.000 ms', '']
20200229.235957,['PING 8.8.8.8 (8.8.8.8): 56 data bytes', '64 bytes from 8.8.8.8: icmp_seq=0 ttl=54 time=20.307 ms', '', '--- 8.8.8.8 ping statistics ---', '1 packets transmitted, 1 packets received, 0.0% packet loss', 'round-trip min/avg/max/stddev = 20.307/20.307/20.307/0.000 ms', '']
20200229.235958,['PING 8.8.8.8 (8.8.8.8): 56 data bytes', '64 bytes from 8.8.8.8: icmp_seq=0 ttl=54 time=33.487 ms', '', '--- 8.8.8.8 ping statistics ---', '1 packets transmitted, 1 packets received, 0.0% packet loss', 'round-trip min/avg/max/stddev = 33.487/33.487/33.487/0.000 ms', '']
20200229.235959,['PING 8.8.8.8 (8.8.8.8): 56 data bytes', '64 bytes from 8.8.8.8: icmp_seq=0 ttl=54 time=22.552 ms', '', '--- 8.8.8.8 ping statistics ---', '1 packets transmitted, 1 packets received, 0.0% packet loss', 'round-trip min/avg/max/stddev = 22.552/22.552/22.552/0.000 ms', '']
```

**Plot image from CSV file**

![Plot image](/_images/ping.results.csv.20200229.png)


