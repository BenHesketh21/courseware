# AWS EC2 Instances



<!--TOC_START-->
## Contents
- [Overview](#overview)
- [Amazon Machine Images (AMIs)](#amazon-machine-images-amis)
	- [Overview](#overview-1)
	- [Viewing Available AMIs](#viewing-available-amis)
- [Running an Instance](#running-an-instance)
	- [Basic Usage](#basic-usage)
- [View Running Instances](#view-running-instances)
	- [Basic Usage](#basic-usage-1)
- [Terminate a Running Instance](#terminate-a-running-instance)
	- [Basic Usage](#basic-usage-2)
- [Tasks](#tasks)

<!--TOC_END-->
## Overview
An EC2 instance is a virtual server in Amazon’s Elastic Compute Cloud (EC2) for running applications on the Amazon Web Services (AWS) infrastructure.

AWS is a comprehensive, evolving cloud computing platform; EC2 is a service that allows business subscribers to run application programs in the computing environment. The EC2 can serve as a practically unlimited set of virtual machines. 

Amazon provides a variety of types of instances with different configurations of CPU, memory, storage, and networking resources to suit user needs. Each type is also available in two different sizes to address workload requirements.

Instance types are grouped into families based on target application profiles. These groups include: general purpose, compute-optimized, GPU instances, memory optimized, storage optimized and micro instances.

## Amazon Machine Images (AMIs)

### Overview
Instances are created from Amazon Machine Images (AMI).
The machine images are like templates that are configured with an operating system and other software, which determine the user’s operating environment.
Users can select an AMI provided by AWS, the user community, or through the AWS Marketplace.
Users can also create their own AMIs and share them.

### Viewing Available AMIs
We need to provide an AMI when running an instance; Amazon has a page with commands for finding the latest image for popular operating systems: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/finding-an-ami.html. Please note that you will need `jq` installed to run the commands provided.
Here is an example that gets the latest `ubuntu 18.04` image id (AMI):
```bash
aws ec2 describe-images --owners 099720109477 --filters 'Name=name,Values=ubuntu/images/hvm-ssd/ubuntu-bionic-18.04-amd64-server-????????' 'Name=state,Values=available' --output json | jq -r '.Images | sort_by(.CreationDate) | last(.[]).ImageId'
```

## Running an Instance

### Basic Usage
Running an instance requires quite a few options:
- **Image ID:**
    This is the base image that the machine will use, and it usually comes with an operating system install, such as Ubuntu.
- **Count:**
    The amount of instances to run from this command
- **Instance Type:**
    The size of the machine, how many CPUs and how much RAM
- **Key Name:**
    The Key Pair to install onto the machine. We need this to be able to securely connect to the instance with SSH.
- **Subnet ID:**
    Which subnet to run the instance in. The instance will be given a private IP address, from the subnet that you put it in, and security group rules from the VPC will be applied to the instance.
```bash
# aws ec2 run-instances --image-id [IMAGE_ID] --count [AMOUNT_OF_INSTANCES] --instance-type [MACHINE_SIZE] --key-name [KEY_PAIR_NAME] --subnet-id [SUBNET_ID]
aws ec2 run-instances --image-id ami-0ee246e709782b1be --count 1 --instance-type t2.micro --key-name MyKeyPair --subnet-id subnet-0b601356c0674d00d
```

## View Running Instances

### Basic Usage
To check what existing instances there are, we can use the `describe-instances` command:
```bash
aws ec2 describe-instances
```

## Terminate a Running Instance

### Basic Usage
We can terminate instances by providing their IDs to the `terminate-instances` command:
```bash
# aws ec2 terminate-instances --instance-ids [INSTANCE_IDS]
aws ec2 terminate-instances --instance-ids i-1234567890abcdef0
```

## Tasks
- Create and configure a VPC with the following:
    - CIDR Block of 10.0.0.0/16
    - Associated Internet Gateway
    - Route Table configured for Internet Access
    - Subnet with a CIDR block of 10.0.1.0/24
    - Security Group that allows SSH access from anywhere
- Create a Key Pair called MyKeyPair, and store the private key into `~/.ssh/MyKeyPair.pem`
- Run an EC2 instance with the following:
    - AMI of your choice
    - The Key Pair you created
    - and put it in the Subnet that you created
- Connect to your EC2 instance using SSH and the private key that you stored

[Go Back](../README.md#tasks)
