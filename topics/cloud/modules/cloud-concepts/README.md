# Cloud Concepts



<!--TOC_START-->
## Contents
- [Overview](#overview)
	- [What is the Cloud?](#what-is-the-cloud)
	- [On-demand self service](#ondemand-self-service)
		- [Google Cloud Platform (GCP)](#google-cloud-platform-gcp)
		- [Amazon Web Services (AWS)](#amazon-web-services-aws)
		- [Microsoft Azure (AZ)](#microsoft-azure-az)
	- [Consumption based pricing](#consumption-based-pricing)
	- [Broad network access](#broad-network-access)
	- [Resource pooling](#resource-pooling)
	- [Rapid elasticity](#rapid-elasticity)
	- [Measured service](#measured-service)
	- [Fault tolerance](#fault-tolerance)
	- [Economies of scale](#economies-of-scale)
	- [Capital expenditure](#capital-expenditure)
	- [Task](#task)

<!--TOC_END-->
## Overview
In this module you will learn about the concepts of cloud. These concepts are shared among all the cloud providers.

### What is the Cloud?

The terms ‘cloud computing’ and ‘the cloud’ have been used to describe all kinds of different technology. Are we
talking about Distributed computing? Networked Services? Virtualized Servers or Hosted services? The actual
definition of cloud computing as reported by NIST (National Institute of Standards and Technology) is: `Cloud computing 
is a model for enabling ubiquitous, convenient, on-demand network access to a shared pool of configurable computing 
resources (e.g. networks, servers, storage, applications, and services) that can be rapidly provisioned and released 
with minimal management effort or service provider interaction`

### On-demand self service

All cloud providers have a dashboard through which the customers can control the services that the provider offers. 
Hence the name `on demand self service`.

#### Google Cloud Platform (GCP)
This is how it looks for Google Cloud:
![Fork >](https://imgur.com/lwJQt2C.png)

#### Amazon Web Services (AWS)
This is how it looks for AWS:
![Fork >](https://imgur.com/cnqjq2M.png)

#### Microsoft Azure (AZ)
This is how it looks for Azure:
![Fork >](https://imgur.com/cK3lnGv.png)

### Consumption based pricing

A *Consumption based pricing* is a service and payment scheme where the customer pays according to the amount of
 resources used. 
 This is similar to how you would pay utilities companies for electricity/gas/water based on how much you've used it.
The prices may have flat rates per resource or they could be varied rates for different component. 

### Broad network access

Access over network via *standard mechanisms* which would generally be taken to mean standard protocols like HTTP or
 TCP. 
Services should be accessible to a variety of clients running on various hardware (phones, laptops, desktops).

In other words, if it’s only accessible using a proprietary protocol or data format, from custom client, it’s
 probably not cloud computing. 

Notice that *network-accessible* is not the same thing as *internet-accessible*; there is no such thing as a private
 cloud on a public network.

### Resource pooling

Cloud services are provided to multiple tenants (users, applications) by a pool of interchangeable resources.
 If each tenant needs its own, specific, customised resources, then it’s not cloud computing.
  Providing on-demand resources with utility pricing can only make economic sense if the resources come from a shared
   pool.

These resources are dynamically assigned and reassigned in order to get optimal use of out of them. 
* Storage, processing, memory, etc.

**Location independent**
* The customer generally does not know, or need to know the exact physical location of the resources
* For regulatory and architectural reasons, the customer is generally able to specify a general location; such as the
 country.
    * e.g. can this data be stored outside of the EU?
    * Can the application function well if the web-server is in the EU and the data it uses is in Australia?
    

### Rapid elasticity

Elasticity is a fundamental property of the cloud.
 The ability to use exactly the resources you need, without either under-provisioning or excessively over
 -provisioning, is one of the key benefits of cloud services.
  Allows the customer to scale in and out with demand. 
* **Note**: usually scaling in and out, as opposed to scaling up and down
May even be automatic or transparent to the customer.
Scaling up can be either vertical or horizontal. 
Vertical scaling up means adding more resources like RAM or CPU's for the environment.
Horizontal scaling up means adding more instances.
Scaling down means giving away the resources like RAM or CPU's, or shutting down the VMs.
![Fork >](https://imgur.com/npvHFLR.jpg)

### Measured service

If resources are being dynamically provisioned, it’s essential that the customer should be able to monitor the
 performance and usage of those resources in real time.
  Most cloud resources are offered on a pay-per-use basis, and the customer must be able to monitor their usage in
   order to control their costs.

### Fault tolerance

Fault tolerance concept exists not only in the cloud but also in the self-hosted environment.
 What this is referring to is the ability for your application to function even if one or more pieces in any layer
  fails.

In the cloud, you have auto-scaling as well as multiple geographical zones to help you aid with fault tolerance. 
In self-hosted domain you would need to configure the infrastructure in order for it to function in case of failure
 or maintenance. This could be done with build and orchestration tools that would monitor your resources and whether
  they are alive and responding or dead and new ones need to be created.

### Economies of scale

Cost advantage experienced by companies when the level of output increases is known as *Economies of scale*. 
This advantage comes from the relationship between per-unit cost and the quantity produced.
 Greater quantity produced lowers the per-unit cost. Increase in the output reduces the average costs, this also
  falls under the *Economies of scale*.
   The increase is brought by synergies of efficiency and operation.
  
At any stage of the production process economies of scale can be implemented.
 Production that is mentioned are all the activities related to the commodity but without the final buyer involvement.
  There are numerous ways how economies of scale can be implemented in the company like: hiring more experienced
   marketing employees, automate human to machine labor.
  

### Capital expenditure

*Capital expenditure* (CapEx) are funds that company uses to upgrade, maintain, acquire physical assets like
: buildings, technology, equipment.
 In short CapEx is the expenses that the company shows on the balance sheet marked as  investment, rather than on the
  income statement as the expenditure.

Typically used for new projects. 

CapEx is not *Operating Expenses* (OpEx), and should not be treated as such.
 OpEx are short term expenses that keep the business running.
  OpEx can actually be deducted from the company's taxes in the year it occurred.

What the CapEx can tell you is how much a company is investing in new or existing assets, for growing or maintaining
 the company.

### Task

Try to answer the following questions in order to check your knowledge.
 If you have trouble answering the question, you can check the answer below.

**Which industries use a similar consumption-based pricing models?**
<details>
<summary>Show Solution</summary>
Utilities companies that provide services like: water, electricity, gas.
</details>

**What is the difference between CapEx and OpEx?**
<details>
<summary>Show Solution</summary>
OpEx is short term expenses to keep the business running, CapEx is the business investment in new or existing
 resources with the goal of expanding the company.
</details>

**How would you describe fault tolerance in one sentence?**
<details>
<summary>Show Solution</summary>
What this is referring to is the ability for your application to function even if one or more pieces in any layer fails.
</details>

**Based on what is the price calculated for the consumption based pricing model?**
<details>
<summary>Show Solution</summary>
You pay for what you use.
</details>
