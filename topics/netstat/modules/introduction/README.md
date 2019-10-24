<!--PROPS
{
    "estTime": 15,
    "questions": [
        {
            "value": "What is the Netstat command used for?",
            "answer": "Displaying network connections for Transmission Control Protocol, routing tables, and a number of network interface and network protocol statistics",
            "choices": [
                "Provide information about the currently running processes, including their process identification numbers (PIDs)",
                "Allowing you to run programs with the security privileges of another user"
            ]
        }
    ]
}
-->

# Introduction



<!--TOC_START-->
## Contents
- [Overview](#overview)
- [Use Cases](#use-cases)
- [Example Outputs](#example-outputs)
	- [Linux](#linux)
	- [Windows](#windows)

<!--TOC_END-->
## Overview
In computing, netstat (network statistics) is a command-line network utility that displays network connections for Transmission Control Protocol (both incoming and outgoing), routing tables and network protocol statistics, and uses a number of network interfaces (network interface controller or software-defined network interface).

Netstat is usually installed on most operating systems, including: Windows, Mac and many popular Linux distributions.
One thing to take into consideration when using netstat is that the options will differ depending on which operating system you are using.

## Use Cases
The netstat tool can be used for the following:
- Finding issues in a network
- Finding what application is using a certain port
- Measuring network performance
- Showing current connections to the machine

## Example Outputs

### Linux
After running a `netstat` command on Linux, you should see an output of the connections to your machine:
```text
Proto Recv-Q Send-Q Local Address           Foreign Address         State      
tcp        0      0 work-laptop:46098       ec2-3-9-202-151.e:https ESTABLISHED
tcp        0      0 work-laptop:41682       wl-in-f188.1e100.n:5228 ESTABLISHED
tcp        0      0 work-laptop:49608       server-143-204-18:https ESTABLISHED
tcp        0      0 work-laptop:46246       lb-192-30-253-124:https ESTABLISHED
tcp        0      0 work-laptop:55948       17.47.211.130.bc.:https ESTABLISHED
tcp        0      0 work-laptop:48226       bam-8.nr-data.net:https ESTABLISHED
tcp        0      0 work-laptop:44982       server-143-204-22:https ESTABLISHED
tcp        0      0 work-laptop:46106       ec2-3-9-202-151.e:https ESTABLISHED
tcp        0      0 work-laptop:36322       104.16.70.125:https     ESTABLISHED
tcp        0      0 work-laptop:42932       do-17.lastpass.co:https ESTABLISHED
tcp        0      0 work-laptop:33642       185.199.109.154:https   ESTABLISHED
tcp        0      0 work-laptop:36784       8.255.186.35.bc.g:https ESTABLISHED
tcp        0      0 work-laptop:56196       a2-18-162-235.dep:https ESTABLISHED
tcp        0      0 work-laptop:38962       ec2-3-209-208-129:https ESTABLISHED
tcp        0      0 work-laptop:50210       ec2-54-145-70-92.:https ESTABLISHED
tcp        0      0 work-laptop:37266       47.67.201.35.bc.g:https ESTABLISHED
tcp        0      0 work-laptop:40866       151.101.192.176:https   ESTABLISHED
tcp        0      0 work-laptop:56710       101.59.190.35.bc.:https ESTABLISHED
tcp        0      0 work-laptop:46112       ec2-3-9-202-151.e:https ESTABLISHED
tcp        0      0 work-laptop:44858       ec2-52-215-192-13:https ESTABLISHED
```

### Windows
When running `netstat` on Windows, you should see an output similar to the one below:
```text
Proto  Local Address          Foreign Address        State
 TCP    127.0.0.1:5939         DESKTOP-VJCN58E:50244  ESTABLISHED
 TCP    127.0.0.1:49938        DESKTOP-VJCN58E:49939  ESTABLISHED
 TCP    127.0.0.1:49939        DESKTOP-VJCN58E:49938  ESTABLISHED
 TCP    127.0.0.1:50244        DESKTOP-VJCN58E:5939   ESTABLISHED
 TCP    127.0.0.1:50248        DESKTOP-VJCN58E:50249  ESTABLISHED
 TCP    127.0.0.1:50249        DESKTOP-VJCN58E:50248  ESTABLISHED
 TCP    127.0.0.1:50708        DESKTOP-VJCN58E:50709  ESTABLISHED
 TCP    127.0.0.1:50709        DESKTOP-VJCN58E:50708  ESTABLISHED
 TCP    127.0.0.1:52865        DESKTOP-VJCN58E:52866  ESTABLISHED
 TCP    127.0.0.1:52866        DESKTOP-VJCN58E:52865  ESTABLISHED
 TCP    127.0.0.1:52867        DESKTOP-VJCN58E:52868  ESTABLISHED
 TCP    127.0.0.1:52868        DESKTOP-VJCN58E:52867  ESTABLISHED
 TCP    127.0.0.1:52869        DESKTOP-VJCN58E:52870  ESTABLISHED
 TCP    127.0.0.1:52870        DESKTOP-VJCN58E:52869  ESTABLISHED
 TCP    172.17.25.197:52256    ams16s32-in-f10:https  CLOSE_WAIT
 TCP    172.17.25.197:52259    ams16s32-in-f10:https  CLOSE_WAIT
 TCP    172.17.25.197:52261    ams16s32-in-f10:https  CLOSE_WAIT
 TCP    172.17.25.197:52376    AT-VIE-ANX-R008:5938   ESTABLISHED
 TCP    172.17.25.197:52378    252-57-168-194:https   ESTABLISHED
 TCP    172.17.25.197:52383    252-57-168-194:https   ESTABLISHED
 TCP    172.17.25.197:52387    252-57-168-194:https   ESTABLISHED
 TCP    172.17.25.197:52388    252-57-168-194:https   ESTABLISHED
 ```
### Output Meaning
You should be able to see, from the examples above, that the outputs on Windows and Linux are very similar.
Here are the meanings of the different headings shown:
#### Proto
This is the type of protocol being used for the connection on that row.
#### Local Address
This is the network interface and port being used on the local machine.
`127.0.0.1` will mean that it's an internal connection being made (within the same machine).
If it's a private IP address, that will likely mean that the connection is being made from outside of the local machine, whether it's on the internet or just communicating with another device on the same network.
#### Foreign Address
This is where the connection is coming from.
From this property, you can determine whether the connection is contained on the same machine or coming from somewhere else.
#### State
The state tells us which state the listed sockets are in.
The TCP protocol defines states, including “LISTEN” (wait for some external computer to contact us) and “ESTABLISHED” (ready for communication).
The stranger among these is the “CLOSE WAIT” state.
This means that the foreign or remote machine has already closed the connection, but that the local program somehow hasn’t followed suit.
#### Recv-Q & Send-Q
These are properties found on the Linux output.
These tell us how much data is in the queue for that socket, waiting to be read (Recv-Q) or sent (Send-Q).
In short: if this is 0, everything’s okay, but if there are non-zero values anywhere, there may be trouble.

## Tasks
Check that netstat is working correctly by opening a command prompt on Windows, or a terminal on Linux, and running the following command:
```bash
netstat
```
Try using `netstat --help` to find out:
- Which option can be used to show the process ID (PID) of the applications using the sockets
- Which option can be used to show only TCP sockets
- Which option can be used to show the system's route table
