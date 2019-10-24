# Models



<!--TOC_START-->
## Contents
- [Overview](#overview)
- [OSI](#osi)
- [TCP/IP](#tcpip)
- [TCP/IP and OSI Visual Comparison](#tcpip-and-osi-visual-comparison)
- [Tasks](#tasks)

<!--TOC_END-->
## Overview
Models are used in networking as a representational and simplified way to give us a high-level understanding of the processes that are happening within a network.
The two most popular models that are in use are the **OSI Model** and the **TCP/IP Model**.
Both of these models have a layered architecture and provide similar functionalities.

## OSI
The **Open System Interconnection Protocol** model is a **7 layer model**, which is a generic, protocol independent standard.
1. **Physical Layer**
This layer describes what hardware is being used, such as **Ethernet cables, hubs and repeaters**. As the lowest layer of the model, it is ultimately responsible for the transmission of data bits from the source, or sending device to the receiving or destination device.
2. **Data Link Layer**
The Data Link Layer checks the data obtained from the physical layer, to ensure that there are no transmission errors, and packages the bits in data Frames. Physical addressing schemes are also managed on this layer, such as **MAC addressing, switches and bridges**. Because this layer is so complex, it is often divided into two sublayers for more clarification; these are known as the **Media Access Control** and the **Logical Link Control** sublayers.
3. **Network Layer**
The concept of routing is introduced here in the network layer. When data arrives here, the source and destination addresses will be examined to see if the data has reached its final, intended, destination.
If the data has reached the correct destination, it will be moved on to the transport layer. If it hasn't, the destination address will be updated and sent to the lower layers.
Routers are used on this layer. As an example, if there is a port forwarding rule to send all incoming TCP traffic on port 8080 to a device on the LAN, the destination addresses will be updated with that of the local device.
Routing is supported on this layer, by maintaining the logical (IP) addresses on a network and mapping them to physical (MAC) addresses.
This is accomplished through using the **Address Resolution Protocol (ARP)**.
4. **Transport Layer**
The two most well-known protocols that are used on this layer are **TCP and UDP**. Other protocols that are on this layer may be used, but only for specific devices. They offer a range of other optional capabilities, such as support for re-transmission, flow control or error recovery.
5. **Session Layer**
The session layer is where connections are maintained and recovered in the case of lost data or connection interruptions. Session orientated communications can be compared to when you talk to a person using a mobile phone vs using a walkie-talkie. With a mobile phone you have to make a call, and the other person must accept the call. This connection is then continued until one of the people on the call hangs up, or there is a connection time out.  When there are connection interruptions on the call, such as someone going through a tunnel on a train, if the interruption isn’t long enough for a time out, the connection will be re-established. However, when using walkie-talkies, there is no connection established, so you would simply talk in the device and hopefully the person with another device on the same radio frequency hears it.
6. **Presentation Layer**
This layer is not referred to as often and is the most simple of the 7 layers. The presentation layer’s role is to make sure that the data is formatted correctly for the application layer. This is includes format conversions, and the encryption or decryption of data to support the application layer.
7. **Application Layer**
This is where network services are operating to supply services to the end-user. Most services are usually just protocols that are working with user’s data. As an example, the application layer protocol in a Web browser application will package the data, using HTTP, to send and receive web page content. Data is provided to and obtained from the presentation layer.

## TCP/IP
1. **Network Access Layer**
The Network Access Layer is the lowest of all the TCP/IP layers and is equivalent to the Physical and Data Link layers in the OSI model. This layer is where details of how data is physically transmitted throughout a network are defined.
2. **Internet Layer**
The Internet Layer is equivalent to the Network layer in the OSI model. This is where data is put into data packets, known **IP Datagrams**, which contain source and destination logical addresses. The information from these packets can be used to forward the datagrams between different hosts and across vast networks. This layer is also responsible for the routing of these datagrams.
3. **Transport Layer**
The Transport layer is equivalent to the Transport layer in the OSI model. The main purpose for this layer is to allow devices to carry on a conversation. Two of the main protocols that are used on this layer are **TCP** and **UDP**.
4. **Application Layer**
The Application layer is equivalent to the Presentation and Application layers in the OSI model. The higher level protocols are included on this layer, such as **HTTP**, **Telnet**, **SSH**, **FTP** and **RDP**.

## TCP/IP and OSI Visual Comparison
Here is a diagram showing how the layers between the OSI and TCP/IP models relate:

![OSI & TCP Comparison](https://lh3.googleusercontent.com/Kk1yl6jxDdDawh4UUEFlxjUyb3NkjI9A39ExIoDriff6cRr2_2noL0zgIz1p6zt1nfrkKcH3mtnIX_6e07g4wIa5StrKMvUO4419CFhjjSML0UQfe4UiW1PMfNPEbHrPNu7DpUD8CkjYNE1BP2jEXa9drRGFaU8133uUH_HhBF9GCMtQBBns-L2t88g8AEGp_KFf49KVLYb59SnPoON7R4jm6ZhQz9BZCX6C9J7omSAeTYYm4hEP-qlJ-XRtd7BwQKe0lSmVSAixeC2gE30s-Eb7EmS_rA9ONGX09lRovj4agv-nDFONhZWputVhSUwlHc-CQo1RLkUz0bq4zls2YNJKw0tkPCgzXNTdjwCozEF5GHcXqe7dF33EAnF3QMs71-RVQQTKiEIMKU_AAkKCL3nY9O9Admiv_KCgyPojUtkQPoXvEAY647nNF4rbNu9siOrnDiJERHopj82Wt9a8pD17UtiG17CJIdLt3V9TWrC8_5qXp_mZdhdO46E3GrzqcgI0epcyRWJGHDsX0rirMUr_6BWb1nTpJQhEy646I01C7Rco7_eXQ0qXNdMyFLEuC1iWi9na4MuuGrdF21_Jwf3MWSVqiE7vM5kz-WTX4OfR_TN5BHb8gKoBXuGhVAe5YzcDFkbU95BxOXgkdM_PDY8QQ90YanfncLoLB8RhdEBHVJB1mDFRmMCGLGhSP4fYjeUsfvJIdIiVlDsCNuBIEa-4AGl4Y_gpzcMTHQ8PQrmjtvtQ=w1208-h752-no)

## Tasks
Have a look at this YouTube video for more information on this:

[![OSI and TCP/IP Model Overview](https://img.youtube.com/vi/i9RL5jD9cTI/0.jpg)](https://www.youtube.com/watch?v=i9RL5jD9cTI)
