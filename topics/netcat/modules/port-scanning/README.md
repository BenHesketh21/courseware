<!--PROPS
{
    "estTime": 10,
    "questions": [
        {
            "value": "What can port scanning be used for?",
            "answer": "Finding out what ports are available on a host.",
            "choices": [
                "Load testing.",
                "Monitoring TCP traffic going through the given ports."
            ]
        }
    ]
}
-->

# Port Scanning with netcat



<!--TOC_START-->
## Contents
- [Overview](#overview)
- [Usage](#usage)
- [Tasks](#tasks)
	- [Run a Basic Scan](#run-a-basic-scan)
	- [Run a Scan Again After Installing an Application](#run-a-scan-again-after-installing-an-application)
		- [Installing on Ubuntu/Debian](#installing-on-ubuntudebian)
		- [Installing on CentOS/RHEL](#installing-on-centosrhel)
		- [Run the Scan Again](#run-the-scan-again)
	- [Cleanup](#cleanup)
		- [Removing on Ubuntu/Debian](#removing-on-ubuntudebian)
		- [Removing on CentOS/RHEL](#removing-on-centosrhel)

<!--TOC_END-->
## Overview
Port scanning is a technique used for finding out which ports have an application running on them, making them accessible.
This can be used to verify security polices that are in place, which define what ports are accessible on a host machine.
A preferred tool for port scanning is `nmap`; however, if this is not available to you, you can still use `netcat`.

## Usage
You can use the following command to run a simple port scan:
```bash
# nc -zv [HOST] [PORT_RANGE]
nc -zv 127.0.0.1 1-1000
```
This example scans the `127.0.0.1` host (the local machine) over ports 1 to 1000.
The `z` option is used here for running netcat in a scanning mode; this means that while it's testing all the ports, it won't attempt to download anything.
The `v` option is used for verbose mode, which indicates, more clearly, whether netcat was able to find an accessible port.

## Tasks

### Run a Basic Scan
On a Linux machine with netcat, run a scan to find the accesible ports:
```bash
nc -zv 127.0.0.1 1-1000
```
You should see that most of the ports are not accessable, because there are no applications listening on them:
```text
bob@port-scanning-with-netcat:~$ nc -zv 127.0.0.1 1-1000
localhost [127.0.0.1] 22 (ssh) open
```

### Run a Scan Again After Installing an Application
Now try installing an application, such as NGINX, so that port `80` shows up in the scan:

#### Installing on Ubuntu/Debian
```bash
sudo apt install -y nginx
```

#### Installing on CentOS/RHEL
```bash
sudo yum install -y nginx
```

#### Run the Scan Again
Try running the scan again:
```bash
nc -zv 127.0.0.1 1-1000
```
You should now see port `80` pop up in the scan:
```text
bob@port-scanning-with-netcat:~$ nc -zv 127.0.0.1 1-1000
localhost [127.0.0.1] 22 (ssh) open
localhost [127.0.0.1] 80 (http) open
```

### Cleanup
Remove NGINX to cleanup:

#### Removing on Ubuntu/Debian
```bash
sudo systemctl stop nginx
sudo apt purge -y nginx
```

#### Removing on CentOS/RHEL
```bash
sudo systemctl stop nginx
sudo yum remove -y nginx
```
