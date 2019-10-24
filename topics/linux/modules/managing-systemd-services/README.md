# Managing systemd Services



<!--TOC_START-->
## Contents
- [Overview](#overview)
- [systemctl](#systemctl)
	- [Listing Services](#listing-services)
	- [Starting a Service](#starting-a-service)
	- [Stopping a Service](#stopping-a-service)
	- [Restarting a Service](#restarting-a-service)
	- [Reloading a Service Configuration](#reloading-a-service-configuration)
	- [Enabling a Service](#enabling-a-service)
		- [Enable and Start](#enable-and-start)
	- [Disable a Service](#disable-a-service)
	- [Check the Service Status](#check-the-service-status)
- [Tasks](#tasks)
	- [Install NGINX](#install-nginx)
	- [Check the Service Status](#check-the-service-status-1)
	- [Stop the Service](#stop-the-service)
	- [Check the Service Status](#check-the-service-status-2)
	- [Enable and Start the Service](#enable-and-start-the-service)
	- [Make a Configuration Change](#make-a-configuration-change)
	- [Cleanup](#cleanup)

<!--TOC_END-->
## Overview
A service, or daemon, is a background application that waits to be used, or carries out essential tasks, rather than being in direct control of an interactive user.
An example of this is all of the processes running in the background on a machine, such as: the networking services, graphical interface, etc.
We can use the systemd software suite as a unified and consistent way of controlling all of these daemons, and even use it to manage our own applications, such as web and API servers.

## systemctl
Within the systemd suite there is a tool called systemctl (System Control), which can be used to interact with services.

### Listing Services
The `list-units` command can be used to see everything being managed by systemctl.
To see the services specifically, which is what we are interested in here, we can use the `--type` option:
```bash
sudo systemctl list-units --type service
```

### Starting a Service
Use the `start` command to start a service.
The service that has been configured will be started in the background:
```bash
# sudo systemctl start [SERVICE_NAME]
sudo systemctl start my-service
```

### Stopping a Service
Use the `stop` command to stop a service.
The process managed by systemd will be terminated for you:
```bash
# sudo systemctl stop [SERVICE_NAME]
sudo systemctl stop my-service
```

### Restarting a Service
Stop and then start a service.
This can be used if a new version of the service has been installed, or if configurations for the application have been updated:
```bash
# sudo systemctl restart [SERVICE_NAME]
sudo systemctl restart my-service
```

### Reloading a Service Configuration
Some services have the capability of reloading their configuration without needing to restart.
This is the preferred option (if it's available) because if the configurations are invalid, the service will continue to use the configuration that was already in place and continue running.
Lets say a new configuration was entered for a service, and the service was then restarted, the service could crash if the configuration is invalid; however, this could be avoided by using the reload command:
```bash
# sudo systemctl reload [SERVICE_NAME]
sudo systemctl reload my-service
```

### Enabling a Service
It's common to need a service to be running once the system turns on.
We can use the enable command to make a service run on start up:
```bash
# sudo systemctl enable [SERVICE_NAME]
sudo systemctl enable my-service
```

#### Enable and Start
The `--now` option can also be used to start the service.
You can think of this as running the `start` and `enable` commands at the same time:
```bash
# sudo systemctl enable --now [SERVICE_NAME]
sudo systemctl enable --now my-service
```

### Disable a Service
This command may sound a little misleading, as it wont actuallly "disable" the service. It will actually just stop it running on startup (so the opposite of enabling a service):
```bash
# sudo systemctl disable [SERVICE_NAME]
sudo systemctl disable my-service
```

### Check the Service Status
To make sure everything is running well, you can check the status of your service using the `status` command:
```bash
# sudo systemctl status [SERVICE_NAME]
sudo systemctl status my-service
```

## Tasks
Here are some tasks that will give you a chance to use the commands shown above.
NGINX will be used as an example for these commands; you don't need to fully understand what NGINX is, just that it's a web-server and, in this case, is managed as a systemd service.
For these tasks, its best to have a fresh install of Debian or Ubuntu

### Install NGINX
We can use `apt` to get our NGINX server downloaded and configured as a systemd service. We'll also install curl, for getting a response from the NGINX server:
```bash
sudo apt install -y nginx curl
```

### Check the Service Status
Make sure that NGINX is running by checking its status:
```bash
sudo systemctl status nginx
```

### Stop the Service
First, lets get a response from the server:
```bash
curl localhost
```
You should see a basic HTML (web page) response.
Now, stop the service:
```bash
sudo systemctl stop nginx
```
If we use curl to try and get a response from the server, it should fail:
```bash
curl localhost
```

### Check the Service Status
We can now see that the service has been stopped, by checking its status:
```bash
sudo systemctl status nginx
```

### Enable and Start the Service
Make sure that the NGINX service will run on startup by enabling it.
The service can be started back up at the same time too:
```bash
sudo systemctl enable --now nginx
```
Check the status to see that the service is back up and running:
```bash
sudo systemctl status nginx
```

### Make a Configuration Change
Edit the `/etc/nginx/nginx.conf` using `sudo`, or as the `root` user, and enter the following:
```nginx.conf
events {}
http {
    server {
        location / {
            return 200 "Reload Worked!\n";
        }
    }
}
```
Then, reload the NGINX service:
```bash
sudo systemctl reload nginx
```
We can then check that the configration has taken effect on the server, by making a request to it (again using curl):
```bash
curl localhost
```
The server should reply with `Reload Worked!`

### Cleanup
Undo the changes we made by running the following:
```bash
sudo systemctl disable nginx 
sudo systemctl stop nginx
sudo apt purge -y nginx
```
