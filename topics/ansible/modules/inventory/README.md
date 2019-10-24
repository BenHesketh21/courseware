<!--PROPS
{
    "estTime": 20,
    "prerequisites": [
        "bash/introduction", "networking/ip-networking", "networking/ssh-key-configuration"
    ]
}
-->

# Inventory

<!--TOC_START-->
## Contents
- [Overview](#overview)
- [Configuration Overview](#configuration-overview)
	- [Inventory Files for Different Environments](#inventory-files-for-different-environments)
- [Inventory Parameters](#inventory-parameters)
	- [Applying to a Host](#applying-to-a-host)
	- [Applying to a Group of Hosts](#applying-to-a-group-of-hosts)
	- [Ansible User](#ansible-user)
	- [SSH Private Key File](#ssh-private-key-file)
	- [SSH Arguments](#ssh-arguments)
- [Tasks](#tasks)
		- [Prerequisites](#prerequisites)
	- [Configure the Inventory File](#configure-the-inventory-file)
	- [Playbook](#playbook)
	- [Run the Playbook on the `test` Hosts](#run-the-playbook-on-the-test-hosts)

<!--TOC_END-->
## Overview
The Ansible inventory is used for defining hosts in your infrastructure to connect to and configure.
A host can be a domain name or IP address.
The default location for the inventory configurations are in the `/etc/ansible/hosts` file however, a different inventory file or hosts can be specified at any time when using the `-i` option on the command line:
```bash
# specify an inventory file
ansible-playbook -i my_inventory playbook.yaml
# specify a list of hosts
ansible-playbook -i '192.168.1.123,192.168.1.124' playbook.yaml
```

## Configuration Overview
The inventory file can be configured with an "INI-LIKE" syntax:
```ini
# single host
mail.example.com

# group of hosts
[webservers]
foo.example.com
bar.example.com

[dbservers]
one.example.com
two.example.com
216.58.205.46
```
When we are configuring ansible playbooks to run tasks we get the option to say which hosts to run the tasks on.
Either a single host or group of hosts can be specified.
When a group is specified, the tasks will be executed on all of the hosts in that particular group.
This feature makes Ansible great for configuring many hosts simultaneously.

You may want to specify the inventory file for most of the tasks that you are running, to edit `/etc/ansible/hosts` you will likely need root access on the machine.

### Inventory Files for Different Environments
Another reason for using the inventory file in a custom location is for running tasks on different environments.
You may have several environments for different development and testing purposes.

These files can then be accessed by passing them as an argument to the inventory option `-i`:
```bash
ansible-playbook -i staging playbook.yaml
ansible-playbook -i development playbook.yaml
```

## Inventory Parameters
Inventory parameters are additional properties which can be configured in the inventory file which can change things like:
- The user to connect to the machine as
- Which private SSH key to use
- The port to connect on, if you aren't using SSH on port 22
- The connection type - maybe you aren't using SSH at all and want to run the tasks locally or in a Docker container

### Applying to a Host
Inventory parameters can be applied on per-host basis, in the example shown here `inventory_parameter` would be replaced with whatever parameter you would like to use:
```ini
foo.example.com inventory_parameter=value
bar.example.com inventory_parameter=value
```

### Applying to a Group of Hosts
Quite often we are going to want to use the same parameter and value for more than one host.
This can be done by applying the parameters to a group as opposed to a single host.
In the example shown, you would replace `inventory_parameter` with the the specific parameter that you want to use:
```ini
[my-group]
foo.example.com
bar.example.com

[my-group:vars]
inventory_parameter=value
```

### Ansible User
The `ansible_user` parameter can be used to change which user to connect as, here Ansible would try to connect to the `bar.example.com` host as the user `bob`:
```ini
bar.example.com ansible_user=bob
```

### SSH Private Key File
One of Ansible's main use cases is for connecting to multiple hosts and multiple envinronments to configure many machines so naturally there are going to be different private SSH key files to access these many different hosts.

A path to a private key file can be specified with `ansible_ssh_private_key_file`.
In the example shown below Ansible will try to connect to the `foo.example.com`, authenticating with the `~/.ssh/development_id_rsa` private key file:
```ini
foo.example.com ansible_ssh_private_key_file=~/.ssh/development_id_rsa
```

### SSH Arguments
We are able to pass any arguments to the SSH connection using the `ansible_ssh_common_args` option.
A common use case for this would be to disable strict host key checking if you knew for certain that the address you are connecting to is correct.

Here is an example of the common args option being used to disable strict host key checking for SSH:
```ini
foo.example.com ansible_ssh_common_args='-o StrictHostKeyChecking=no'
```

## Tasks
In this set of tasks we are going to be configuring Ansible to be able to "ping" a group of servers.

#### Prerequisites
- Two Linux machines
    - Public IP Address
    - Port 22 open to internet access
- SSH key pair
    - Public key installed on both machines
    - Private key installed on local machine as `~/.ssh/ansible_id_rsa`

### Configure the Inventory File
There is a file in this module folder called `inventory`, use this as a template for creating your own inventory file, replacing the following:
- `IP_ADDRESS_1` and `IP_ADDRESS_2` with the public IP addresses of you machines.
- `USER` with the user you configured SSH access for on the machines

It should then look something like this, but with different IP addresses and a different user, well unless you're called Bob I guess:
```ini
[test]
IP_ADDRESS_1
IP_ADDRESS_2

[test:vars]
ansible_user=USER
ansible_ssh_common_args='-o StrictHostKeyChecking=no'
ansible_ssh_private_key_file=~/.ssh/ansible_id_rsa
```

### Playbook
The playbook has been configured for you already in a file called `playbook.yaml`.
All this playbook does is tell Ansible to connect the `test` group of hosts in the inventory file and run the `ping` module.

This playbook will confirm that we can successfully connect to all of the hosts in the `test` group and execute tasks on them:
```yaml
- hosts: test
  tasks:
  - name: "Ping {{ inventory_hostname }}"
    ping:
```

### Run the Playbook on the `test` Hosts
Now we can have a go at running the playbook, you will need to run the command shown while in this module directory.
The `-v` option is just going to show a little more information about the tasks being run, inlcuding the "pong" response from the servers:
```bash
ansible-playbook -v -i inventory playbook.yaml
```
You should then see and output similar to the following, indicating that Ansible was able to connect successfully to the hosts configured in the inventory file:
```text
bob@work-laptop:~/projects/github.com/bob-crutchley/notes/topics/ansible/modules/inventory$ ansible-playbook -i inventory -v playbook.yaml 

PLAY [test] ********************************************************************************************************************************************************************************

TASK [Gathering Facts] *********************************************************************************************************************************************************************
ok: [ec2-3-9-191-132.eu-west-2.compute.amazonaws.com]
ok: [ec2-35-178-160-92.eu-west-2.compute.amazonaws.com]

TASK [Ping] ********************************************************************************************************************************************************************************
ok: [ec2-3-9-191-132.eu-west-2.compute.amazonaws.com] => {"changed": false, "ping": "pong"}
ok: [ec2-35-178-160-92.eu-west-2.compute.amazonaws.com] => {"changed": false, "ping": "pong"}

PLAY RECAP *********************************************************************************************************************************************************************************
ec2-3-9-191-132.eu-west-2.compute.amazonaws.com : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
ec2-35-178-160-92.eu-west-2.compute.amazonaws.com : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
```
Note that the hosts (`ec2-3-9-191-132.eu-west-2.compute.amazonaws.com` & `ec2-35-178-160-92.eu-west-2.compute.amazonaws.com`) shown in the output will show as the IP addresses that you configured in your inventory file.
