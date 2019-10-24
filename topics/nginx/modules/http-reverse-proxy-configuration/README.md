# HTTP Reverse Proxy Configuration



<!--TOC_START-->
## Contents
- [Overview](#overview)
- [Reasons for Using a Reverse Proxy](#reasons-for-using-a-reverse-proxy)
	- [Load Balancing & Global Server Load Balancing](#load-balancing--global-server-load-balancing)
	- [Protection from Attacks](#protection-from-attacks)
	- [Caching](#caching)
	- [TLS/SSL Encryption](#tlsssl-encryption)
	- [Visual Representation](#visual-representation)
- [Configuration](#configuration)
	- [Basic](#basic)
	- [Multi-Tier Applications](#multitier-applications)
- [Tasks](#tasks)
	- [Prerequisites](#prerequisites)
	- [Configure the `api` Virtual Machine](#configure-the-api-virtual-machine)
		- [Make Sure Git is Installed](#make-sure-git-is-installed)
		- [Download and Install the `api` Application](#download-and-install-the-api-application)
	- [Configure the `web-app` Virtual Machine](#configure-the-webapp-virtual-machine)
		- [Make Sure Git is Installed](#make-sure-git-is-installed-1)
		- [Download and Install the `web-app` Application](#download-and-install-the-webapp-application)
	- [Configure the `nginx` Virtual Machine](#configure-the-nginx-virtual-machine)
		- [Install Git](#install-git)
		- [Configure NGINX](#configure-nginx)
	- [View the Web Application](#view-the-web-application)
	- [Get the Current Date](#get-the-current-date)
	- [Clean Up](#clean-up)

<!--TOC_END-->
## Overview
An NGINX reverse proxy server sits in front of web servers and forwards client requests (e.g. web browsers) to those web servers.
Reverse proxies are typically implemented to help increase security, performance, and reliability.

## Reasons for Using a Reverse Proxy
There are several reasons for configuring your web applications to be behind a reverse proxy.

### Load Balancing & Global Server Load Balancing
Reverse proxies can be used as load balancing solution for popular websites that cannot handle all of the incoming traffic on a single server.
This can also be introduced on a global scale for directing customers to your services which are located closer to them geographically.
Clients would connect to the NGINX server, then NGINX would distribute the traffic evenly over the application servers behind it.

### Protection from Attacks
By using a reverse proxy, information about the applications behind it are not revealed, making it harder for attackers to establish unwelcome connections to your applications.

### Caching
Caching can be used to save on time and network traffic.
Resources and information received from remote locations by the reverse proxy can be cached so that it doesn't have to make another request for them if another client asks for the same thing such as a public image or icon.

### TLS/SSL Encryption
Encrypting traffic is now almost just expected when you visit a website however, encrypting and decrypting all requests can be expensive computationally.
A reverse proxy can be used to encrypt and decrypt communications before passing it on to your web applications which can be configured in a private subnet, only accessible by the reverse proxy.
This would save your web application servers from having to handle any encryption and would still be a solution secure enough for many scenarios.
You can of course implement TLS internally behind the reverse proxy to adhere to any mandatory compliances or requirements.

### Visual Representation
Consider the following diagram and points for the service hosted on `example.com`:
- More than one instance of the web application can be hosted behind the NGINX reverse proxy.
- NGINX will balance HTTP traffic between the two istances of the web application evenly.
- If the web server wants to make requests to an API or backend service, this can be done using NGINX as well. All requests starting with `/api` can be sent to the API servers instead of the web application, you will get a chance to implement and understand this in the Tasks section.

![NGINX Reverse Proxy](https://lh3.googleusercontent.com/dzet9BkO4Vy3BQn61CKpu7KMAeBPngZPZFdPGWLwk8pOlyIp4KgR4lFr6OiwSQDq_XZ_GlBvX0FsQIWMF_v7bxXpdonWNNK7oDBHqDOzczo_HWuPuHI7uOdtofYV2K5vzBb3wD3epF5JjFl_mxDEjwYKb1hn5a69bc6ZdT-wnsvmbbG2F2944LngaAeec6a2QSbVBg4cWHw3FkzYhaFaumBa86ZljYsIOn2d0h4yPtNjGkwM1LXgC8n4DqM-gXO_Nu-bbJHkX-GG1iUCNXZgbNpTS5RoPCsN9YTOyJ9w15CRYTap3RX6c0o5nFxArcqGIdCWEoLvQlNK72ENRh17sgOxtzg2WCXi4eSovnDJ3WW-Zm35ci3IgZ4arWZqU8dGI5zDE67YPOz_hxwWo_eLR0CXTjk2hZDFhgFTf-WX8CHrgtbjetFFQdZ3dxOs6-33DDBEoPxyAAKA4iYdj5LlH6taiRoU2rbbN3xGIq5wFAdgpT7l8IIvLaogY6dTVXQCk3ijos5nvZD4Ar1TvN10agbqZKi4W629h7K3c2q7Jz1rktKd9PGjxEaWFnRBU047lr4E7A4dGAmPTTQWvMpZm5ej27cV3bxDqC_iW01u-UfAUdEZ5HAMDAflorYBy1NMOAkcZBrC-L6wZ3YxdukFwJ0Q9q4FxLxmtS4aFPgYdPhaZUdXGamUy9pk6mbVyBTr_jasuNIWxaq4SG7O3cuptlzIXVhO3Yf2AIw2fHPaj5LMbAvs=w1168-h669-no)

## Configuration

### Basic
A simple NGINX reverse proxy can be configured by using a `proxy_pass` directive for a `location` context inside a HTTP virtual server.
This example will proxy HTTP requests to the `web-app` host on port `80`:
```text
events {}
http {
    server {
        listen 80;
        location / {
            proxy_pass http://web-app;
        }
    }
}
```

### Multi-Tier Applications
Applications are often developed in multiple tiers; front-end, back-end and database for example.
NGINX can be used as reverse proxy, giving access to different tiers of the application depending on what URL is used.
Here is an example for a reverse proxy configuration that serves the `web-app` by default, but when `/api` is accessed, HTTP requests are sent to the `api` server:
```text
events {}
http {
    server {
        listen 80;
        location / {
            proxy_pass http://web-app;
        }
        location /api {
            proxy_pass http://api;
        }
    }
}
```

## Tasks
This guide will walk you through deploying an application behind an NGINX reverse proxy that has a front end and backend service.

### Prerequisites
- 3 Ubuntu or Debian virtual machines on the same network/subnet with the host names as follows:
    - `nginx`
    - `web-app`
    - `api`

    On cloud providers like AWS, Azure and GCP this is usually done by just naming the virtual machines as shown above when you are creating them.
- The `nginx` virtual machine will need a public IP address and have port `80` accessible for incoming traffic over the internet.

### Configure the `api` Virtual Machine
The API is going to return a date and time when a GET request is made to `/api/date`.
Connect to the `api` virtual machine and use the commands shown in this section to install the API server.

#### Make Sure Git is Installed
We are going to use Git to download the application files that are on store in this module folder, for that we will of course need Git installed.
```bash
sudo apt update
sudo apt install -y git
```

#### Download and Install the `api` Application
The `api` application can now be installed by cloning this repository with Git, changing to the `api` directory and running the `setup.bash` script:
```bash
git clone https://github.com/bob-crutchley/notes
cd notes/topics/nginx/modules/http-reverse-proxy-configuration/application/api
./setup.bash
```

### Configure the `web-app` Virtual Machine
The web application is very simple; it uses basic JavaScript for connecting to the API server.
Connect to the `web-app` virtual machine and install the application using the commands shown in this secion.

#### Make Sure Git is Installed
Git will need to be installe on this virutal machine as well, run a  command to make sure the APT repositories are up to date and install git:
```bash
sudo apt update
sudo apt install -y git
```

#### Download and Install the `web-app` Application
We can now go ahead and install the `web-app` application by cloning this repository, changing to the `web-app` directory and running the `setup.bash` script.
```bash
git clone https://github.com/bob-crutchley/notes
cd notes/topics/nginx/modules/http-reverse-proxy-configuration/application/web-app
./setup.bash
```

### Configure the `nginx` Virtual Machine
NGINX is going to be the component that ties together the Web application and API server.
All HTTP requests are going to go through NGINX first but then sent to the correct service depending on what URL was requested.

You will see that there is a button on the Web application which makes a HTTP GET request to `/api/date` and then displays that information on the page.
Because the URL starts with `/api`, our NGINX configuration is going to proxy the request to the `api` server and get the response from that service.

This is the configuration that is going to be installed into NGINX for you:
```text
events {}
http {
    server {
        listen 80;
        location / {
            proxy_pass http://web-app;
        }
        location /api {
            proxy_pass http://api:3000;
        }
    }
}
```
To get the NGINX server setup, connect to your `nginx` virtual machine and run the commands shown below.

#### Install Git
We are going to get the NGINX configurations onto the `nginx` virtual machine by using Git as well.
Update the APT repository and install Git with these commands:
```bash
sudo apt update
sudo apt install -y git
```

#### Configure NGINX
NGINX can now be configured by downloading he configurations with Git, changing to the `nginx` directory and running the `setup.bash` script:
```bash
git clone https://github.com/bob-crutchley/notes
cd notes/topics/nginx/modules/http-reverse-proxy-configuration/application/nginx
./setup.bash
```

### View the Web Application
Now that everything is setup we can make sure that the application is working.
Navigate to the public IP address of you `nginx` virtual machine in your web browser, you should then see something like the image below.

Please note that your public IP address will almost certainly be different to the one shown in the screenshots.

![NGINX Web Application](https://lh3.googleusercontent.com/8KgJlGCqQ2rA9lvVBJzzD5G4vcMRTD6USiKEpmpWfx-0qxIcqjbzlqGX8BcybufPtvH69ZI5CDs7D2i57wubM8cvmZvHKJ0mz3KkwMCKN-0L1qnkeEKQoz5XDQyiy_ncvb7tKgLpRV5xkSfy-d2UQ5Ab-w69pULRzjvcaFoKkvOaa9DCU1C78NN-nTulKGDbkcmxJo6R0AngL_J0tM9esVov1aJ0WMeDB-P8O_2lwp7ixMLlvF-ZdxnrMcad0WbVBN4XFUQt089yFVUk3qgXkTkGu9WruTRZd3CM3Aw4AOVmUjavPU3Ioxpp8TqIBH5K9Lg99ovV_BJ7014jS94cDQlfyWzA0y1vWZS-0482TXswdf3dSjLZip0ecAv42AgkcMnxo98QH1vulQMUz5itW_N1icHWwFz2xdI51eC4vz5aPUg_tboCMgVdJoAROFR5t3Nh1CAE9zyelQEQU4ONvfoshAJwl6eSB2Esk70A3MSQAL1rghNZcluApMI1edFUMpGl_C_EZxpfsHapNQTMLH-p-ojQi4mlrJl3zlGcOERCAYmO9So7sVqmeD1ZGhVlh6QJelDthujDOCr4t3-noMafqD73x0aso39GhdC8a-Ba_DjkrBIWaOWB4yaWs2Nmppkj-ThbylzpBZ9JfnCs2gtVc8Lu28P9GGhIPAQBbYYBbB-qgHxykc7mNcwHsmdBAKgFvl_NersOouoFgr7WFadP7GpxJJ9EJGWIYlfzbirpgXFu=w1026-h357-no) 

### Get the Current Date
Click the button on the web page to get the current date, it should then be displayed on the webpage:

![NGINX Web Application Button Click](https://lh3.googleusercontent.com/S5I_ONtk_ufb1rTmlL4cRBngAZ9mtJo3DWdEKzEKF0ADP9InvYEA6jUMCqlB224JUBjxLvfa7Jv5rYa_nNY_hYmnsQRGiUlqmbhgTDshtvk1IYz4Zkmmn1r5jOImmzZrMUSvcN8fbcT_IMlbbPFBYTq9bMecHJ4tlsdqWvl0Y98Y5mkdrStsO_SoDPAJsFKtsLbU6jdNcLlw_5GVglIOPE50vFR1batgymfbpatTCwCsObTtgYYSow5G_JaAWPxbau44iXAt65rA4L76zQe4yDhJIyPE6gwIrqN_sz61fJqTQQToMV9tl8Kxy9Lyz91YewvwYfee63-rqcRvISdFcXoxMZqAozuSRCdvQYxztSXxii_CjhpdlI8VikUeVsDtJI0dcwKgY2wIQTnb0BHuirLQhcsPyQz5P-R-SosRaGDxYYWsfIgjKmuMRplQ99BQ7-KsAY8Ar5i96pDARNbCbqAYYP41OszfVQYnk6V2GPl7HlhwX8O1bWkRP69jGUjefUcCTWy1znMwRuUZm0OUzhLztjxufrjIOH13ZIPKTORyJkk1yBoe629etMUwN2VJhwNlOunkqgCzooJaw-TzoT1b3AmtsvX74wIVuI_kHH_QacXMUbZEu1MEWyw0WX7XDSy6mii-37qsYExgvpuWo1jO7-RA2bDxY84N0TimjgSiBZBOTSwGdbRiZRACp96aPh6rjwus6D1tusW1A6Yitbd_xsMrs3AMbt0IOUCXN7ChTUnq=w1024-h349-no) 

### Clean Up
You can now finish this task by deleting any virtual machines, virtual networks, subnets and firewall rules that you created while working on this task.
