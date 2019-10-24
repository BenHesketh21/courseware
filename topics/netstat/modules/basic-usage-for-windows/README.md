<!--PROPS
{
    "estTime": 15,
    "software": [
        {
            "name": "nginx",
            "version": "1.16.1",
            "platform": "windows"
        }
    ]
}
-->

# Basic Usage for Windows



<!--TOC_START-->
## Contents
- [Overview](#overview)
- [Options on Windows](#options-on-windows)
- [Tasks](#tasks)
	- [Install NGINX on Windows](#install-nginx-on-windows)
	- [Identify the Application Using a Port Number](#identify-the-application-using-a-port-number)
	- [Stop the Application](#stop-the-application)
		- [Using the Process Name](#using-the-process-name)
		- [Using the Process ID (PID)](#using-the-process-id-pid)

<!--TOC_END-->
## Overview
Netstat on Windows displays active TCP connections, ports on which the computer is listening, Ethernet statistics, the IP routing table, IPv4 statistics (for the IP, ICMP, TCP, and UDP protocols), and IPv6 statistics (for the IPv6, ICMPv6, TCP over IPv6, and UDP over IPv6 protocols).

## Options on Windows
Used without parameters, `netstat` displays active TCP connections.
Typically on Windows CLI tools options when running commands are prefixed with `/`.
For instance, to use the `a` option you would put `/a`.
This is not the case with netstat, where you can use `-`.
An example of using the `a` option would be `-a`.
Here are some of the other available options to use with netstat on Windows:

| Option | Description |
|--------|-------------|
| `-a`      | Displays all active TCP connections and the TCP and UDP ports on which the computer is listening |
| `-b`      | Displays the executable involved in creating each connection or listening port |
| `-e`      | Displays Ethernet statistics, such as the number of bytes and packets sent and received. This parameter can be combined with `-s.` |
| `-h`      | Show available options |
| `-n`      | Displays active TCP connections, however, addresses and port numbers are expressed numerically and no attempt is made to determine names. |
| `-o`      | Displays active TCP connections and includes the process ID (PID) for each connection. You can find the application based on the PID on the Processes tab in Windows Task Manager. This parameter can be combined with `-a`, `-n`, and `-p`. |
| `-p` | Shows connections for the protocol specified by Protocol. In this case, the Protocol can be tcp, udp, tcpv6, or udpv6. If this parameter is used with `-s` to display statistics by protocol, Protocol can be tcp, udp, icmp, ip, tcpv6, udpv6, icmpv6, or ipv6. |
| `-s` | Displays statistics by protocol. By default, statistics are shown for the TCP, UDP, ICMP, and IP protocols. If the IPv6 protocol is installed, statistics are shown for the TCP over IPv6, UDP over IPv6, ICMPv6, and IPv6 protocols. The -p parameter can be used to specify a set of protocols. |
| `-r` | Displays the contents of the IP routing table. This is equivalent to the `route print` command. |

## Tasks
Here, we'll look at how we can find a process using a certain port on a machine.
It's a common issue where you have an application running (such as a web server) and you are unable to redeploy that application because the old version of it is still running; this means that the port is in use.
An efficient way to resolve this is to find the process name by the port that it's listening on.
For instance, if we knew that the application was listening on port `80`, that means we can use a tool like netstat to identify that application's name by the port that it is listening on.

To start, we need to install an application to do this - NGINX is a simple reverse proxy and web server that can serve that purpose well.

### Install NGINX on Windows
- Download NGINX `1.16.1` from [here](http://nginx.org/download/nginx-1.16.1.zip) 
- Extract the `nginx-1.16.1.zip` file
- Execute `nginx-1.16.1/nginx.exe` - All you have to do is double click the file; don't expect anything to pop up as it runs in the background
- Check that NGINX is working by navigating to http://localhost in your browser

### Identify the Application Using a Port Number
NGINX runs on port `80`.
Firstly, we need to get an output from netstat containing the applications name.
In the examples below the following options are used:
- `a`; We are using this to show TCP and UDP ports which the computer is listening on
- `n`; This is being used because we don't need to resolve host names, so this will mean that the command runs faster
- `b`; One of the most important things we need is the process name; the `b` option will show us this
- `o`; Another way of managing the process is by using the process ID (PID)
- `-p TCP`; We saying that we only want to see TCP sockets here to save us looking through too much output
```powershell
netstat -anbo -p TCP
```
This should give you an output which contains the following:
```text
Active Connections

  Proto  Local Address          Foreign Address        State           PID
  TCP    0.0.0.0:80             0.0.0.0:0              LISTENING       4436
 [nginx.exe]
```
We can see from this output that there is an application (`nginx.exe`) using port `80` on the machine and it has a PID number of `4436`.

### Stop the Application
Below are two methods of killing the NGINX process; try identifying and killing the nginx process with both.
Remember to start NGINX again after killing the process the first time.

#### Using the Process Name
Now we know the application name, we can use that to kill the application and gain access back to that port.
```powershell
taskkill /IM nginx.exe /F
```

#### Using the Process ID (PID)
To kill a process using its PID we can use the following; replacing `[PID]` with the PID number:
```powershell
taskkill /F /PID [PID]
```
