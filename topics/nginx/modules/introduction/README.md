# Introduction



<!--TOC_START-->
## Contents
- [Overview](#overview)
- [Installation](#installation)
	- [Linux](#linux)
		- [CentOS/RHEL](#centosrhel)
		- [Debian/Ubuntu](#debianubuntu)
	- [Windows](#windows)
	- [Docker](#docker)
- [Tasks](#tasks)
	- [Install NGINX](#install-nginx)

<!--TOC_END-->
## Overview
Nginx is a web server which can also be used as a reverse proxy, load balancer, mail proxy and HTTP cache.
The goal behind NGINX was to create a fast web server for handling a large amount of concurrent connections.
NGINX has a few common use cases:
- Static files: NGINX can serve static files, such as HTML, CSS and JavaScript.
- Act as a reverse proxy: handle and process all requests before sending them to another application server.
- Be used as a load balancer: requests can be distrubed over multiple instances of your application to allow for high availability should one of you application servers fail.

## Installation

### Linux
On Linux systems, NGINX can usually be installed using the relevant package manager:

#### CentOS/RHEL
```bash
sudo yum install -y nginx
```

#### Debian/Ubuntu
```bash
sudo apt install -y nginx
```

### Windows
An installer for NGINX can be downloaded from the [NGINX downloads page](http://nginx.org/en/download.html).
- Download the latest, stable version of NGINX
- Unzip the downloaded file
- Run the `nginx.exe` executable - don't worry if it seems like nothing happens, NGINX will run in the background.

### Docker
If you have Docker configured then you can get NGINX running using the `nginx` image:
```bash
docker run -d --rm -p 80:80 --name nginx nginx
```

Once you have installed NGINX for your relevant Operating System, you can navigate to `http://localhost` in your web browser to see if NGINX is running. If you are on Linux and don't have a GUI, then you can run `curl http://localhost` to see if you can get a response from the NGINX service.

Once you have put `http://localhost` in your web browser you should see a page like the following:
![NGINX Default Page](https://lh3.googleusercontent.com/G4w7DJI6YST8allYA8rBpnrySbB0N4sundqXZQbux85RgFtHC08kb6-MsvHgO2dICdlecfvU5D1UEim1LGTNwZFRJLASopmASoGeCV2lnICpJz84jI_XU-Y-TjBs4u-m8lP8wYe-ziKv0ZR3K4UZ_j0tVMcfrdckNo7lL_OGyUa9wE2ZgZecS9otx7zVNusXgYphtI2PGzA6F0d6QJEDIE5wrbsZzFHSmtNLwzDkY3ILGaJTEGfkfCT7QHT82-d3ck_6nnO_IHfCGw80yAyBznUHa7RBEv_h5i1Nq8ePQLd9rwcKV7-LZyHcQJG1P4CSy3sZYtcsOaSzlr67QMIZMj_OnfaULmcLnZICk5JXGzRYqvjuG8SPMRYjdzGR3n6fBAL_G6s6lFuROuT4EtaMoiJN0YkibJw_RjPKkKbUjJYvon8G9KzvSlonY8mvm0Cdt_UQu9B1jKy-2A0CgTxDmp56mfKo4yEDlwl4l2oejvIdQ-w26RacR1C625xc3ffEGsUf9fppfwQgKkWVps_Nd5z86xmCm4kZysluOYHohTihokpiMU6YN6L2oHhyHj8xbC0MRywEbL-sUmtBTv6rOZF770c3NeO0RGu5axeAsho0t_1ANO0gdk35oMlYfG38ikreb9_il6UHXK8v5SWsQur5foFgFskX_Ti-3uC2fS-5V56lqzBRlNDPZ08VZlrEpN3XHu-pVgTaH3OXrU6RiYWPT6vNtDy5nvf1dgUQko97-TH6=w748-h295-no)

If you used the `curl` command on a terminal then you should see the HTML response:
```text
bob@work-laptop:~/projects/github.com/bob-crutchley/notes$ curl http://localhost
<!DOCTYPE html>
<html>
<head>
<title>Welcome to nginx!</title>
<style>
    body {
        width: 35em;
        margin: 0 auto;
        font-family: Tahoma, Verdana, Arial, sans-serif;
    }
</style>
</head>
<body>
<h1>Welcome to nginx!</h1>
<p>If you see this page, the nginx web server is successfully installed and
working. Further configuration is required.</p>

<p>For online documentation and support please refer to
<a href="http://nginx.org/">nginx.org</a>.<br/>
Commercial support is available at
<a href="http://nginx.com/">nginx.com</a>.</p>

<p><em>Thank you for using nginx.</em></p>
</body>
</html
```

## Tasks

### Install NGINX
Install NGINX for your current Operating System.
