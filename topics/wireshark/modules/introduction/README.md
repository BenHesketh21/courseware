<!--PROPS
{
    "estTime": 15,
    "software": [
        {
            "name": "Wireshark",
            "version": "3.0.3",
            "platform": "windows",
            "downloadURL": "https://1.na.dl.wireshark.org/win64/Wireshark-win64-{{VERSION}}.exe"
        }
    ]
}
-->

# Introduction



<!--TOC_START-->
## Contents
- [Overview](#overview)
- [Purpose](#purpose)
- [Installation](#installation)
	- [Windows](#windows)
	- [Ubuntu/Debian](#ubuntudebian)
- [Tasks](#tasks)
	- [Open Wireshark](#open-wireshark)
	- [Select a Network Interface](#select-a-network-interface)
	- [Filter Packets by Host Name](#filter-packets-by-host-name)
	- [Make Some Packets for Wireshark to Capture](#make-some-packets-for-wireshark-to-capture)
	- [Following the HTTP Stream](#following-the-http-stream)
	- [Anaylsing the HTTP Stream](#anaylsing-the-http-stream)
	- [Importance of HTTPS](#importance-of-https)

<!--TOC_END-->
## Overview
Wireshark is a free and open-source packet analyzer.
It is used for network troubleshooting, analysis, software and communications protocol development, and education.

## Purpose
- Network administrators use it to troubleshoot network problems
- Network security engineers use it to examine security problems
- Quality Assurance (QA) engineers use it to verify network applications
- Developers use it to debug protocol implementations
- People use it to learn network protocol internals

## Installation

### Windows
There is a setup utility available for Wireshark on Windows.
You download it from [here](https://1.na.dl.wireshark.org/win64/Wireshark-win64-3.0.3.exe) then run the setup.

### Ubuntu/Debian
Wireshark can be installed via `apt`:
```bash
sudo apt install -y wireshark
```

## Tasks

### Open Wireshark
You can open Wireshark on Linux by running `sudo wireshark`. On Windows, you should be able to find it by searching for `wireshark` in the start menu.

### Select a Network Interface
Wireshark will list the available network interfaces to monitor.
You will need to select the one that you are using to connect to the internet, by double clicking it.
If you are not sure which one that is, here are some points to consider:
- If you are on a wired connection, the interface to use will likely be called something like`Ethernet` or `enps01` on Linux.
- If you are on a wireless connection, the interface to use will likely be called something like`Wifi` or `wlan0` on Linux.
![Interface Selection](https://lh3.googleusercontent.com/WF_XlRG_wy53COd3ZSCBeOTogdCo4xICsjXqfjlR2Qyc3jKDLZ3ZHEigcOB5uzL0JloQTR8R16uN6HoFYAaCW9KVmNH4zh8VMI2e08kiM_9c9mUXClcKgNJtE3bF0n8mWdbEmAgEjOsVFFclthV-fyWvTGdI9uAc1itWzr3C4so10fY4m9OFfaJFgLnMZGZJLbbwsMwCrg910ceY74CF1L4ihdSq8mVlpGen6qeyFUAdgch3ZiC0s-n5gp3NRm9r0VkVtndy6Fp6uT0uvPKQnRjjgqfi2GvlWLAz0RomX_kCSMPRw42qi2DpA7rtCTkG4QvJNvOgIe5_pU9gagq_bUbAfo66rT_kd_qMmIgV9tvaQ0X-Wcizk9QSBDUttxmduzkwWJ3Fpei8_V0shNnLMS5eH9RnqgOZwNMdSVq6bYOWFl26IbVFqeftpi5RLlClUNx0VhxLZklLUgzMRuBIn2yWyPU4mi18SFL_C0M_cK6A0-EZFi-cv2W1VRUTOAFAEMp_N8PIwkmkXDQSXdWT7ZhsWqCBK_8pZLJFJooK3DOnntcd1Ac7fN-lNEukWV27lx6EtEiNFuST_HK_N4n79fxy6FIM8-SeVk3cLGqy_1F6BSZ4D83dQcHvrj7jymKZ4gGE2nGp5wuFFD1H2aS3Q1h1tgWA4HaIjcwnEl9X8dU4MTEQTRA5TPEltTPmf-wOrH9KjbisUkogSUh1kNQhN2JrfYbAgxHWzC8eKOWHTsTkiFbl=w903-h417-no)

### Filter Packets by Host Name
You should now see Wireshark recording lots of packets, which are flying around your local area network (LAN).
We will need to use the filtering tool to help us find what we want.
Set the display filter to be `http.host == example.com` and press either `Enter` on your keyboard or the arrow button on the display filter box.
The display should now be empty:
![HTTP Host Filter](https://lh3.googleusercontent.com/jAWTt1VhcdQ6bvsVHcENGHj6EjZVOeHKwJ4zGbK_6tMArVh6_ha3xxl2TxhxpBOoPK36zJ6CxBjVcAhnPDNfp6LVPhJNDSZgu_t66PgY5xw0mhvg006dqHY5DPBmPIk7dM9XZsDQVuikV7O_PUvzuuaWwHG7HHOznHhhSohzHEpM1lNrruM_AKu5jVjZMnHM31bWiAPFOWQIuNsIzoU6fob_RtKhMcHaGMUkEDyWwssv7LEgRft9l13j_L5jn8dafPp-s_STdC5zcvxhbcUY-HmO3ItudInfke6Hc1AdosHjASorACYWzixUz1XonP_SRHdtzrOMWDuCusnpYc56U9tjxANWBrRcoQN6g8QEAFyovib9oKDNcwLJao2wkXrbpUwVPQwiMscc4N6YQ22DjFfwCdoJn6Mob3DkRHwnVMh5yMdhWIXSveLEDVRF9aXHMpFmePavA5-qzPU0BelaNqrAEJ239NjXRi0GNY2HZiFEDL7yUzlh9hjGaDkOMN_GFNTcJKh1_OJJIIs1sas-7nsw3iPq3A6lxM9AAAxK1fTeKedwVqPt2w7mTAa-GJ1mitaGqygGOo8aVM-SQkAuWp7tDwdl1_2B_1S2I7F-QvF4s4Fw_xzxkQaiKWd6wpgb6Ry3-EIahtHE4VOq6SRRM89yCmaqqCKcoHrx9ce6Q5uv96vMB0ilthdUFZwv090i_fKQjleN3ZQFqqLIR4iS2n6jgUYka1_6fZfleI72QjmWjn4F=w929-h417-no)

### Make Some Packets for Wireshark to Capture
At the moment, the display filter is only going to show connections that are made to `example.com`.
Open [example.com](http://example.com) in your web browser.
You should now see some packets appear in Wireshark.

### Following the HTTP Stream
Packets transmitted over a network are tiny; we need to piece them together by following the HTTP Stream.
Follow the HTTP Stream by right clicking on the packet for `GET /`, then selecting `Follow` -> `HTTP Stream`.
![Follow HTTP Stream](https://lh3.googleusercontent.com/aazYyiTkX-uH1qTJx4KZefs6iw_dDN68kZVCSxSHmOFXltX30pr4pbxknrWW2fxzpaCiOqE-9LRY2zC8fvpjHKYks9mJB4BL2M_ZoeZl7RS6GhqkMGAQ-sx-qTJsH0Iga4g_-yjfceCYaCi3oex9wrr3JoDImLURyO95zp4yYT8N6x8tlOJFGNSljO5ag5oqEvyMeYx0Nsrr-RtoPZwV0oHN5ds9bZ9TGXHmXCzNpxQi-RJnCDnqE_IK1gf6V0RPPfQeLn4k_IUY-Vbmzov4bs0WjI3vUInCNznRYfQdPnO9jl3C18U39s4a0lsM-HRw0qdaFWgJGgvvn9ft_OY1qFn_cS08QjM3Q1E19pYJIQSIEnBFWSvES-UXeQ7XY5iFBjYu-igPnPL9_HopB97J98_svT-OAaUDGFG6MPBjyFT65L7OH_ed3cODr28SzVxLrbCYOo4U90-JG42YBjxnJw8mdbM0-KKuqOxDpRh19kgRveRbVC_gFs8M8fzFbq4zT_A2OEKQnEDqSxk0Wt7cfw2LeeVGZRKt6uaUQ2HcWcNefZCKSq4gRaZMfEjJUE1xod33dlxK95r3C-goFEOqY_ZTrS4e4F3degkRsI4OngO-G_VbJB1T6VZIPDcEOl9yePeNC_oGa4-920Cvw9HrbABo2ucNmTKxcgTuYT7yVFrik3YC7KnQa8-gtpwPnLjXK35B2yb3taEhOYHMumpmQBaJFh1oVA9BkCio8aWM25LVpQo2=w927-h522-no)

### Anaylsing the HTTP Stream
A new window should now pop up, containing the HTTP Stream for the connection that you made to `example.com`.
This window is showing us all the information about the connection, including what was downloaded - you should be able to see the HTML for `example.com`:
![HTTP Stream](https://lh3.googleusercontent.com/sSh_JjuzZFgGO1YgJc68SbrDTKWQvW7Hd7gQVw918Po-Bx0Bv3hGtRp2hatutIp1JVMou2FKkiGmI2IaIOLF5vJMwWMt2fb7PkeVEWSwgt9ZHOx1Nn8cAL3sRvLxhSj0FYqLvuCrobkhR1mS64c-svzh9WMpFSx7o2ibZmET54faQgvW0O_X7DRw0YNonv8t9YUEj1cUeJC6GTn5L-0oQZXeR21OqAWFzg1PgIkgGwbjxxdBu4vCjj-jzPlxWnmCyjVLXzkpaqpBec7XckPFajR67oNSSyr9fkj0SXQJ1fh4t7wr2zc-wkCkS7tz4n6atsS0e-b4u2kqkOKUgqMfV75Dt659b3kp_EnGP4SpMESaEvqeJdDbV51aREXqgvUWRwbn2Ztp11PjxNts7LvV5e_pzC8YjnnYFVTSKiVMo83VDNgcPqj2rTS9D7D3zl3fgpmbkfHKC4IzIq8sCzc9XuB54VR8cERHZNrc7Qd9hie63XvWGm7TO-dprcEWCenhL0jUqDkSKGppSfgi4B7cYNIROwu0VxOcV6MvJMAZI-peC0ruKDYldFERwEeQRRMdcwsq0welc_3Yd7y_rJ-F0-BYa8nbw0UGGqSv5fvgH1pL5ldWDZ11sV1n6WkmeH5wMVFmN_Tg_gd0GKVLYo0X5nkBix0G4DoGRC9xaVmtWdDfW--1lS4Rlgt5fZbrle_v2pLbOcpMLG3E8Lt1S05OnuX50Kelf_bXfrUYA9noSqv7WEza=w868-h1118-no)

### Importance of HTTPS
Notice that we connected to `example.com` using HTTP, and not HTTPS.
This means that anyone on the same network as you could have ran Wireshark as well, and be viewing this information.
Lets now look at packets that have been transmitted over HTTPS and see what difference there is:
- Close the HTTP Stream Window, seen previously
- Stop Wireshark from scanning by clicking the red stop button.
- Find out the IPV6 address of `example.com` by using `ping`. You can use `ping -n 1 -6 example.com` on Windows and `ping -c 1 -6 example.com` on Linux. The IPV6 address can then be taken from the output; in this case, the value is `2606:2800:220:1:248:1893:25c8:1946`:

    ```text
    Pinging example.com [2606:2800:220:1:248:1893:25c8:1946] with 32 bytes of data:
    Reply from 2606:2800:220:1:248:1893:25c8:1946: time=89ms
    
    Ping statistics for 2606:2800:220:1:248:1893:25c8:1946:
        Packets: Sent = 1, Received = 1, Lost = 0 (0% loss),
    Approximate round trip times in milli-seconds:
        Minimum = 89ms, Maximum = 89ms, Average = 89ms
    ```
- Enter `ipv6.addr==2606:2800:220:1:248:1893:25c8:1946` into the display filter on Wireshark, changing `2606:2800:220:1:248:1893:25c8:1946` to the IPV6 address you just got from running the `ping` command.
    ![IPV6 Address Display Filter](https://lh3.googleusercontent.com/JwQQm8tcKqO7O9W5XhHUomKQgl59fbQpa5_MtT6d-jklXfGO1Go5uikSU82a5NOIDamYdea_yBsRDSk6CXLyJHevarWOxb2LewhlScB52hBTvh3XykJNzGU9_VDAtCMPChpgovnbqbcZtE-aprfJWZ_vqmW11TJE7bspKRaDcNsyXQ8invnL8VO99WC3sYAX3vYagUBSY7AqB32tjNu_OBgUEkIq9BaPRnVK4heppD0ORpdMQieOK_lHnCmS0wM3rI7tNI4K5PGDIZAK9dlE5i_REbbR1U7_r_mN8fQJ89gUu-JYFMR5rEOWQ81KGOpwKG98If2JMvjO8Kfedu3RCKfZ1F07fehlI19V_zhm47U8LzUI8okSpcfoGb1WWQPsAQNklV9slZuD6qZN4Fvqjc1KliB0LBf0QAZWfGMTyEkqnht73azX4HFVjITt-RDAEbKExyVLVYTylnkKHkDkN72ggCG8ux-mP5G3gNr4GlzhsT1nIO2La7oxZflOKG37MHqvFiXPsvEKwZjX4lVD72iIwygYl9zrgC-rD9stv0RO5T9Zoe1twB6PZ6uKneZcedkr2lBfiapDZhlaRVjaO3FVmha9tGDyTAEntQVOxXaNacC5p5ibfsxavOEMRxLWq3HEd_Cn2NXqXptKnGXCyD8ow1dQrnRMKgHJJ9gqP51fYZm5DQBfs6b2KM5eio__thqSL4pzDiTa4BxZWfi8NAU7hN8TD50bXTCGWYc8AgMSlAxL=w810-h22-no)
- Run a scan on Wireshark again by clicking on the blue shark fin.
- Navigate to https://example.com in your web browser. You should see packets starting to appear in Wireshark
- Follow the TCP stream from `Client Hello`.
![HTTPS TCP Stream](https://lh3.googleusercontent.com/2GEtYKYbiUn28ilXzLTkIcYJQ64c6oeeadNzlPj6Ocd28RYOolJZ1IZjTeLXgVyxp1s0j4aIhfER6N8QDfNhxyuwcOlhqZxf5LxMeWATNodt7gDRQgx59GWOF-fej8eMsjc_LV3vidR0DV9mwsaiVT2XYtPkNoXLT03a0NJJ9ZGqF2Aw66lpXGkxQ0fekBkZpMs_Kq9sRqd9ze6aX4ewN5TwOirVFA7Gct5Vjlv2uwDZcyslRQqi8FGn4U87R6O4hVrG8NY6API9G8yG8lgbd-l_PeDyIsHIAvCtvMVXhgem-RvjeGvI9udEBrCZtaLGj_PFs85tpcNOBqFJ6TKz3ebbzQQKXvm5Pc6JZ5IOLcWMfGzOoyHTMxEYMxG-0yfmWs-QLbCSrUeYB0AO7Ca5PAa3ECNbps1bNcdCdc7nqDDQ2dhXgQH-CiSnccY3MpvYjJeP2nSvCQvyWi_hN0buPma1rHgD85lhSw94SPff0alkVqn4C5KaEJohWsfJP7ONi8wmWPiBV9ztZzuzL0RpZwQtkJXKhFPLDS77ZGhb5uihc7Yzb8a6IP9y-e5cWEyfc7kDYIoevQPyHocLV5wQfyvL53sRrLgjqaYpOQGaTJrEMRaGKS_6BhYPcRsIdoibwbpcZUV9RKZLGX1yOTRroFoijmUddUHjF3DQ9KN68p75qqL5CsZFrP1ilf3KZJoSUIhDNid-lAa47_blvoxHL7WrFWpymh-gSa03XdrKFEHaaNaG=w910-h650-no)
- You can see here that the whole stream of data is completey unreadable thanks to HTTPS:
![TLS TCP Stream](https://lh3.googleusercontent.com/haTm06zIEFxpct3_dO1TcAMAsyUuAXF36Hi5adCHcFlMRRI08rjDj94pElyD-VcLilTh6Ua-WgtSbvakl9w5x66KU-Gub17piBEjoB-z8gZO42ceIQxDdArED2SCiCgjgSA4Bv2lS9qeqeNz4AZ-cuaB_xTMP7eMEXg8L3wQ_zyDCrhbQuTIpkXN1LzimyoTZFrXgwjTV173aQjnkaLsc528_z1qqKAUgO-_txeQTv_u11e-fTsFHfA64yTjxZUtF6huzRqVnC1Nq7rPbKjaAolNLydCQaM7b8UXF-sctBAGrmIhpOo2SapojZUFa9j3IOOT91esdZOwnIZnwKAV1HYqf3aGKtgEGP5pIwXSZ9eeqlBQ2Zricbe_oLNLT4jYLsyEde66oARoQy8IbufalZhgm0_tTWp7vSlRO2VU7uxc3asdLdGRQx9aWAqK7IZqA0RjdnTCySU2taMnbhLrE90V6Cu7B1aBAwxqmNAddSAAAZGzGQPvLkuMeexbX7qb26pqQ_ESHsE2fBceKUslGn4t1LyYBAa8P79gEQ-0k5YKMmh3-hZnmPX8AoODBp3Gwawkq332Brw3q9vhwkBWspP7mBHASEuQi13RaoszOh0tXkrdQGjMCGmKP46l8BqDrV_vaXuvbm-r-d_EpGLIdPz4ql86PF0z6PSpI5gpC57zoKEBiurq8iMIMEZsFnbzWhAph4FwASuaSb_AHOco5Q0taramX1mTaxh8EAyrdqSSeMbp=w865-h1116-no)
