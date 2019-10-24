<!--PROPS
{
   "estTime": 30,
   "questions": [
        {
            "value": "What does MAC stand for?",
            "answer": "Media Access Control.",
            "choices": [""]
        },
        {
            "value": "What is a MAC Address?",
            "answer": "A unique identifier assigned to a Network Interface Controller (NIC).",
            "choices": [""]
        }
   ]
}
-->

# MAC Address



<!--TOC_START-->
## Contents
- [Overview](#overview)
- [Relevence & Day to Day Application](#relevence--day-to-day-application)
	- [Public Wifi](#public-wifi)
- [Viewing Your MAC Address](#viewing-your-mac-address)
	- [Windows](#windows)
	- [Linux](#linux)
		- [Using ifconfig](#using-ifconfig)
		- [Using ip](#using-ip)
- [Format](#format)
	- [Hexadecimals](#hexadecimals)
	- [OEM & Unique ID](#oem--unique-id)
- [Spoofing](#spoofing)
	- [Linux](#linux-1)
	- [Windows](#windows-1)
	- [Why?](#why)
- [Tasks](#tasks)
	- [Find Out About Your Current MAC Address](#find-out-about-your-current-mac-address)
	- [Change Your MAC Address](#change-your-mac-address)

<!--TOC_END-->
## Overview
A Media Access Control (MAC) address of a device is a unique identifier assigned to a Network Interface Controller (NIC).
A NIC, is a computer hardware component that connects a computer to a computer network; this often comes in the form of an Ethernet port on the device or a wireless adapter.
For communications within a network segment, it is used as a network address for most IEEE 802 network technologies, including Ethernet, Wi-Fi, and Bluetooth.  
MAC addresses are used as physical hardware addresses for devices on a network.
These are important because they are unique for every piece of networking hardware.
The main usage case is within a low level of networking when delivering frames (packets of data) over Local Area Networks (LAN) to make sure that the data is getting to the correct device.

## Relevence & Day to Day Application
Because MAC addresses are used on such a low level for LAN; any network connection made, be it browsing the internet or making a video call, will end up using MAC addresses at some point for the connection to be established.

### Public Wifi
MAC addresses are there for identifying a device, so this can be utilised for something like public Wifi.
When you try to log into a Wifi network in an Hotel or Coffee shop for example, you will likely be faced with a pay wall.
After purchasing Wifi access, the MAC address of the current device you are using can be stored on their servers, so that any traffic coming from your device will be allowed onto the Internet.

## Viewing Your MAC Address

### Windows
On a Windows machine you can use the `ipconfig /all` command inside a command prompt or PowerShell to see what your MAC address is.
The MAC addresse can be found under the `Physical Address` property:
```text
Wireless LAN adapter Wi-Fi:

   Connection-specific DNS Suffix  . :
   Description . . . . . . . . . . . : Intel(R) Dual Band Wireless-AC 7265
   Physical Address. . . . . . . . . : DC-53-60-BD-C4-64
   DHCP Enabled. . . . . . . . . . . : Yes
   Autoconfiguration Enabled . . . . : Yes
   Link-local IPv6 Address . . . . . : fe80::7194:cbcc:656f:f492%4(Preferred)
   IPv4 Address. . . . . . . . . . . : 172.17.25.18(Preferred)
   Subnet Mask . . . . . . . . . . . : 255.255.255.0
   Lease Obtained. . . . . . . . . . : 28 August 2019 11:03:21
   Lease Expires . . . . . . . . . . : 29 August 2019 11:03:21
   Default Gateway . . . . . . . . . : 172.17.25.1
   DHCP Server . . . . . . . . . . . : 172.17.25.1
   DHCPv6 IAID . . . . . . . . . . . : 81548128
   DHCPv6 Client DUID. . . . . . . . : 00-01-00-01-24-33-DD-D2-B8-6B-23-7B-7B-C3
   DNS Servers . . . . . . . . . . . : 8.8.8.8
                                       9.9.9.9
   NetBIOS over Tcpip. . . . . . . . : Enabled
```

### Linux
Depending on what tools are installed on your system there are several ways that you can get your MAC address:

#### Using ifconfig
Here's an example using `ifconfig` to find out what your MAC address is, the command used here is `ifconfig -a`.
The MAC address in this exmaple is `60:57:18:31:ab:5a` shown after the `ether` property.
```bash
wlp2s0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 172.17.25.138  netmask 255.255.255.0  broadcast 172.17.25.255
        inet6 fe80::7eb3:fea9:bb3:ecb9  prefixlen 64  scopeid 0x20<link>
        ether 60:57:18:31:ab:5a  txqueuelen 1000  (Ethernet)
        RX packets 499884  bytes 208446448 (208.4 MB)
        RX errors 0  dropped 1  overruns 0  frame 0
        TX packets 142416  bytes 28168977 (28.1 MB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
```

#### Using ip
Below is the output from running `ip link show`.
The MAC address in this case is `60:57:18:31:ab:5a`, under the `link/ether` property:
```text
3: wlp2s0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc mq state UP mode DORMANT group default qlen 1000
    link/ether 60:57:18:31:ab:5a brd ff:ff:ff:ff:ff:ff
```

## Format

### Hexadecimals
MAC addresses are 6 bytes (48 bits) of data represented as a hexadecimal:
```text
1C-B7-2C-B9-27-09
```

### OEM & Unique ID
The first 3 bytes in a MAC addres is issued to the Original Equipment Manufacturer (OEM) to assign to the device.
The last 3 bytes are unique to the device which are created and assigned by the OEM.
For example in the MAC address `1C-B7-2C-B9-27-09`; `1C-B7-2C` would be the part issued to the OEM to assign and `B9-27-09` is what was created and assigned by the OEM.

## Spoofing
Although the MAC address for your device is basically hard-coded into the network interface, modern network drivers will typically allow you to change the MAC address temporarily.
Please note though that depending on you network adapter and drivers that you are using, this may not work.

### Linux
This is easy enough to do on Linux by turning off the interface, changing the address to what you like and then starting the interface again:
```bash
# find the interface to change the address of, enp1s0 for example
ip link show
# bring down the interface
ip link set [INTERFACE] down
# set the address
ip link set dev [INTERFACE] address [MAC_ADDRESS]
# bring the interface back up
ip link set dev [INTERFACE] up
```
You can go through the same process to reset your MAC address to its original value, otherwise you can just restart the system.

### Windows
PowerShell is a great tool for modifying your MAC address temporarily.
Be sure to take note of your current MAC address before changing it, or else you will have to restart your computer to reset it.
First we can find what network adapters are available and then change the MAC address accordingly:
```powershell
# find available network adapters
get-netadapter
# update the network adapter, refferring to it by its Name property
set-netadapter -Name "[ADAPTER_NAME]" -MacAddress "[MAC_ADDRESS]"
```
To reset your MAC address on Windows to its original value, you can use the same method as above, or by restarting your computer.

### Why?
Changing a devices MAC address can be used for bypassing or "tricking" access control in place by disguising itself as another device.
This is typically a technique used for malicious purposes but can be used for penetration testing and ensuring your services are robust enough to not be susceptible to this.

## Tasks

### Find Out About Your Current MAC Address
- Find the MAC address of the current device that you are using, remember you can use `ipconfig /all` on Windows and `ip link show` on Linux.
- Use the first 3 bytes of your MAC to find out who manufactured your network interface card (NIC), usually just putting it in a Google search will show you this.

### Change Your MAC Address
- Make a note of your current MAC address.
- Change your MAC address to the following: `00-10-18-57-1B-0D`
- Reset your MAC address back to its original value.
