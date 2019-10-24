# Virtual Private Cloud (VPC)



<!--TOC_START-->
## Contents
- [Overview](#overview)
- [Creating a VPC](#creating-a-vpc)
	- [Basic Usage](#basic-usage)
	- [CIDR Blocks & Limitations](#cidr-blocks--limitations)
- [View Existing VPCs](#view-existing-vpcs)
	- [Basic Usage](#basic-usage-1)
	- [Getting the ID Property Using Queries](#getting-the-id-property-using-queries)
- [Delete VPCs](#delete-vpcs)
	- [Basic Usage](#basic-usage-2)
	- [Creating a Default VPC](#creating-a-default-vpc)
- [Tasks](#tasks)
	- [Managing a Simple VPC](#managing-a-simple-vpc)
		- [Create a new VPC with a CIDR block of `10.0.0.0/16`](#create-a-new-vpc-with-a-cidr-block-of-1000016)
		- [Delete a VPC using ID](#delete-a-vpc-using-id)
		- [Storing a VPC's ID in a Bash Variable](#storing-a-vpcs-id-in-a-bash-variable)
		- [Using a Bash Variable to Delete a VPC](#using-a-bash-variable-to-delete-a-vpc)
		- [Make sure that there are none of the VPCs we created here are left and move on to the next section:](#make-sure-that-there-are-none-of-the-vpcs-we-created-here-are-left-and-move-on-to-the-next-section)
	- [Learn how to Fully Configure a VPC](#learn-how-to-fully-configure-a-vpc)

<!--TOC_END-->
## Overview
Amazon Virtual Private Cloud (Amazon VPC) lets you provision a logically isolated section of the AWS Cloud where you can launch AWS resources in a virtual network that you define.
You have complete control over your virtual networking environment, including selection of your own IP address range, creation of subnets, and configuration of route tables and network gateways.
You can use both IPv4 and IPv6 in your VPC for secure and easy access to resources and applications.

You can easily customize the network configuration for your Amazon VPC.
For example, you can create a public-facing subnet for your web servers that has access to the Internet, and place your backend systems such as databases or application servers in a private-facing subnet with no Internet access.
You can leverage multiple layers of security, including security groups and network access control lists, to help control access to Amazon EC2 instances in each subnet.

## Creating a VPC

### Basic Usage
VPCs can be created very easily - you should only have to provide the CIDR block, which defines the address range for your subnet:
```bash
# aws ec2 create-vpc --cidr-block [CIDR_DEFINITION]
aws ec2 create-vpc --cidr-block 10.0.0.0/16
```

### CIDR Blocks & Limitations
The CIDR block is what defines the size of your network.
The smallest CIDR block you can have is /28, with 16 hosts, or /16, which can have up to 65,536 hosts.

## View Existing VPCs

### Basic Usage
You may want to view the existing VPCs to view the properties of them:
```bash
aws ec2 describe-vpcs
```

### Getting the ID Property Using Queries
To manage a VPC, such as when you want to delete it, you will need to be able to reference that VPC by its ID.
If you have several VPCs then the output can be a little overwhelming, considering that you just want to see the IDs.
We can use a query, like the one below, and change the output to be text only; this will return a list of VPC IDs:
```bash
# aws ec2 describe-vpcs --output [OUTPUT_TYPE] --query [JSON_QUERY]
aws ec2 describe-vpcs --output text --query "Vpcs[].VpcId"
```

## Delete VPCs

### Basic Usage
The VPC ID must be provided when deleting a VPC:
```bash
# aws ec2 delete-vpc --vpc-id [VPC_ID]
aws ec2 delete-vpc --vpc-id vpc-061635ad5414cf433
```

### Creating a Default VPC
A default VPC is suitable for getting started quickly, and for launching public instances such as a blog or simple website. You can modify the components of your default VPC as needed.
Other resources that are needed to get EC2 instances functional are already in place such as an Internet Gateway, DHCP Options Set, Subnets and Security Groups.

If, for whatever reason, you have deleted your default VPC, it's easy to create another one:
```bash
aws ec2 create-default-vpc
```

## Tasks

### Managing a Simple VPC
Try to complete the following tasks, using the commands you learned above:

#### Create a new VPC with a CIDR block of `10.0.0.0/16`
This example creates a VPC network that can have up to 65,536 hosts:
```bash
aws ec2 create-vpc --cidr-block 10.0.0.0/16
```

#### Delete a VPC using ID
We can then delete the VPC using its ID; just replace `[VPC_ID]` in the command below with the ID of your VPC you just created:
```bash
aws ec2 delete-vpc --vpc-id [VPC_ID]
```

#### Storing a VPC's ID in a Bash Variable
```bash
vpc_id=$(aws ec2 create-vpc --cidr-block 10.0.0.0/16 --query Vpc.VpcId --output text)
echo ${vpc_id}
```
You wil now be able to access the `vpc_id` variable in other parts of the script you are writing.

#### Using a Bash Variable to Delete a VPC
```bash
aws ec2 delete-vpc --vpc-id ${vpc_id}
```

#### Make sure that there are none of the VPCs we created here are left and move on to the next section:
```bash
aws ec2 describe-vpcs
```

### Learn how to Fully Configure a VPC
Unless you create a default VPC, there are several other components to understand and configure:
- Learn about [Subnets](./subnets)
- Learn about [Internet Gateways](./internet-gateways)
- Learn about [Route Tables](./route-tables)
- Learn about [Security Groups](./security-groups)

[Go Back](../README.md#tasks)
