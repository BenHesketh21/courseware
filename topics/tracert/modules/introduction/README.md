<!--PROPS
{
    "estTime": 10
}
-->

# Introduction



<!--TOC_START-->
## Contents
- [Overview](#overview)
- [Tracert Output](#tracert-output)
	- [Example Output](#example-output)
	- [Output Meaning](#output-meaning)
		- [Hop Number](#hop-number)
		- [Name & IP Address](#name--ip-address)
		- [RTT Columns](#rtt-columns)
- [Tasks](#tasks)
	- [Try it Out](#try-it-out)

<!--TOC_END-->
## Overview
In computing, `traceroute` and `tracert` are computer network diagnostic commands for displaying the route (path) and measuring transit delays of packets across an Internet Protocol (IP) network.

Here's an example of a path for going to `google.co.uk` from a computer in London:
![Traceroute Map](https://i.imgur.com/cE9UPCB.png)

The history of the route is recorded as the round-trip times of the packets received from each successive host (remote node) in the route (path); the sum of the mean times in each hop is a measure of the total time spent to establish the connection.
Traceroute proceeds unless all (three) sent packets are lost more than twice. If this happens, the connection is lost and the route cannot be evaluated.

## Tracert Output

### Example Output
Below is an example output from a basic `tracecrt` command to `google.com`:
```text
Tracing route to google.com [172.217.20.142]
over a maximum of 30 hops:

  1    <1 ms    <1 ms    <1 ms  hyperhub.mynet [192.168.1.1]
  2    32 ms    58 ms     4 ms  100.97.100.1
  3     1 ms     1 ms     1 ms  172.16.25.18 [172.16.25.18]
  4     9 ms     1 ms     1 ms  172.17.10.102 [172.17.10.102]
  5     1 ms     1 ms     1 ms  172.17.14.0 [172.17.14.0]
  6     1 ms    <1 ms    <1 ms  172.16.17.81 [172.16.17.81]
  7    <1 ms    <1 ms    <1 ms  ae2-775.cr1-man1.ip4.gtt.net [77.67.123.169]
  8     7 ms     7 ms     7 ms  et-0-0-43.cr10-lon1.ip4.gtt.net [89.149.139.1]
  9     8 ms     7 ms     8 ms  72.14.221.145
 10     *        *        *     Request timed out.
 11     9 ms     8 ms     9 ms  216.239.57.120
 12     7 ms     7 ms     7 ms  108.170.246.176
 13     8 ms     8 ms     9 ms  64.233.175.113
 14     8 ms     8 ms     8 ms  72.14.237.52
 15     8 ms     8 ms     8 ms  74.125.242.65
 16     8 ms     8 ms     8 ms  172.253.68.23
 17     8 ms     8 ms     7 ms  muc11s10-in-f14.1e100.net [172.217.20.142]
```

### Output Meaning
Below is a table showing the meaning of the different columns of the `tracert` commands output.
The data in the table is taken from the first 3 hops of the example above.

| Hop Number | RTT1 | RTT2 | RTT3 | Name & IP Address |
|------------|------|------|------|-------------------|
| 1 | 1 ms | 1 ms | 1 ms |  hyperhub.mynet [192.168.1.1] |
| 2 | 32 ms | 58 ms | 4 ms | 100.97.100.1 |
| 3 | 1 ms  | 1 ms | 1 ms | 172.16.25.18 [172.16.25.18] |

#### Hop Number
This is the first column and is simply the number of the hop along the route. In this case, it is the first hop.

#### Name & IP Address
This column has the IP address of the router. If it is available, the domain name will also be listed.

#### RTT Columns
The three `RTT` columns display the round trip time (RTT) for your packet to reach that point and return to your computer.
This is listed in milliseconds.
There are three columns because the tracert sends three separate signal packets.
This is to display consistency, or a lack thereof, in the route.

## Tasks

### Try it Out
Lets see what hops are made just by making a request to `google.com`:
```bash
tracert google.com
```
You should see an output similar to this:
```text
Tracing route to google.com [172.217.20.142]
over a maximum of 30 hops:

  1    <1 ms    <1 ms    <1 ms  hyperhub.mynet [192.168.1.1]
  2    32 ms    58 ms     4 ms  100.97.100.1
  3     1 ms     1 ms     1 ms  172.16.25.18 [172.16.25.18]
  4     9 ms     1 ms     1 ms  172.17.10.102 [172.17.10.102]
  5     1 ms     1 ms     1 ms  172.17.14.0 [172.17.14.0]
  6     1 ms    <1 ms    <1 ms  172.16.17.81 [172.16.17.81]
  7    <1 ms    <1 ms    <1 ms  ae2-775.cr1-man1.ip4.gtt.net [77.67.123.169]
  8     7 ms     7 ms     7 ms  et-0-0-43.cr10-lon1.ip4.gtt.net [89.149.139.1]
  9     8 ms     7 ms     8 ms  72.14.221.145
 10     *        *        *     Request timed out.
 11     9 ms     8 ms     9 ms  216.239.57.120
 12     7 ms     7 ms     7 ms  108.170.246.176
 13     8 ms     8 ms     9 ms  64.233.175.113
 14     8 ms     8 ms     8 ms  72.14.237.52
 15     8 ms     8 ms     8 ms  74.125.242.65
 16     8 ms     8 ms     8 ms  172.253.68.23
 17     8 ms     8 ms     7 ms  muc11s10-in-f14.1e100.net [172.217.20.142]
```
