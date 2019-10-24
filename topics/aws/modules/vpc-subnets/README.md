# EC2 VPC Subnets
A VPC spans all the Availability Zones in the region.
After creating a VPC, you can add one or more subnets in each Availability Zone.
When you create a subnet, you specify the CIDR block for the subnet, which is a subset of the VPC CIDR block.
Each subnet must reside entirely within one Availability Zone and cannot span zones.
Availability Zones are distinct locations that are engineered to be isolated from failures in other Availability Zones.
By launching instances in separate Availability Zones, you can protect your applications from the failure of a single location.
We assign a unique ID to each subnet.



<!--TOC_START-->
## Contents
- [Creating Subnets](#creating-subnets)
	- [Basic Usage](#basic-usage)
- [View Existing Subnets](#view-existing-subnets)
	- [Basic Usage](#basic-usage-1)
	- [Getting the ID Property Using Queries](#getting-the-id-property-using-queries)
- [Delete Subnets](#delete-subnets)
	- [Basic Usage](#basic-usage-2)
- [Tasks](#tasks)

<!--TOC_END-->
## Creating Subnets

### Basic Usage
After you create a subnet, you can't change its CIDR block.
The size of the subnet's IPv4 CIDR block can be the same as a VPC's IPv4 CIDR block, or a subset of a VPC's IPv4 CIDR block.
If you create more than one subnet in a VPC, the subnets' CIDR blocks must not overlap.
The smallest IPv4 subnet (and VPC) you can create uses a /28 netmask (16 IPv4 addresses), and the largest uses a /16 netmask (65,536 IPv4 addresses).

When you create each subnet, you provide the VPC ID and IPv4 CIDR block for the subnet:
```bash
# aws ec2 create-subnet --vpc-id [VPC_ID] --cidr-block [CIDR_BLOCK]
aws ec2 create-subnet --vpc-id vpc-081ec835f3EXAMPLE --cidr-block 10.0.1.0/24
```

## View Existing Subnets

### Basic Usage
You may want to view the existing Subnets to view the properties of them:
```bash
aws ec2 describe-subnets
```

### Getting the ID Property Using Queries
To manage a Subnet, such as when you want to delete it, you will need to be able to reference that Subnet by its ID.
If you have several Subnets, the output can be a little overwhelming, considering that you just want to see the IDs.
We can use a query, like the one below, and change the output to be text only; this will return a list of Subnet IDs:
```bash
# aws ec2 describe-subnets --output text --query Subnets[].SubnetId
aws ec2 describe-subnets --output text --query Subnets[].SubnetId
```

## Delete Subnets

### Basic Usage
The Subnet ID must be provided when deleting a Subnet:
```bash
# aws ec2 delete-subnet --subnet-id [SUBNET_ID]
aws ec2 delete-subnet --subnet-id subnet-04c9613a521b24db0
```

## Tasks
Try to complete the following tasks using the commands you learned above:
- Create a new VPC with a CIDR block of 10.0.0.0/16
- Create a new Subnet inside the VPC you made, with a CIDR block of 10.0.1.0/24
- Create another Subnet inside the same VPC, with a CIDR block of 10.0.2.0/24
- List the Subnets you have, showing only the IDs of them
- Delete the VPC and Subnets that you created.

[Go Back to VPC Tasks](../README.md#tasks)
