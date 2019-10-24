# netcat
<!--TOC_START-->
## Contents
- [Overview](#overview)
- [Versions](#versions)
- [Installation](#installation)
	- [Dependencies](#dependencies)
		- [Ubuntu/Debian](#ubuntudebian)
		- [CentOS/RHEL](#centosrhel)
	- [Download & Install](#download--install)
- [Modules](#modules)

<!--TOC_END-->
## Overview
netcat (often abbreviated to nc) is a computer networking utility for reading from and writing to network connections using TCP or UDP.
This tool is a feature-rich network debugging and investigation tool, since it can produce almost any kind of connection its user could need and has a number of built-in capabilities.
Its list of features includes port scanning, transferring files, and port listening, and it can be used as a backdoor.
## Versions
There are a few different version of netcat, they are all similar but some of the features differ depending on the version.
For most part though, you shouldn't need to worry about which of these versions are installed; it only really matters if require a specific feature.
- GNU Netcat; GNU rewrite of netcat, the network piping application.
- openbsd-netcat; TCP/IP swiss army knife. OpenBSD variant.
- libressl-netcat; Low level UDP/TCP connection tool with support for TLS protocol.
## Installation
### Dependencies
To keep the installation here consistent across Linux distributions; this guide will show you how to install the GNU netcat by building it from the source code.
The only thing that differs is how the dependencies for building it are installed beforehand:
#### Ubuntu/Debian
```bash
sudo apt install -y make gcc
```
#### CentOS/RHEL
```bash
sudo yum install -y make gcc
```
### Download & Install
```bash
NC_VERSION="0.7.1"
# download netcat source code
curl https://netcologne.dl.sourceforge.net/project/netcat/netcat/${NC_VERSION}/netcat-${NC_VERSION}.tar.gz -o netcat-${NC_VERSION}.tar.gz
# extract source code from tar.gz
tar -xzvf netcat-${NC_VERSION}.tar.gz
# build and install netcat
cd netcat-${NC_VERSION}
./configure
sudo make install
```
We can now confirm if netcat is installed by checking the version:
```bash
nc --version
```
<!--MODULES_START-->
## Modules
- [Port Scanning with netcat](./modules/port-scanning)
<!--MODULES_END-->
