# AWS Route Tables



<!--TOC_START-->
## Contents
- [Overview](#overview)
- [Creating Route Tables](#creating-route-tables)
- [Deleting Route Tables](#deleting-route-tables)
	- [Basic Usage](#basic-usage)
- [Creating Routes](#creating-routes)
	- [Route for Internet Access](#route-for-internet-access)
- [Deleting Routes](#deleting-routes)
	- [Basic Usage](#basic-usage-1)
- [Tasks](#tasks)

<!--TOC_END-->
## Overview
A route table contains a set of rules, called routes, that are used to determine where network traffic is directed.

Each subnet in your VPC must be associated with a route table; the table controls the routing for the subnet. A subnet can only be associated with one route table at a time, but you can associate multiple subnets with the same route table.
The following are the basic things that you need to know about route tables:
- Your VPC has an implicit router.
- Your VPC automatically comes with a main route table that you can modify.
- You can create additional custom route tables for your VPC.
- Each subnet must be associated with a route table, which controls the routing for the subnet. If you don't explicitly associate a subnet with a particular route table, the subnet is implicitly associated with the main route table.
- You cannot delete the main route table, but you can replace the main route table with a custom table that you've created (so that this table is the default table each new subnet is associated with).
- Each route in a table specifies a destination CIDR and a target (for example, traffic destined for the external corporate network 172.16.0.0/12 is targeted for the virtual private gateway). We use the most specific route that matches the traffic to determine how to route the traffic.
- CIDR blocks for IPv4 and IPv6 are treated separately. For example, a route with a destination CIDR of 0.0.0.0/0 (all IPv4 addresses) does not automatically include all IPv6 addresses. You must create a route with a destination CIDR of ::/0 for all IPv6 addresses.
- Every route table contains a local route for communication within the VPC over IPv4. If your VPC has more than one IPv4 CIDR block, your route tables contain a local route for each IPv4 CIDR block. If you've associated an IPv6 CIDR block with your VPC, your route tables contain a local route for the IPv6 CIDR block. You cannot modify or delete these routes.
- When you add an Internet gateway, an egress-only Internet gateway, a virtual private gateway, a NAT device, a peering connection, or a VPC endpoint in your VPC, you must update the route table for any subnet that uses these gateways or connections.

## Creating Route Tables
When creating a route table, you will need a VPC to attach it to. This is then referenced by its ID when creating the Route Table:
```bash
# aws ec2 create-route-table --vpc-id [VPC_ID]
aws ec2 create-route-table --vpc-id vpc-a01106c2
```

## Deleting Route Tables

### Basic Usage
Like most resources, a Route Table can be deleted by referencing its ID.
Make sure that the Route Table isn't being used by any VPCs or Subnets:
```bash
# aws ec2 delete-route-table --route-table-id [ROUTE_TABLE_ID]
aws ec2 delete-route-table --route-table-id rtb-22574640
```

## Creating Routes

### Route for Internet Access
A very common reason for needing to create routes is for Internet access; we can create a route for all requests from instances in a VPC going to the `0.0.0.0/0` address range to get routed to an Internet Gateway, allowing internet access for that instance:
```bash
# aws ec2 create-route --route-table-id [ROUTE_TABLE_ID] --destination-cidr-block [ADDRESS_RANGE] --gateway-id [INTERNET_GATEWAY_ID]
aws ec2 create-route --route-table-id rtb-22574640 --destination-cidr-block 0.0.0.0/0 --gateway-id igw-c0a643a9
```

## Deleting Routes

### Basic Usage
When deleting a Route from a Route Table, you must reference the Route Table ID and the destination CIDR block (the address range) that the Route has configured - for example: `0.0.0.0/0`:
```bash
# aws ec2 delete-route --route-table-id [ROUTE_TABLE_ID] --destination-cidr-block [CIDR_BLOCK]
aws ec2 delete-route --route-table-id rtb-22574640 --destination-cidr-block 0.0.0.0/0
```

## Tasks
- Create VPC and an Internet Gateway that is attached to it.
- Create a Route Table for the new VPC.
- Add a Route that allows Internet Access for the VPC.
- Delete the Route Table, detach the Internet Gateway from the VPC and delete the it, Delete the VPC

[Go Back](../README.md#tasks)
