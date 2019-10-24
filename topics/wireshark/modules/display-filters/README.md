# Display Filters

<!--TOC_START-->
## Contents
- [Overview](#overview)
- [Filtering by Protocol](#filtering-by-protocol)
- [Relational Operators](#relational-operators)
- [Filtering by Port](#filtering-by-port)
- [Logical Operators](#logical-operators)
- [Filter by Host & Address](#filter-by-host--address)
	- [IPV4](#ipv4)
	- [IPV6](#ipv6)
- [Filter by Network](#filter-by-network)
- [Tasks](#tasks)
	- [TCP](#tcp)
	- [Display Your Machine's Incoming and Outgoing Packets](#display-your-machines-incoming-and-outgoing-packets)
		- [Incoming Traffic](#incoming-traffic)
		- [Outgoing Traffic](#outgoing-traffic)
	- [Default Filters](#default-filters)
	- [Generating Filters](#generating-filters)
		- [Finding IP addresses by using generated filters](#finding-ip-addresses-by-using-generated-filters)

<!--TOC_END-->
## Overview
Wireshark's display filter is a bar located at the top, just above where the packets are being shown.

This is where you type expressions to filter the frames, IP packets, or TCP segments.

The screenshot below shows the display filter being used to only show packets using TCP:

![Wireshark Display Filter](https://lh3.googleusercontent.com/VtovFjwfL1fIKWCN8cZ1D_D_gM0sRlACU-Tj0aOGRDkuVj1MFb7fw5oS4qLkcWMXNwDvFumS546eKLJqwMGztwep24tC-DQKgp13lLVO1SRSATgNERooMwBDqc4d6E3GmLFkg56HekgIiAaFp46KUfhNMlHMm8r0zfqYlHmgzj9F5Lu0LMD8Umk_MKZrDW-n0GGVBQabe4pEx0nO2OBXbJxCzJqWzUd9f9czTTWNacs2XTj2nl3kQdMxmFyM4GJoZNAORRyj60PwT83RGyprUwDNnlTXGojOqsrMzktKbUCIpIre4nSZN8vwl_kfKr69p-GDO-DBt9dMHZh7dw2gg2hH8eqOZA5FPs1bwTcJJySrBRzWmFV1u6DW1RySHfFFglno2r3wzWMeyrG0rMLZBYDZiBNfvlMOOTLG_jK8WZ-fyFBQ367oUerKerL6GKwSWvP86VfA1YhZNwrjSQvIxmJAZCbeFpU5A0LJkyNnolOashFVHqIktURpgc2ZkeyJa_hjFvN3qzJ6upw9f7pi-TTnoIhT6BP8W70LpGHuxxb_NncEQj6_sHm0Ksfnv14hz5yraDRKliSTzx87l4izwMSL45neSozGzpR_8feTc3ouSTyoS5hoE1lRLLg4UEmtbvlkWOC_oN2qQLs-QGgWCVu52jcyBEsUtVCFUHKOC7QxGm2227d1uHG0XjIYLITYd_sIgDAUo3oG7lskrtL06Xcchpjf31N4Hovmo3Z0inFOBThP=w1168-h404-no)

## Filtering by Protocol
To only show a certain protocol acronym can usually just be put in the display filter.

It's important to keep the letters **lowercase** however:

| Protocol | Display Filter Value |
|----------|:--------------------:|
| Transmission Control Protocol (TCP) | `tcp` |
| User Datagram Protocol (UDP) | `udp` |
| Internet Control Message Protocol (ICMP) | `icmp` |
| Server Message Block (SMB) | `smb` |

Here's an example for filtering out packets using the ICMP protocol while a `ping` command to `google.com` was being run:

![ICMP Display Filter](https://lh3.googleusercontent.com/W1j_AtrwMCGBhr3yRUnMc50qgVoltCOT1AnFXXSU9U_8TcSsi1rXDsoPnKiAXxUllgfHsN4dXLB2Bq09aVvPfhwYKgCAQLDoa5hWNnEZ2nvc6HNSB1lZDafJl61jg-ZXwaaRXf687Fyi0viLOO5dUpJoy6IcabiMiKAUDmpjbVXrfg0E11sTT-rFXIF0ecanlyvQl0KsJyugNM3NpoYaDnXSQuhDfCfESy9wF7YHpsMXhadOCk27DVheYB5vEVHFH7GTEmEU8eBxXTI32edzXU14UN1wCUEBv4OqVUEmrt36SweGI1TJ8XW6rT70Zs5Dt1raERiZnLHwYAkG9axjn2SMrCtcXNC1fALajWJ-v5V42qJry_EEs-BLGhwwFPBSWnayEhOHHUHf7GjTVlLIW51ZfVNbdNB9tBkW9s6RNbO6KYXtKe7gtx4WXeDBIVNfy3CK0j8pHdvWDE6K4A6ghpv0a2Gn0ASYGtW13sU90VwR6zmwmYW57Cjm1R9c93amp3SzKoqHEYGJ5fH_qF-lHH7b0UGpLGXeu05K-plJ7lBWJPyOqSMk_2jGwki5hjr-vFMajJu0CrdfdfSD2gQGG-LsUZCgVUbtBS7jUhDeHpOrYpAW6GNNrZ8Gq3hGVlniI9pW_uN3TG8KPuHO47_KGhlWRRXoaiwyiTACFZL187_gveZGYwiTlnC53BA5L4nqzdLXhX1WJ4usBTdZeiBaOVZT8UT-HyAA1EBxeFOhi2eTPWHW=w1168-h339-no)

## Relational Operators
The operators here have the same logic as most programming language.

When the condition that you put into the display filter equates to true, the packet will be shown.

| Operator | Description |
|----------|-------------|
| `eq`, `==`     | Checks if the values of two operands are equal or not, if yes then condition becomes true. An example of this would be checking if the packet is from a certain host: `ip.host == example.com` |
| `!=`     | Checks if the values of two operands are not equal, if values are not equal then condition becomes true. You could use this to show packets **not** coming from port `80` for instance: `tcp.port != 80` |

This is an example of a display filter only showing packets coming from the same network (assuming your LAN CIDR is `192.168.1.0/24`):

![LAN CIDR Display Filter](https://lh3.googleusercontent.com/6CwjtGqMl4NkyBbg7vmK86Kl4G_Las0jBT55O4pRbRCLIqkGGJ2HyL5HmUMZWyTu4e1MQ63m5dLaXjlQJ3BFy-nk5NOStU-asvSoo_8vl3lW3Kg2x5eA6JR25pyOb72VyRj1yyh6JF7uwIWNPz4Ad0yZIxLzvIkEsAbOblv4UwuusxrVoKPosDqVad0ndkWthd-WWbhbW21m-wB3aM6z0vLrJ8oKwmVHejE_6fKg8WxlXc-56tp_kYVqHj2Wn0NAmPJZSSTsXUnKHOHvYvXxM1trL5UU0snyeDQ6EDZgCqbGMy1oeEcThQxOSw05GuL8OYS7yLm6nkPSz_6_VzQ5FteQBmpzEh1PqyGhAofMVSaCevCH764jn8SDNHWq0hBVQV9MpCbgTJk4LlQ7mu27J5PqrQb62oC_ifZir4OIApmp8RwMoy6ORsLeUgwvDUj0S9ogKM4LiunfwpQJfDv0dfujnBdmPl_E888jMzOrK6TNfhHl0kSzzJqftX9fR7iMDRC6W4BkQ2sWOuwKjPeCa_MWW1m7LZp5mcztXo7sWSOayTiQp6hoeYRtniDQWWwcLRrxJr-yh0tR0lCZRCJ3uKfMySLxuCHFvl3waw21WGFJuISKTMPlakdSdhR97GNiMWRLH_D3jR9fVlY2g4G8ieMwob8asaSDD7Fhlxh048gzpxhxPBvrjX3tifkcxWlkwvgdH4fJb6DRIF84KxULv4zA0QZizWsc0ubl2iG2MAyRKv8G=w914-h266-no)

## Filtering by Port
We can check for connections to a specific in-use port with `tcp.port`.

For instance, if we wanted to check connections on port 52036:

![High Port Display Filter](https://i.imgur.com/nz2P16e.png)

Wireshark also allows for testing multiple ports through a specific membership operator, `in { }`. Values within the curly brackets have to be separated with an empty space.

Here, checking for activity across multiple ports is very easy. Let's add another port (e.g. 51728) to the programs we're filtering connections with:

![High Ports Display Filter](https://i.imgur.com/KnBznnK.png)

## Logical Operators
Logical operators allow us to chain conditions to make much more complex and specific filters.

The operators are `and`, `or` and `not`:

| Operator | Description | Example |
|----------|-------------|---------|
| `and`, `&&` | Logical AND operator. If both the operands are true, then the condition becomes true. | Show only traffic on the LAN (192.168.1.x), not internet traffic: `ip.src==192.168.1.0/24 and ip.dst==192.168.1.0/24`
| `or`, <code> &#124;&#124; </code> | Logical OR Operator. If any of the two operands is true, then condition becomes true. | Show only SMTP (TCP port 25) and ICMP Traffic: `tcp.port eq 25 or icmp` |
| `!` | Logical NOT Operator. Use to reverses the logical state of its operand. If a condition is true then Logical NOT operator will make false. | Show traffic that is **not** TCP: `! tcp`

This screenshot shows the `OR` operator being used to show only TCP and UDP traffic:

![TCP or UDP Display Filter](https://lh3.googleusercontent.com/s7gigEWszpwt0APSZOQkmnKx3lrT3PIKTVXurtak5b8Cmns1tCXupkHebkeMnLE6UEruCNURqRffOVEuAm4D_CdGIB5l322zS64oRfXoH49o-WlPhOPMHxhAFYwjpSLKOmzjf2LXxGwA2Pfi4GhSKH6D0gUNuEBCKTWGmSr6lUbru6yLrdLvNYqsTPeN8xTbnUv8zoNDeDcCGi85kkWoRLnWLiNdh-tmyzR5zm2WwoJjieZj3ppKskV36Lg_alOG-bXWttS2LgMaa6nnIo-qz7dldXMTLt7lmQ_Tp3fNlkh1gmnu7CHhqAHTt3W3ga1qpiCMZXaj4mRr86MZqMAE84ovR5FVLsRQuDIjnUDMJlGhJe1qkNg92hHrbQTPAZ56E98Ag2C1Q3vcfUMXRgOh_TW0TeV8RwUh5mf2ioSS_rvkC5uYSuFJhDWpGUD0Hza0zKa-Jg9P6FAhdJ_M7C-LJ8neDAcJmK9Tq0l7BA73iX9-Lmesg9_425qCaf2mpTBq7G4nfPQYbRjWPqTQrxGi32kllDnWjL2SmFJPPriXf8H3sisGrbSmLMdyq8dnF-BA4Vd2owCG-ubg0WRj5unh_W9kJqedcyo-cZsDNWoDySbv3a3IR2QcUjfoNIV3PvJ1LDbEm-0hqdZnD0Cw8h--_ryYIe9WqvZ7NQFINe1LiI4hTA2YnFtw4MWMlivrdY1zN4Po9AujxCq3ezvJ07lM658GvBfX2_EfB2GXCxgOh4qKNUNH=w1165-h341-no)

## Filter by Host & Address

### IPV4
We can specify which host or address to filter out by using `ip.addr` for domain names like `example.com` and IPV4 addresses such as `172.217.169.78`.

This example will filter out packets for `example.com`:
```text
ip.addr == example.com
```
This doesn't have to be a hostname; we can use just a regular IPV4 address as well:
```text
ip.addr == 93.184.216.34
```

### IPV6
To filter by an IPV6 address we can use `ipv6.addr` to create conditions; this example will show packets for `2606:2800:220:1:248:1893:25c8:1946`:
```text
ipv6.addr == 2606:2800:220:1:248:1893:25c8:1946
```

## Filter by Network
The CIDR of a network can be provided in the display filter to only show connections on a certain network.

You may, for instance, only want to see the traffic on your **L**ocal **A**rea **N**etwork (LAN), or vice-versa.

To see only TCP traffic on a LAN with a CIDR block of `192.168.1.0/24` we can use the display filter `ip.src == 192.168.1.0/24 and ip.dst == 192.168.1.0/24 and tcp`:

![TCP LAN Display Filter](https://lh3.googleusercontent.com/Acx9D9IbLldO3xcxhO2uBkSvTHxSMAqOFN4PCwLbHoTQlBkL62SYu50pK4gxWUEylLBSYq6XpAZzZDprZaUBtO4A3C38y1pgMDdNrKk6dHS0mgHrNhoa_-XVLgSx9M6dFeWXXxuBrfbCrHU9-nFlsC0HHdoeVks3iseotT8xh0LbULIFerwMGSQhUUvekgjH-4GrMIPEjGhYmWHbOKb1h1O_Ya4pUy7m_GvvZqdpj8HQP4GquEDyddcvIbFjpf6dNsjhH7pv_uQdqR3IYgL4iTykMqrtkpcWR09B3Fc49gEoG2sIzFqcOkAGJoezOuJoCaqeK7Puyfyaf639sHRtxk4Nq_3IOPQiAWXd6mYrtxKC1BGJpJrHZg307vGiTNLmQRdbmzecMXVtiEBhZuWQUt7r6_atRO6Ur5rR9DRzn4opqsznPPv___hetoRN8b_IJKGauwi37RM3_Fgp_WoMnQT77_Tce3RKgspHIKhllTQ3mqSlMWTxQ21q41gmFu0qWZ8ZTb021gi61QQY5aNp9kV89B7r1iW9MUhA-4v-5M2yivPEXwU1fI6AomjMPlU83t_cLngMAbtFx7Esb_O8BFZn878pxKH1rfzjCMzKjuEBT-up1QLrplv3gPssErO6s8WoppupzUByfaR-ALLqI-YC6YQSiV3tAYGeYORfF_he0wZOP08OrGLrX8rmCHF5ZaE4fYvuuTmMIt27NHKQna1z46bBvaOOMrL3almL6fftOoqE=w1165-h302-no)

## Tasks

### TCP
Lets start by displaying only TCP traffic by using just `tcp` as the display filter:

![TCP Display Filter](https://lh3.googleusercontent.com/VtovFjwfL1fIKWCN8cZ1D_D_gM0sRlACU-Tj0aOGRDkuVj1MFb7fw5oS4qLkcWMXNwDvFumS546eKLJqwMGztwep24tC-DQKgp13lLVO1SRSATgNERooMwBDqc4d6E3GmLFkg56HekgIiAaFp46KUfhNMlHMm8r0zfqYlHmgzj9F5Lu0LMD8Umk_MKZrDW-n0GGVBQabe4pEx0nO2OBXbJxCzJqWzUd9f9czTTWNacs2XTj2nl3kQdMxmFyM4GJoZNAORRyj60PwT83RGyprUwDNnlTXGojOqsrMzktKbUCIpIre4nSZN8vwl_kfKr69p-GDO-DBt9dMHZh7dw2gg2hH8eqOZA5FPs1bwTcJJySrBRzWmFV1u6DW1RySHfFFglno2r3wzWMeyrG0rMLZBYDZiBNfvlMOOTLG_jK8WZ-fyFBQ367oUerKerL6GKwSWvP86VfA1YhZNwrjSQvIxmJAZCbeFpU5A0LJkyNnolOashFVHqIktURpgc2ZkeyJa_hjFvN3qzJ6upw9f7pi-TTnoIhT6BP8W70LpGHuxxb_NncEQj6_sHm0Ksfnv14hz5yraDRKliSTzx87l4izwMSL45neSozGzpR_8feTc3ouSTyoS5hoE1lRLLg4UEmtbvlkWOC_oN2qQLs-QGgWCVu52jcyBEsUtVCFUHKOC7QxGm2227d1uHG0XjIYLITYd_sIgDAUo3oG7lskrtL06Xcchpjf31N4Hovmo3Z0inFOBThP=w1168-h404-no)

### Display Your Machine's Incoming and Outgoing Packets 
For this part you will need to know what your private IP address is.

You can find your private IP address in Linux by typing `ifconfig` (in Windows type `ipconfig`) into a command window:

![Private IP ipconfig](https://i.imgur.com/Bn4GABx.png)

#### Incoming Traffic
You can display incoming traffic to your private IP address by filtering by destination `ip.dst`:

![Incoming Traffic Display Filter](https://i.imgur.com/ekZsmlN.png)

#### Outgoing Traffic
You can display outgoing traffic by filtering by source `ip.src`:

![Outgoing Traffic Display Filter](https://i.imgur.com/A2aUj5V.png)

### Default Filters
You can also click **Analyze > Display Filters** to choose from the default filters Wireshark comes bundled with.

From there, you can add and remove your own custom filters with the **+** and **-** buttons at the bottom of the panel.

Let's add in a filter for the TCP-only traffic on our LAN with the filter we looked at earlier.

After clicking the **+** button you can type in the details needed for the filter:

- Since you will only need to worry about TCP traffic, use the `tcp` filter.

- You also need to set the source `ip.src` and destination `ip.dst` to your private IP address.

Give the new filter a meaningful name. Since we're looking for TCP traffic going both to and from a particular CIDR (your private IP), this is relatively easy:

![LAN TCP-Only Display Filter](https://i.imgur.com/yTZB3Pi.png)

### Generating Filters
Any packet that Wireshark finds can be used as the basis for its own filter.

Let's try this out by right-clicking any packet and click **Apply as Filter > Selected** to see this happening:

![Right-Click Display Filter](https://i.imgur.com/NW7HoI7.png)

#### Finding IP addresses by using generated filters
This has a number of real-world applications.

As an example, let's say we want to get the IP addresses of the Spotify servers which some  machine is currently streaming music from.

We can start by opening a command window and typing `netstat -bn` to see all the ports which are currently open, along with the services running on them:

![Netstat Show Ports](https://i.imgur.com/DnQg6dm.png)

Spotify appears in this list a few times thanks to the distributed nature of music streaming services.

Luckily, we can plug all the ports which Spotify is using into Wireshark by using the membership operator `in {...}` we explored earlier.

This will filter to show all the traffic moving between Spotify and our machine:

![Spotify TCP Traffic Filter](https://i.imgur.com/iJ3s3ZG.png)

There are a few IP addresses flying around here, so let's make things easier for ourselves by first filtering in the conventional way.

Let's keep the port filter from earlier in place, but now we also want to restrict this filter to show only packets **received** by the machine (`ip.dst==192.168.1.154`).

This will give a list of traffic coming in specifically from Spotify servers:

![Spotify TCP Received Packets Filter](https://i.imgur.com/01fpgbV.png)

We can see that there are two source IP addresses in the list.

On one of these packets, right-click inside the **Source** column, then click **Prepare a Filter > Selected** to start building a filter.

For the second IP address, right-click as before, but then use **Apply as Filter > or Selected**.

The filter will generate itself in the bar at the top:

![Spotify TCP Received Packets Filter](https://i.imgur.com/g1Ht8kT.gif)

For longer and more complex filters, generating filters is invaluable.
![Right-Click Display Filter](https://i.imgur.com/NW7HoI7.png)
