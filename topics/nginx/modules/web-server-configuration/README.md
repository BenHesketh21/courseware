# Web Server Configuration



<!--TOC_START-->
## Contents
- [Overview](#overview)
- [Web Servers](#web-servers)
	- [Hardware](#hardware)
	- [Software](#software)
- [Configuration](#configuration)
	- [Top-Level Contexts](#toplevel-contexts)
	- [Virtual Server](#virtual-server)
- [Tasks](#tasks)
	- [Prerequisites](#prerequisites)
	- [Install the Web Application](#install-the-web-application)
	- [Configure NGINX](#configure-nginx)
	- [Access the Web Application](#access-the-web-application)

<!--TOC_END-->
## Overview
NGINX can be configured as a web server to serve content such as HTML, CSS, JavaScript and Images.
This allows us to deploy our web applications so that they can be accessed efficiently.

## Web Servers
A web server could be referring to hardware, software, or a combination of both, although you could refer to the software counterpart as a HTTP server.

### Hardware
From a hardware perspective, a web server would be a computer that has web server software installed on it and is connected to the internet.
This computer would also have all files that are going to be served (HTML documents, CSS, images and JavaScript files).

### Software
The software will allow users to connect and access the files stored on the computer.
This will most often be a HTTP server.
HTTP servers are a type of software that can understand Universal Resource Locators (URLs), allowing applications like web browsers to download and utilise their resources for things like web applications that we use everyday.

Web servers, software and hardware combined, allow us to access content over the internet - most commonly in our web browser:
![Web Server](https://lh3.googleusercontent.com/jjIKwaFUdtPFK4785VQbd67_F0g_t3Q2FoAwWp6A7-jBwIel3r8nlRh5sWVzIu50TVIVJCcC6AkQDC5_KH2RrbQbEGDnhEcF8-Ebs_bZX_eadZS_40GrXdgN5WqhEhvM07H8wGuVU1UpcJ9tHmwYrIiLFlhGdZLl8H1gLnf8KA_FJVz_EE4quNo-jnU3a-fCTI5pgh6BocULmrQBqbxkDLVKN0cpUlACuPqrUf9i0zcWus8SCat3fHrX8TV1lwrYkKQ4rIT0hh-MyhSNL94NC8iXr_x1XQoOCZD422eQBIMVXtMkY_QbkkKf8VqHNLm5QA1L8-u1XjIGoUmVmINQm1w73EZARbgcHX2BQ02WCS83COehpZybXSp3mdRp3V59-qeuygR2uhpkhJnCyhTk5iWW4AEU8YPAugtcN1b4EjWVq9V2xRnav6WvElo-J486ZUKK0ygxDY-blBVLxZcqOTwxhdUW1LzwxhtVZeYLdO3P62QjUYKgSjDzyJlEpSMXxLVCTiCff1ARNd32Z2zPmBWMmiyj7qWOxMl9p31aaLscvZEHg1uTs0hY7D9cj9jFk4oQqHhcrrrJbRhIxHUO0bYJBfD2ntPSMUJdlr6y0ylcKP1Q63FdPDTw9_zpJdyVCjMLy0H4JrKpU4oxuwyjf20iO1mYbgcp-9Pyds8ikUamkxYTRnKL2HdhC0p0B_BB2TBIemY1QOO5h83Lp336h67RWM5CLfzBgGbRaDzwnSUHkI0m=w1254-h620-no)

## Configuration
This section discusses how you can configure an NGINX server to serve a web application over HTTP.

### Top-Level Contexts
We first need to ensure the top-level contexts are in place; this includes `events`, `http` and `server`.
- The `events` context must be included, even if it doesn't have anything configured inside it.
- The `http` context is going to be added so that we are able to access the web application over HTTP.
- The `server` context is going to be used to create a virtual server, which will serve the web application files.
```text
events {}
http {
    server {
    }
}
```

### Virtual Server
The virtual server must be configured to understand a few important things.
All the points discussed below are configured in the virtual `server` context.
- Where are the web application files?
    - The installation folder of your web application files can be set with the `root` directive.
- What's the default index file?
    - Conventionally, the default page for a web application is the `index.html` file; this can be specified with the `index` directive.
- Multipurpose Internet Mail Extensions (MIME) Types
    - MIME Types are a way of providing more information about the files being served, so that your web browser can handle them correctly.
    - MIME Types are important especially for more modern web application frameworks and libraries using JavaScript extensively such as React, VueJS and Angular
    - MIME Types configurations come preconfigured with NGINX and can just be just added to the virtual server configuration using an `include` directive.
- Location context for accessing other resources
    - Web applications will commonly pull in other files to use, such as CSS and JavaScript.
    - The `try_files` directive can be used to help find resources, and default to a certain location if the requested resource can't be found.
```text
# for general traffic processing
events {}
# for serving over http
http {
    # virtual server for http
    server {
        # accessable on port 80
        listen 80;
        # the folder which the web application is installed
        root /opt/web-application;
        # the default web page
        index index.html;
        # included mime types
        include /etc/nginx/mime.types;
        # location context so that files from the server can be downloaded and used by your browser
        location / {
            try_files $uri $uri/ /;
        }
    }
}
```

## Tasks
This section will walkthrough configuring an NGINX server to host the web application included on this module, using the above information as a reference.
If possible, it's advised to have a Linux virtual machine for this task with a public IP address and firewall port `80` open so that it can be easily deleted afterwards, as opposed to cluttering your work machine.

### Prerequisites
Make sure that you have the following installed for this:
- Git
- NGINX

### Install the Web Application
The web application in question is included in this module folder.
All we need to do is install the application into a suitable folder, such as `/opt/web-application`:
```bash
# clone this repository
git clone https://github.com/bob-crutchley/notes
# copy the web application folders to /opt/web-application
sudo cp -r notes/topics/nginx/modules/web-server-configuration/web-application /opt/
```

### Configure NGINX
We'll now need to configure NGINX to host our web application.
Enter the following into the `nginx.conf` file:
```text
events {}
http {
    server {
        listen 80;
        root /opt/web-application;
        index index.html;
        include /etc/nginx/mime.types;
        location / {
            try_files $uri $uri/ /;
        }
    }
}
```

### Access the Web Application
Your web application should be accessable either on `localhost` if you installed it on a local machine or the public IP address on port `80`:
![NGINX Web Application](https://lh3.googleusercontent.com/4rBKXTIQR1IfBUGO5Z8xsNdrLhG8obTn4s6TICIT-j5mc9jk1twZSzw4nmA9CNmglAW8MciKcyHLaA6OXuav-XmrHy0V-_FA1xncKWf3r52GWXdkzwP4eLKoLqDiRBo--OvmBVX7VUVC6NTyOozMXusjEHWSMjaS40dbi_pXwEDDlp-7VcOGOlWFf2-Y3r1COPGAooOHaq2ZOTbRJIdwwPmCEMPG8wAXQ6fvlFAPEhEZzaThMXxn2kgAzELzfVHjW4sEQ4xJDn0tDHcn8tAHzSwyHtRSkG4yW88X5sZ75zB54pWrtU8Dt7xz_iazN0NxezbZ-ohjJdL9yRepmjqtrt-5lNhHperlnfooAAtM8CEF6GfJSORkRc5EK1J31vbhq2_-uL-Twq_FYaXjU-8poxUnaA--esG3R8FskxHowbGIZOXqzrqoFqlX5LLK4BeBZoIpMbJLQ2qX9GvSQ9-UluI6ICxGQlXlc0XEl-XCEWf2nf2nJ-KgO6vhKFIjH_EmDTLrVezSNQOWnRJ-cHXwBOy_QiBWPOPEfLvu5nBmcyn-zWu5B3JpmwjL-f1ECI3zH4gLDBrCOVhCi6demvW-Pm6yXeoFQCQZTcMUZh_WMuyvaeT20M-Lv8FZsxCrlBiz42h8EO0hJKXxmLHuaAPD_3Szw5ccxEAU__m3rGP1BiXkKyDxhpGxTwmVepaUV3wXiP2J1Toe2kPlwhK-jG8Ne4RsjBV6-21-n3yIzvrl-7Rl6AZf=w1028-h450-no)

If you see this page then you have completed the task, otherwise double check your NGINX configuration and make sure that the web application is installed into `/opt/web-application`.
