<!--PROPS
{
    "estTime": 10
}
-->

# Introduction



<!--TOC_START-->
## Contents
- [Overview](#overview)
- [Traceroute Output](#traceroute-output)
	- [Example Output](#example-output)
	- [Output Meaning](#output-meaning)
		- [Hop Number](#hop-number)
		- [Name & IP Address](#name--ip-address)
		- [RTT Columns](#rtt-columns)
- [Tasks](#tasks)
	- [Installation](#installation)
		- [Ubuntu/Debian](#ubuntudebian)
		- [CentOS/RHEL](#centosrhel)
	- [Try it Out](#try-it-out)

<!--TOC_END-->
## Overview
In computing, `traceroute` and `tracert` are computer network diagnostic commands for displaying the route (path) and measuring transit delays of packets across an Internet Protocol (IP) network.

Here's an example of a path for going to `google.co.uk` from a computer in London:
![Traceroute Map](https://i.imgur.com/cE9UPCB.png)

The history of the route is recorded as the round-trip times of the packets received from each successive host (remote node) in the route (path); the sum of the mean times in each hop is a measure of the total time spent to establish the connection.
Traceroute proceeds unless all (three) sent packets are lost more than twice. If this happens, the connection is lost and the route cannot be evaluated.

## Traceroute Output

### Example Output
Below is an example output from a basic `traceroute` command to `google.com`:
```text
traceroute to google.com (172.217.169.78), 30 hops max, 60 byte packets
 1  192.168.0.254 (192.168.0.254)  3.141 ms  3.123 ms  3.129 ms
 2  172.16.25.2 (172.16.25.2)  3.753 ms  3.750 ms  3.738 ms
 3  no-reverse-dns.metronet-uk.com (164.39.75.105)  6.859 ms  6.861 ms  6.857 ms
 4  no-reverse-dns.metronet-uk.com (164.39.85.25)  6.830 ms  6.816 ms  6.863 ms
 5  no-reverse-dns.metronet-uk.com (85.199.237.157)  6.867 ms  6.864 ms  6.876 ms
 6  no-reverse-dns.metronet-uk.com (51.179.187.200)  6.801 ms  5.118 ms  4.975 ms
 7  no-reverse-dns.metronet-uk.com (85.199.224.241)  4.932 ms * *
 8  te1-5.man-tck1gw.metronet-uk.com (85.199.239.165)  3.002 ms  3.098 ms  3.080 ms
 9  te1-4.man-tcw1gw.metronet-uk.com (77.75.191.34)  11.700 ms  11.861 ms  11.847 ms
10  te0-0-0-0.man-tcw2br.metronet-uk.com (164.39.85.50)  3.472 ms  3.451 ms  3.421 ms
11  po-5-11.bb1.man2.uk.m247.com (148.252.210.96)  44.219 ms  44.156 ms  43.243 ms
12  te-9-2-0.core-dc2.man4.uk.m247.com (77.243.185.0)  29.972 ms  30.308 ms  28.651 ms
13  xe-2-2-2-0.core1.man4.uk.m247.com (83.97.21.71)  3.728 ms xe-2-3-0-0.core1.man4.uk.m247.com (83.97.21.150)  3.667 ms xe-1-0-3-0.core1.man4.uk.m247.com (77.243.176.46)  3.090 ms
14  te-9-3-0.bb1.lon1.uk.m247.com (212.103.51.17)  8.133 ms te-9-6-0.bb1.lon1.uk.m247.com (212.103.51.19)  9.081 ms te-9-8-0.bb1.lon1.uk.m247.com (77.243.176.247)  8.704 ms
15  google1.lonap.net (5.57.80.136)  8.735 ms  8.597 ms  9.454 ms
16  74.125.242.97 (74.125.242.97)  11.616 ms 74.125.242.65 (74.125.242.65)  10.939 ms  10.902 ms
17  172.253.66.101 (172.253.66.101)  10.034 ms 172.253.66.99 (172.253.66.99)  10.873 ms 172.253.66.101 (172.253.66.101)  10.751 ms
18  lhr48s09-in-f14.1e100.net (172.217.169.78)  9.355 ms  9.113 ms  9.563 ms
```

### Output Meaning
Below is a table showing the meaning of the different columns of the `traceroute` commands output.
The data in the table is taken from the first 3 hops of the example above.

| Hop Number | Name & IP Address | RTT1 | RTT2 | RTT3 |
|------------|-------------------|------|------|------|
| 1 | 192.168.0.254 (192.168.0.254) | 3.141 ms | 3.123 ms | 3.129 ms |
| 2 | 172.16.25.2 (172.16.25.2) | 3.753 ms | 3.750 ms | 3.738 ms |
| 3 | no-reverse-dns.metronet-uk.com (164.39.75.105) | 6.859 ms | 6.861 ms | 6.857 ms |

#### Hop Number
This is the first column and is simply the number of the hop along the route. In this case, it is the first hop.

#### Name & IP Address
This column has the IP address of the router. If it is available, the domain name will also be listed.

#### RTT Columns
The three `RTT` columns display the round trip time (RTT) for your packet to reach that point and return to your computer.
This is listed in milliseconds.
There are three columns because the traceroute sends three separate signal packets.
This is to display consistency, or a lack thereof, in the route.

## Tasks

### Installation
Traceroute is a tool that is typically used on Linux systems.
Windows uses a very similar tool, called `tracert`, that comes pre-installed.

#### Ubuntu/Debian
```bash
sudo apt install -y traceroute
```

#### CentOS/RHEL
```bash
sudo yum install -y traceroute
```

### Try it Out
Lets see what hops are made just by making a request to `google.com`:
```bash
traceroute google.com
```
You should see an output similar to this:
```text
traceroute to google.com (172.217.169.78), 30 hops max, 60 byte packets
 1  192.168.0.254 (192.168.0.254)  3.141 ms  3.123 ms  3.129 ms
 2  172.16.25.2 (172.16.25.2)  3.753 ms  3.750 ms  3.738 ms
 3  no-reverse-dns.metronet-uk.com (164.39.75.105)  6.859 ms  6.861 ms  6.857 ms
 4  no-reverse-dns.metronet-uk.com (164.39.85.25)  6.830 ms  6.816 ms  6.863 ms
 5  no-reverse-dns.metronet-uk.com (85.199.237.157)  6.867 ms  6.864 ms  6.876 ms
 6  no-reverse-dns.metronet-uk.com (51.179.187.200)  6.801 ms  5.118 ms  4.975 ms
 7  no-reverse-dns.metronet-uk.com (85.199.224.241)  4.932 ms * *
 8  te1-5.man-tck1gw.metronet-uk.com (85.199.239.165)  3.002 ms  3.098 ms  3.080 ms
 9  te1-4.man-tcw1gw.metronet-uk.com (77.75.191.34)  11.700 ms  11.861 ms  11.847 ms
10  te0-0-0-0.man-tcw2br.metronet-uk.com (164.39.85.50)  3.472 ms  3.451 ms  3.421 ms
11  po-5-11.bb1.man2.uk.m247.com (148.252.210.96)  44.219 ms  44.156 ms  43.243 ms
12  te-9-2-0.core-dc2.man4.uk.m247.com (77.243.185.0)  29.972 ms  30.308 ms  28.651 ms
13  xe-2-2-2-0.core1.man4.uk.m247.com (83.97.21.71)  3.728 ms xe-2-3-0-0.core1.man4.uk.m247.com (83.97.21.150)  3.667 ms xe-1-0-3-0.core1.man4.uk.m247.com (77.243.176.46)  3.090 ms
14  te-9-3-0.bb1.lon1.uk.m247.com (212.103.51.17)  8.133 ms te-9-6-0.bb1.lon1.uk.m247.com (212.103.51.19)  9.081 ms te-9-8-0.bb1.lon1.uk.m247.com (77.243.176.247)  8.704 ms
15  google1.lonap.net (5.57.80.136)  8.735 ms  8.597 ms  9.454 ms
16  74.125.242.97 (74.125.242.97)  11.616 ms 74.125.242.65 (74.125.242.65)  10.939 ms  10.902 ms
17  172.253.66.101 (172.253.66.101)  10.034 ms 172.253.66.99 (172.253.66.99)  10.873 ms 172.253.66.101 (172.253.66.101)  10.751 ms
18  lhr48s09-in-f14.1e100.net (172.217.169.78)  9.355 ms  9.113 ms  9.563 ms
```
