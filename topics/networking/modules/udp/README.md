# UDP



<!--TOC_START-->
## Contents
- [Overview](#overview)
- [UDP Header Format](#udp-header-format)
- [UDP Operation](#udp-operation)
- [Tasks](#tasks)
	- [Viewing UDP Packets with Wireshark](#viewing-udp-packets-with-wireshark)

<!--TOC_END-->
## Overview
User Datagram Protocol (UDP) is connectionless and not as reliable a service as TCP. There is no acknowledgement of packet delivery, sequencing or even error recovery.
However, UDP does have a very important advantage over TCP - **speed**.
Higher connection speeds are always preferred, but sacrificing reliability can be a big issue (depending on the use case).
UDP is great for tasks that require data on demand or in real-time, such as audio and video streaming on conference calls or when playing online multiplayer games.

## UDP Header Format
Other than the data, there are four components to a UDP packet’s header. This is significantly smaller than the TCP headers, because UDP is more limited in capability.

1. `Source Port` - The port from which the packet was sent from
2. `Destination Port` - The port of the receiving device
3. `Length` - The total size of each data packet is stored here, including both the header and the
data.
4. `Checksum` – Similar to how TCP works, UDP checksum allows the receivers to validate
the incoming data for any corrupted parts of the message. 

![UDP Header](https://lh3.googleusercontent.com/g8GbrocvKB53cwpqiWtSqxgnmkdiUJMQOLsfd4gxkTf2Qq82nASrHXe2oTtMa_MVmzuuH33K0F8T7cNDunhBHnGKQQhmir5LyacyCWpPEQA63kZrPMSpYYKc4Ch_g_oMbpAqzXxv6iivDz7L0S64gP7cHyGCVndcpHtHie4hjGYhePBTtVr9SJ14w7eRB8tirtFFbOBRMuocYiUB-42wnNP3rOq6nUnqGwolgM5Sf9-P0YQfX7HipbyOcDcXTX42TKnvHrdnpHVndv6YIByhNKpRM-opAKrTbrbtfl6sEzlg5Ip-rZB-8QCf755dn-L2g1tYmvKoJHic_fs6ZOSj2K0Il3ybk5k-b5DhsfrQ1EOD3XJv8kCL-E4i1IriAIchgB_ZMM5EFBizbcE1FyZ4RLRnHJtVzLf7vuBzr9RMGi9W22vsm6ad_6K1-P1Z3WokXc4-a2nPyHvf_Fis9vldJ9WsdJeiKc-OBS2D7yk-rdQuwp_XRm_2uRae1_HET7RRcHjq9N45EOtA87OPJGVvXbPQkuLwtJCE4Alm3Fyec4zNzfDoVS4XVGwi1b9UkS33exSPOmTWnXhBB0kzwLJDSj83g6wRWuoE4LtmCXxbhBx-srU3XFCGdVRfTaJ7BU4aar20lkjIgqNgCfS-7c2nKS7pUBEixcdIfbIb8e8lUE08XS3vmDtT89tmfp5-dPNsEwqpYh73yFRNieu33IiXQifD50QDXX5uRVoWyrtZMMK1XYAE=w1084-h341-no)

## UDP Operation
Regarding the illustration below:

- Segment 1, 2, 4 and 6 are successfully received by the server and processed
- Segment 3 was lost in a connection interruption. There is no way of the remote server, or local machine, knowing that it should have received that lost packet. If this were TCP, the packet would have been resent to the server after a time-out period.
- The packet from segment 5 has been corrupted and the checksum validation fails when it reaches the server. The local machine does not know about this and will not resend the packet; it will simply discard it.

![UDP Operation](https://lh3.googleusercontent.com/kskI1eWHh67F2Nbh1raZeNNllsbIPdl9bh6bqC9_XKkRx3VHkE34ToBYZNsEjtlrfRog7vXYhrrJ5JEkDdfgEbgvp4V95F7f1PbbO3rxAiF8SC-d0zfv27lu5WJ-KGk-wQrDdXPiv9paqM5pnvONDSfOlwfmWSOzEdLJRx4vsG9oyQ6kxu3tEbhEy4ktU4DtGfhvohTSMx5hpVab4tP618_eacN8ji-8PpD3A6BIXIfZruxAus8prZyak0aTeChW2KeLoVL35PzH3_NRiH0d23ZrOaT-eZF7yD5Rf8pqyP4C4UAJRLP_HTu-a8z13NRSOaMezE7bB42GMImQA2GOnrjOvXaNhJEzAMuouVTg98NxFLJc4-0o-RkHjf1yqpDjVFahC6-lx7jxYhu_OTXsE5MnQQs7t8NVwOmCzEgRkvKAViRH4xNUgCe_IKO_L5Ys8CGEmiqZ7d9sUE81zRcE_tnHaK5sNneVxaIiXZLIp6KFeRkcCOQ4qZ1CkXGgXj70L-ZF6O79m22mjQmwvaewNu62LTNJRiNoDjQUou3Kf-wMK95vtQZd9Sm19x66RdZA32QonJPU_49rFaZccn4OaK3qcE5Q8vCek4-OlBglnokzcwL3keTP9qi1NYZpT1X9Z8nwmrsrG6k4uOQ9GKDZ1yx3oUwbvGyp18GbqddhXgFkHnUuJBD0Fd7gEnI4XgteKOuLIMvT-TyeEjHzNX3zP-ppwED-tkTR1Xxw8s46dXw3Fkt4=w725-h685-no)

## Tasks
For the task below you will need Wireshark installed.
If you are unsure what Wireshark is, or how to use or install it, please have a look at the Wireshark [Introduction Module](/topics/wireshark/modules/introduction)

### Viewing UDP Packets with Wireshark
- We can start by running a brief scan, until some packets come in.
- Add a display filter for UDP, by putting `udp` in the display filter box:
    ![UDP Display Filter](https://lh3.googleusercontent.com/uz5gxaGCQE_guHbfHo9MVM7onIM1qEmtdxzkHTFGRd8hWZHV_PS7KZtnJPcrrNnfJV8oTw2VWiIJ-EHAUfm7UmOPs4xMLseSpqFMCvJ1ELKmw2A4E2xhGnI7D7L0GxxVwFMSYveEqfI3V2NVO268dK6eLRMrGYXbiULBuPhSlCdamh4nefkOITf30Ih2272G-IiT0X5uYXVT9GgOpbHadJwsIDs8FWujTH8iAf5UvgjvH84Rg9OVXPrJB2N8Oc_Ljuy3br5GuGUMKHn8m9jaT9bIKTHihYp3WO4mSpwn-kymrA6rplz9DlKEbu7awkZk6xIH6yTqTStMO4H82Q8yPX5W1NA9nf0IBdeLG-qqCspeVKeM_oW_hfuI8Rf6Y6_WKigAOQ5McmIsQP5pZNeOK-YkkNePLSnTeb8ZbJXiHeJPIlcYhts88X3DkRLNQtVPoHGmAXfHUHVBjwVetBX-tgziDoib6IxCN7tSzHq-uK1bE1ubhxuzXbkLGn1JMtOk2hsYP5ncTAnIOTjg51XVCOE3i27MEtakh5UCFU-6-5wUol6rjnoL_UIVS1tg5S_m8WuTFbPMMzyrvn5xzMmVtgOz8A1gqK_lr5KDHlu9vVh09DFaS93PKER8DWZcUYhYM8nHT0NPW1Zr-Bd0MeqxshAK3pCCdn1aY91I0IsSrH-xhlvswZaiV9mHVv8BcvSXExYH0k_2Kv_6q-zkPQ5JoRvZX56jCWleZB4wpw4qqMVwflK2=w1116-h51-no)
- Once there are some packets there, you can stop the scan and click on one of the packets that use the UDP protocol
- On the middle window frame, select the `User Datagram Protocol` drop down

You should now be able to see information about the UDP packet. See how many of the properties shown in UDP Header diagram you can find here:

![UDP Data](https://lh3.googleusercontent.com/W0ZWp-urebN0f7nyIC17HpXW4IL3XT8WunCu3KH3-K3FL2pEYpmXT74yFVM7eSfdt6iWjH2JppSxqwy0CjmTfV-8Zn28P7tafGXi5aiMm41c30UITk3pQapeRSZ3ohGSkdDDtWeJFl27PLNGZw8cPVEEmhoDiPGyvLUsgthVLPjjXxP2CYdYtP2BKAyeW5yPcmDnOi1hkTcxG_wtfAfBFET1kkImZa9nnyRSoYrup8-BpRE-etXYVJ1Mm-8Fi6owjiEtQZV_yNySMekYmK4j4MHoIFxzanw85Q-k0lIikQ7eAwSbQVxUZoied57IHb0rSijkXznM5338NScibPDurik5CcdiQ9HuzOxIJHb1JmORRyHtMgMgswSLBmbe119qnQRbs4-iIymI3o4u4gC_yPkL1YXJVN4K7O3-k1LvqKlfbBj3KHGUMbJ9f5_Hv7k_2lv06rgretJBULdUSjw4zWZb0MLR6k1QRm4xKSpRRW8xYGifA1MGuQ_QnVJB-dNeYLHVJ0vrRXFKyDhViaWWu--WkiZbZvSAi9awKf_Vv1OvoskH1-rSgNMRPhMISD7YITCYtnZvVr1qJ5UD2qmHYl8wXYs3ECEH_ZmFb6edrnnCfW0xm9aR_O9Eml8JaVTTpzEai76RtwYXt7JQia-zAyfFaS5CzG-w96j8rsy30iA_UVa4Jiz2yMt4jevDJMzKZLsARVqhFNVIy5DySekNeA1LPvRFXDTlCvBwopkQ8dV68_p4=w1181-h1287-no)
