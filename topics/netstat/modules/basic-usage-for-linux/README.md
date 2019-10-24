# Basic Usage for Linux



<!--TOC_START-->
## Contents
- [Overview](#overview)
- [Options on Linux](#options-on-linux)
- [Tasks](#tasks)
	- [Install NGINX for Your Operating System](#install-nginx-for-your-operating-system)
		- [Ubuntu/Debian](#ubuntudebian)
		- [CentOS/RHEL](#centosrhel)
	- [Identify the Process ID of the Application Using a Port Number](#identify-the-process-id-of-the-application-using-a-port-number)
	- [Clean Up](#clean-up)

<!--TOC_END-->
## Overview
The netstat tool is very important for Linux network administrators, as well as system administrators, to monitor and troubleshoot their network related problems and determine network traffic performance.

## Options on Linux
|Short and Long Options|Description|
|----------|--------------|
|-a, --all|Displays all active connections and the TCP and UDP ports on which the computer is listening|
|-c, --continuous|Continuous listening|
|-h, --help|Show the available options that can be used|
|-l, --listening|Display listening server socket|
|-n, --numeric|Displays active TCP connections, however, addresses and port numbers are expressed numerically and no attempt is made to determine names|
|-p, --programs|Display PID/Program name for sockets; this is great for finding what applications are taking up the ports you are trying to use |
|-t, --tcp|Filter TCP Sockets|
|-u, --udp|Filter UDP Sockets|
|-v, --verbose|Show more information and statistics|
|-V, --version|Display the version of netstat that's installed|

## Tasks
Here, we'll look at how we can find a process using a certain port on a machine.
It's a common issue where you have an application running (such as a webserver) and you are unable to redeploy that application because the old version of it is still running; this means that the port is in use.
An efficient way to resolve this is to find the process ID by the port that it's listening on.
For instance, if we knew that the application was listening on port 80, that means we can use a tool like netstat to identify that application's PID by the port that it is listening on.

To start, we need to install an application to do this - NGINX is a simple reverse proxy and webserver that can serve that purpose well.

### Install NGINX for Your Operating System

#### Ubuntu/Debian
```bash
sudo apt update
sudo apt install -y nginx
```

#### CentOS/RHEL
```bash
sudo yum install -y nginx
```

### Identify the Process ID of the Application Using a Port Number
NGINX runs on port `80`.
Firstly, we need to get an output from netstat containing the applications PID:
```bash
netstat -tulpn
```
You might notice that, under the PID column, there aren't any values (only `-` is listed):
```text
(No info could be read for "-p": geteuid()=1001 but you should be root.)
Active Internet connections (only servers)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name
tcp        0      0 0.0.0.0:80              0.0.0.0:*               LISTEN      -
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      -
tcp6       0      0 :::80                   :::*                    LISTEN      -
tcp6       0      0 :::22                   :::*                    LISTEN      -
udp        0      0 0.0.0.0:68              0.0.0.0:*                           -
udp        0      0 10.154.0.34:123         0.0.0.0:*                           -
udp        0      0 127.0.0.1:123           0.0.0.0:*                           -
udp        0      0 0.0.0.0:123             0.0.0.0:*                           -
udp6       0      0 fe80::4001:aff:fe9a:123 :::*                                -
udp6       0      0 ::1:123                 :::*                                -
udp6       0      0 :::123                  :::*                                -
```
This is because the processes are executed by another user, meaning you don't have access to that information.
To get around this, we can use `sudo`:
```bash
sudo netstat -tulpn
```
Now we should see a list of PIDs:
```text
Active Internet connections (only servers)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name    
tcp        0      0 0.0.0.0:80              0.0.0.0:*               LISTEN      1665/nginx: master  
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      686/sshd            
tcp6       0      0 :::80                   :::*                    LISTEN      1665/nginx: master  
tcp6       0      0 :::22                   :::*                    LISTEN      686/sshd            
udp        0      0 0.0.0.0:68              0.0.0.0:*                           583/dhclient        
udp        0      0 10.154.0.34:123         0.0.0.0:*                           644/ntpd            
udp        0      0 127.0.0.1:123           0.0.0.0:*                           644/ntpd            
udp        0      0 0.0.0.0:123             0.0.0.0:*                           644/ntpd            
udp6       0      0 fe80::4001:aff:fe9a:123 :::*                                644/ntpd            
udp6       0      0 ::1:123                 :::*                                644/ntpd            
udp6       0      0 :::123                  :::*                                644/ntpd 
````
You will now be able to use the PID of NGINX (1665 in this case) to manage that process (most likely to kill it):
```bash
sudo kill 1665
```

### Clean Up
Lets stop and remove NGINX to cleanup:
```bash
sudo systemctl stop nginx
sudo apt purge -y nginx
```
