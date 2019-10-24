<!--PROPS
{
    "prereqs": [
        "jenkins/web-setup",
        "jenkins/jobs",
        "jenkins/freestyle-project",
        "linux/systemd",
        "linux/sudo"
    ]
}
-->

# Basic Python Flask Freestyle Project Deployment with systemd



<!--TOC_START-->
## Contents
- [Overview](#overview)
- [Sample Project](#sample-project)
- [Host Machine Configuration](#host-machine-configuration)
- [Jenkins Job](#jenkins-job)
- [Shell Script](#shell-script)
	- [Installing the systemd Service](#installing-the-systemd-service)
	- [Installing and Configuring the Application Files](#installing-and-configuring-the-application-files)

<!--TOC_END-->
## Overview
Basic deployment of a Python Flask server, using systemd and a Freestyle Project.
Included in this module folder is a Python Server that uses the Flask framework.

## Sample Project
The sample project included for this example is a single python script.
There is also a systemd service configuration included, for running the application as the `pythonadm` user.
Please note that, because of systemd, this example will not work inside a docker container.

## Host Machine Configuration
There are a few prerequisites for this module, so make sure the following has been configured on your machine:
- Linux operating system with systemd, not in a container
- Jenkins installed & running
- Python 3 installed
- Jenkins user, configured as a sudo user with no password

## Jenkins Job
Create a Jenkins Freestyle Project called flask-app and configure it to download this code onto its filesystem; this can be configured in the Source Control Management section:
- `Repository URL` set to `https://github.com/bob-crutchley/notes`

## Shell Script
Add the following into an `Execute shell` build step:
```bash
# move to module folder
cd ./topics/jenkins/modules/basic-python-flask-freestyle-project-deployment-with-systemd
# install the service script
sudo cp flask-app.service /etc/systemd/system/
# reload the service scripts
sudo systemctl daemon-reload
# stop the old service
sudo systemctl stop flask-app
# install the application files
install_dir=/opt/flask-app
sudo rm -rf ${install_dir}
sudo mkdir ${install_dir}
sudo cp -r ./* ${install_dir}
sudo chown -R pythonadm:pythonadm ${install_dir}
# configure python virtual environment and install dependencies
sudo su - pythonadm << EOF
cd ${install_dir}
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements.txt
EOF
# start the flask app
sudo systemctl start flask-app
```
See below for explanation of the commands used in this script:

### Installing the systemd Service 
To account for any changes to the script, or if this is the first time installing the application, the service script needs to be installed into `/etc/systemd/system/`.
For systemd to pickup the changes, we must also reload the services with `systemctl daemon-reload`.
Before we start replacing the old application files, the service should be stopped by running `systemctl stop flask-app`:
```bash
# install the service script
sudo cp flask-app.service /etc/systemd/system/
# reload the service scripts
sudo systemctl daemon-reload
# stop the old service
sudo systemctl stop flask-app
```

### Installing and Configuring the Application Files
Here, we can recreate the application folder to make sure we have a fresh start.
Once the folder has been recreated, the application can be copied in.
We then need to make sure that `pythonadm` owns the folder, because that's the user that is going to be running the application.
Then we need to setup the python virtual environment and install the dependencies.
This is ran as the `pythonadm` user, to make sure that the files remain owned by the `pythonadm` user.
Once all that is done, the service can then be started again using `sudo systemctl start flask-app`.
```bash
# install the application files
install_dir=/opt/flask-app
sudo rm -rf ${install_dir}
sudo mkdir ${install_dir}
sudo cp -r ./* ${install_dir}
sudo chown -R pythonadm:pythonadm ${install_dir}
# configure python virtual environment and install dependencies
sudo su - pythonadm << EOF
cd ${install_dir}
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements.txt
EOF
# start the flask app
sudo systemctl start flask-app
```
