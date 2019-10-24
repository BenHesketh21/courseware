# Configuration



<!--TOC_START-->
## Contents
- [Overview](#overview)
- [Directives](#directives)
- [Include Directive](#include-directive)
- [Top-Level Contexts](#toplevel-contexts)
- [Virtual Servers](#virtual-servers)
	- [HTTP](#http)
	- [Mail & Stream](#mail--stream)
- [Reloading configurations](#reloading-configurations)
- [Tasks](#tasks)
	- [Edit the `nginx.conf` File](#edit-the-nginxconf-file)
	- [Reload the New Configurations](#reload-the-new-configurations)
	- [View the New Changes](#view-the-new-changes)
		- [Response In a Web Browser](#response-in-a-web-browser)
		- [Response Using `curl`](#response-using-curl)

<!--TOC_END-->
## Overview
NGINX uses a text-based configuration file written in a specific format.
The default file used to configure NGINX is the `nginx.conf` file. This can be found in `/etc/nginx` on Linux systems, and in `[INSTALL_PATH]/conf/nginx.conf` - `[INSTALL_PATH]` on Windows machines (based on the location that you unzipped the NGINX folder to).

## Directives 
When configuring the `nginx.conf` file it will contain *directives* and their parameters.
You can use simple single-line directives which just have 1 parameter; like a key-value pair:
```text
user    nginx;
```
Other directives can act as a container, holding other related directives enclosed using curl braces (`{}`).
These types of directives are often referred to as *blocks* or *contexts*:
```text
location / {
    return 200 "OK\n";
}
```

## Include Directive
NGINX configurations can become difficult to maintain due to the size and length of the file getting larger.
The `include` directive can be used to effectively "import" other configurations from other files.
You can use this for feature-specific configuration files; conventionally you would store these extra files in `/etc/nginx/conf.d` on Linux systems and `[INSTALL_FOLDER]/conf` on Windows.
Here is an example for the `conf.d/http` and `conf.d/stream` files being included:
```text
include conf.d/http;
include conf.d/stream;
```

## Top-Level Contexts
There are a few top-level contexts that are used to group together directives for handling different traffic types:
- **events**: Genereal connection processing
- **http**: HTTP Traffic, which can be used for things like web applications
- **mail**: Mail Traffic, for when you are using NGINX with an SMTP (Mail) server
- **stream**: TCP and UDP traffic, for when your application is using TCP to communicate, as opposed to something like HTTP
Any directives that get place outside of these contexts are said to be in the *main* context.
```text
# this directive is included in the main context
user nginx;

events {
    # directives here apply to all traffic types
}

http {
    # http configurations
}
```

## Virtual Servers
One or more server blocks can be included in each of the traffic handling contexts.

### HTTP
HTTP virtual servers are used for handling traffic for resources depending on what IP address or domain is used.
Furthermore, a location context can be included to handle a specific Universal Resource Identifier (URI).

Here is an example configuration for using 2 virtual servers and 4 location contexts.
To avoid collisions with port mappings, each virtual server has been set to listen on a different port using the `listen` directive under the `server` contexts.
By default, the HTTP virtual server will listen on port `80`.
```text
events {}
http {
    server {
       location /one {
            listen 8001;
            return 200 "Location 1, Virtual Server 1\n";
       }
       location /two {
            listen 8002; 
            return 200 "Location 2, Virtual Server 1\n";
       }
    }
    server {
       location /one {
            listen 9001;
            return 200 "Location 1, Virtual Server 2\n";
       }
       location /two {
            listen 9002;
            return 200 "Location 2, Virtual Server 2\n";
       }
    }
}
```
If you were to make requests to an NGINX server with this configuration (assuming you are accessing NGINX using `localhost`), you would see the following responses depending on the URI and ports used:

|Request|Response|
|-------|--------|
|http://localhost:8001/one|Location 1, Virtual Server 1|
|http://localhost:8002/two|Location 2, Virtual Server 1|
|http://localhost:9001/one|Location 1, Virtual Server 2|
|http://localhost:9002/two|Location 2, Virtual Server 2|

### Mail & Stream
For the Mail and TCP/UDP traffic the `mail` and `stream` contexts are used respectively.
You would use the `stream` context if the applications you are using NGINX with uses TCP or UDP traffic, as opposed to HTTP.

Streams can be used for proxying requests that are TCP or UDP, as opposed to HTTP; this example accepts TCP connections on port `80` and proxies them to `192.168.1.123:8080`.
```text
stream {
    server {
        listen 80
        proxy_pass 192.168.1.123:8080;
    }
}
```

## Reloading configurations
Once you have made a change to the NGINX configuration, you will likely notice that nothing has actually happened. This is because the NGINX configurations must be reloaded.

We can send the `reload` signal to NGINX using the `-s`option:
```bash
nginx -s reload
```
Configurations on Linux can also be reloaded by using `systemctl`:
```bash
sudo systemctl reload nginx
```

## Tasks
Here we are going to be changing the `nginx.conf` file so that it can return three different values depending on what URI we request.

### Edit the `nginx.conf` File
Start by editing the `nginx.conf` file to contain the following:
```text
# the events context must exist for any configuration to work
events {}
# http context because we are going to be making http requests
http {
    server {
        # this vritual server can be accessed on port 80
        listen 80;
        location / {
            return 200 "Default Location\n";
        }
        location /one {
            return 200 "Location One\n";
        }
        location /two {
            return 200 "Location Two\n";
        }
    }
}
```

### Reload the New Configurations
Before our changes are going to work we need to reload our NGINX configurations.
On Linux first try using `systemctl`:
```bash
sudo systemctl reload nginx
```
Otherwise use the `nginx` binary:
```bash
nginx -s reload
```

### View the New Changes
We can then use a web browser to see the changes by putting the different resources in the URL bar (`/`, `/one`, `/two`).
If you are on a Linux machine with no GUI, the `curl` command can be used to make HTTP requests to NGINX.

Depending on the URI request that you made, you should get the relevant response from NGINX for how you configured it above.

#### Response In a Web Browser
![NGINX Default Location](https://lh3.googleusercontent.com/zvRwSbAuZTBwFswyeLBlnrejvGeXXFhSj46CRv_BcGLc24vq7NXDXnnTqOArLyTPzwnvJW-D9J5W3jjzqTmdeG2v3JyJMgekL3CO7ENhYij4_fphEBZAaQLcenWRNGJRE-MG3txSQIVFqQRNDU3vlSaStCAr9JZmNfNfdNH_-2ieGEnIAIqpAe3vqKFg9f4i78RaJlY7B0YTq-IReQ2uXe7qiVU4ZzdlI0nARuxYWnBPfxIVL4czTqajMyMvIHtHx0wxnscljfk4t6aX-L5TN35rYBrVm9LBffJ6davYqL8xCNOYjcM0KJs2-EgcbuxDRZe5grJt1gc1ZC-2YkDJL189ayiy_QgkzdvnCTKd8Vta2Omb2DJJ-YbY4PPLnRvHI1NkNvMM8HH5D3AK7rW6zlUjDK7XIvpLK6stYSscvpAVJ9YZ1qZHz5wMUvD8-_ejXS4v0oqHnlm__ICX-rFNIPmOcy1Og5LdkXNIudqbyqgba6_fQ5rLKldO5VndwomTS1-44JEJW7qwyrBrz9jf00TEdhSapBHtPnlWdQt1At2nlnL_feCHejORwIkmK4Yeqohk_pE6xycPMkuMeXTsJt2Fy8LR-r1p3p32EVtStZmzxj_fh7limlm2V4s1p76KQwPT4dPO_57vxqxN860AbGC86XBlFNFSysCdlGQ0JDPuXx-PJRpDCWCfpYu97zHYxJgRmVoRQYC7b7nd0P07no3pHLTNGaLmuFRTPLvevE5NvTGL=w1030-h117-no)
![NGINX One Location](https://lh3.googleusercontent.com/ou48oAWQIHHDH7ETrVA9mClrO3FrbXYOtOgBKbvWNxpZrWh96jdfQq3r5cWL3gOOuvrzLMDWeIqDdMmFqT9omG9b3Pub9-F5WuEecVB9L-3B-Spxb9tOWzIFjny30MapJVJH_wBcib05RYx8fLhcefR7JSe4u88RFFmiJzimEkdq1DUP5pd2X7uo-cZ4NWfHP_1thYLwWvgccQ2BbZRXhDapPCoIvzg8N5bh7WGkhFogl25_ZF7p_knEjRuzcuuwSdbdkkcoOl1eKm-QSFFly8xp5NV_CuL_gfzRwtxG_gKJhzu6n_RfYSm7Y_RjP7uhh9LeHELvtHD1HIRrzNSPQNrfkPUxr1IjRB_prqCY6qYeBtq_2ERu9ep8cQWH5I7qyfeaKtIihaCLta4__VAJD0JIphy-Wgmipvfc7zp0J7rIVT20rp-OVq4VdX5W7HahFdK1S89nud5iFPMv1fI0LZS2XxKaDA78OkuvxhZjwqV8flcAcXLu6yIz3nX5I0tGa3qqN2iQ2Iyc-ap7CSson_OLW5KZS7b1rYAoVswAdt-tegCzkZo1g_3FivbTy3OohFzFCfds7je8CQNvBGylAtk0pRrTAXokM7IFGlcrUDpAp2P6R2XTuv02qNe9d2eCtwFRSy_2Sy3HByD7EZhHGHpaxlkCL_34uIgw5Kqs9MyrTE6eYDSZiXniEUtlrQ2NcQVyB2GxGgxxoxeY-4VN2SibkqYux_lq-n2z84r2qB9NQrVG=w1029-h115-no)
![NGINX Two Location](https://lh3.googleusercontent.com/HEFDlUmKvtq53zasqkcfVwoBhVtFSIAkAErWQbzzp5yHj3m7aArKtKN6eLGOYElX-MEQ_Jn4ADN_4s98ZynUoEw_YxYeyDpao-1Tq32p5D_lW51ll_Oy6MUax14wuiuY4LfR8FDp3f8wiiCOyHSrOE0YSzwweUolbD91AAXIxho1h9IbSZKG94sOPH_410sIefJtW1B5phM3Mim5JVjdHdWQkx22LAE1Apy0BRE4OwJsggAy-ke_RZN7HoWMNeRGXUqPxEAVJKIthCgFxKgMv0ALFZ7WvIVBtzfzt7_zm6D2hX4qHD5btv9fbP8liiKYVgkv9xCsy4Sdj6EHu3X3rOVhZekQioxpYyvw8G-6GrX0ZGYqD6Zo9M3SgsSeeJcavfgDNoL7FJv6HtJ2cZLsOExEeqHNuM1EJ12xBqJzLpBN_ZktKJlKeIOuhccTkL95gXDAMe0V-nKAjsXKDkvbfJCRmysYpo8T5saOISUUQoO_zYMNYzdjHX8uFFEQVIu2twk5ul96SgUmDfvjvxjN56-g9Try-EojDZAmWSypfZSVInq3wwd935WFJm8HotndMJPwH3dGCDtYpADYRyL7-XIz_tmDG0HBsW6Arab2z7jKpY1N6eXbKUXt8E-RBmgYa78sLLJMuP8gu9rBRgGCiFjjFhFLVHrUKjHFqHBIVSJertcW85NbUFgj9tTapp6TNIvhmYz5vMfRdyfUQvMdXNZUHEdXTkn-g9Sn1Q28_3qGmGNl=w1029-h116-no)

#### Response Using `curl`
```text
bob@work-laptop:~/projects/github.com/bob-crutchley/notes$ curl http://localhost
Default Location
bob@work-laptop:~/projects/github.com/bob-crutchley/notes$ curl http://localhost/one
Location One
bob@work-laptop:~/projects/github.com/bob-crutchley/notes$ curl http://localhost/two
Location Two
```
