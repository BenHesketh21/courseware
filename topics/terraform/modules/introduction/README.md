# Introduction

<!--TOC_START-->
## Contents
- [Overview](#overview)
	- [Infrastructure as Code](#infrastructure-as-code)
	- [Workflows](#workflows)
	- [Common use cases](#common-use-cases)
- [Tasks](#tasks)
	- [Installation](#installation)
	- [Windows](#windows)
		- [Configuring the Terraform on your `PATH`](#configuring-the-terraform-on-your-path)
	- [Linux](#linux)
	- [Verify the Installation](#verify-the-installation)
	- [Creating a Simple Resource in AWS](#creating-a-simple-resource-in-aws)
	- [Creating a resource in AWS](#creating-a-resource-in-aws)
	- [Create an Access Key](#create-an-access-key)
	- [Create Some Basic Terraform Files](#create-some-basic-terraform-files)
		- [Configure the Provider](#configure-the-provider)
		- [Create a Basic Resource](#create-a-basic-resource)
		- [Use the Configurations That You Created](#use-the-configurations-that-you-created)
	- [Clean up](#clean-up)

<!--TOC_END-->
## Overview

Terraform allows you to control your infrastructure on the cloud service provider. 

The big providers are: 
* AWS
* GCP
* Azure 

### Infrastructure as Code

Infrastructure as code means that we can use a high level or descriptive programming language to describe and manage infrastructure.
 
There is a known issue with pipelines called **environment drift**, which means that over time, an environment can end up in unique configuration that cannot be automatically recreated.
 
When environments become inconsistent, deployments can be affected and testing can be made invalid.
 
With infrastructure as code, the infrastructure configurations can be versioned and maintained, so if another environment needs to be created, you can be sure that you are using up to date configurations.

### Workflows

There are a few steps that should be followed for a deployment, don't worry if you don't understand the concepts immediately, they will make more sense later on.

1. **Scope** - check resources that need to be created for a given project
2. **Author** - create the configuration file
3. **Initialise** - execute `terraform init` in the project directory where the configuration file lies. 
This will download any dependencies necessary for the selected cloud provider.
4. **Plan** - execute `terraform plan` in the project directory where the configuration file lies. 
This will verify the creation process and scan the configuration file for any detectable faults.
5. **Apply** - execute `terraform apply` in the project directory where the configuration file lies. 
This will create the actual resource as well as the state file which terraform will use to check for changes in the configuration file to what is actually deployed.

### Common use cases

* **Multi-Tier Applications** - It is very common to have applications with multiple tiers, each tier having different requirements and dependencies. 
With Terraform we are able to describe each tier of the application as a collection of resources so that the dependencies for each tier can be handled automatically.
* **Software Demos** - Although tools like Vagrant can be used to create environments for demos, vagrant can’t completely mimic production environments.
Additionally, depending on how large the infrastructure for the application is, it might be challenging to run it on something like a laptop.
 Because configurations for Terraform can be distributed, demos can be run against the end user’s infrastructure with ease. 
 Parameters for the Terraform configurations can also be tweaked so that the software can be demoed at any scale.
* **Disposable Environments** - It is common to have a staging environment before deploying to production, which is a smaller clone of the production environment. 
Production environments over time can become more complex and require more effort to mimic on a smaller scale. 
With Terraform, the infrastructure will be kept as code and can easily applied to other new environments for testing and then be disposed. 
Spinning up and disposing environments this easily means that costs can also saved on environments that do not need to be operational 24/7 and only for a fraction of that time.
* **Multi-Cloud Deployments** - Terraform has the ability to configure infrastructure across more than one cloud service.
 This hybrid solution might be due to a customer wanting to take advantage of the features available on different cloud provider solutions. 
Another reason for multi-cloud deployments could be for extra fault tolerance.

## Tasks

### Installation

We will now install terraform and check that the installation was successful.

### Windows

* Navigate to https://www.terraform.io/downloads.html in a web browser and download Terraform for 64-bit windows
* Extract the .zip file
* Copy the terraform.exe file from where you decided to extract it to a new folder: `C:\tools\terraform\`

#### Configuring the Terraform on your `PATH`
We now need to configure the `PATH` environment variable so that Terraform can be used easily on the command line.
- Press **Windows key + R** to open the **Run program**
- Type **SystemPropertiesAdvanced** and click **OK**
    
![Windows Configure Environment Variables](https://imgur.com/6y4t3MX.jpg)
    
- Select **Environment Variables...** button
    
![Select Environment Variables](https://imgur.com/XihMpT9.jpg)
    
- Under *User Variables for <your-username>*, select **New…** and enter the Variable name: **TERRAFORM_HOME** and the Variable value: `C:\tools\terraform`, then click **OK** button
    
![Environment Variables](https://imgur.com/EaIt6Jv.jpg)
    
- Under *System Variables*, select the variable called **Path** then click **Edit…** then in the next window click **New** and enter **%TERRAFORM_HOME%**
    
![System Variables](https://imgur.com/bkXxBsK.jpg)
    
- Click **OK** button on the *Environment Variable Windows* and close the *System Properties* window.
    

### Linux

Follow the steps below, entering the commands into a terminal. 
* Make sure your system is up to date:
    * If you are using Debian/Ubuntu OS: `sudo apt update && sudo apt upgrade -y`
    * If you are using CentOS/RHEL/Fedora: `sudo yum update -y`
* Ensure the unzip and wget tools are installed:
    * If you are using Debian/Ubuntu OS: `sudo apt install -y unzip wget`
    * If you are using CentOS/RHEL/Fedora: `sudo yum install -y unzip wget`
* Download the Terraform zip:
    * Please not the version here will likely not be the latest, so please use the official download page to find out what the latest download link is: https://www.terraform.io/downloads.html. 
     You will likely need to download the 64-bit version.
    `wget https://releases.hashicorp.com/terraform/0.12.12/terraform_0.12.12_linux_amd64.zip`
* Extract the Terraform zip archive: `unzip terraform_*_linux_*.zip`
* Move the Terraform binary to the /usr/local/bin folder: `sudo mv terraform /usr/local/bin`
* Remove the downloaded zip file: `rm terraform_*_linux_*.zip`

### Verify the Installation
You can verify that you have installed Terraform correctly by opening a command line or terminal and run the command below, the version of Terraform that you installed should be shown: `terraform --version`

### Creating a Simple Resource in AWS

We will now create a resource in AWS and check that it has been successfully created.

### Creating a resource in AWS

Before going forward with this task there are a couple of pre-requisites:
* Your terraform installation has to be working
* You will need an AWS account
    * If you don't have one, you can create a free account by going to: [AWS free account](https://aws.amazon.com/free)
    
We will now create a resource in AWS using Terraform.

### Create an Access Key
First you need to find your `access_key` and `secret_key` in order to give terraform access to manage resources on AWS.

You can find them by following these steps:
* Log in to your *AWS Management Console*
* Click on your user name at the top right of the page
* Click on the *Security Credentials* link from the drop-down menu
* Find the *Access Credentials* section, and copy the latest *Access Key ID*, this is the `access_key` 
* Click on the Show link in the same row, and copy the Secret Access Key, this is the `secret_key` 
    * If there is no Secret Access Key, create a new one
* Copy and save both in some text file but make sure to note down which is which. 
After saving both of them you should have them looking like this in your text file.
```
access_key = "AKIBIWX7DKIDGMCHPG4A"
secret_key = "3gSerUT5rreC989K5l4f3WcGZ0yUNaltaw4C8r/1"
```

### Create Some Basic Terraform Files
For the next step create a new folder, you can pick any name for it but a suggested one would be `example_1`.

Within the newly created folder, create a new file called `main.tf`.

Open the `main.tf` with a text editor of your choosing.

#### Configure the Provider
We will now declare in terraform syntax what provider we'll be using, as well as the `access_key`, `secret_key` and region where the resource will be created.

Place the following into your `main.tf` file:

```
provider "aws" {
	access_key = "AKIBIWX7DKIDGMCHPG4A"
	secret_key = "3gSerUT5rreC989K5l4f3WcGZ0yUNaltaw4C8r/1"
	region = "eu-west-2"
}
```

First line tells terraform that the cloud provider will be `aws`.

Second and third lines are required to authenticate with `aws` and give terraform access to manage the resources.

Fourth line is specifying which region the resource will be created.

#### Create a Basic Resource
For the next step we need to tell terraform what resource to create.

Place the following into your `main.tf` file below the `provider`:

```
resource "aws_instance" "example" {
	ami = "ami-2757f631"
	instance_type = "t2.micro"
}
```

The first line is telling terraform to create a new resource, in this case a virtual machine instance, with the name of `example`.

Second line is declaring what *Amazon Machine Image* to use for the operating system.

Third line is declaring what instance type to use, this will determine how many virtual CPUs and Memory it will have.

`main.tf` should look similar to this once you have place the two pieces of text into it:
```
provider "aws" {
	access_key = "AKIBIWX7DKIDGMCHPG4A"
	secret_key = "3gSerUT5rreC989K5l4f3WcGZ0yUNaltaw4C8r/1"
	region = "eu-west-2"
}

resource "aws_instance" "example" {
	ami = "ami-2757f631"
	instance_type = "t2.micro"
}
```

#### Use the Configurations That You Created
* Open a terminal in the directory where the `main.tf` file is located.
* Run the following command for terraform to get any required dependencies based on the cloud provider being used:
    `terraform init`
* Run the following command to scan the `main.tf` for any issues:
    `terraform plan`
* Run the following command to create the real resource:
    `terraform apply`
* Once terraform will give you a prompt about the successful operation in the *AWS console* under *Compute* and then *EC2* check that the resource has been created. 
Make sure that you are within the correct region, otherwise you won't be able to see the resource.
    

### Clean up

To delete the created resource run the following command in the terminal, make sure that the terminal is in the directory where `main.tf` is located:
    `terraform destroy` 

Check in the *AWS console* under *Compute* and then *EC2* check that the resource has been deleted.

Make sure that you are within the correct region, otherwise you won't be able to see the resource.
