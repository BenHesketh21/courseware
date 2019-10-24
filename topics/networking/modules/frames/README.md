# Frames



<!--TOC_START-->
## Contents
- [Overiew](#overiew)
- [Incoming and Outgoing Frames](#incoming-and-outgoing-frames)
- [Frames Traversing the Network](#frames-traversing-the-network)
- [Cyclic Redundancy Check (CRC)](#cyclic-redundancy-check-crc)
- [Tasks](#tasks)
	- [Viewing Frames with Wireshark](#viewing-frames-with-wireshark)

<!--TOC_END-->
## Overiew
Devices on a network send and receive Packetized Data in discrete chunks called frames.
Frames can hold a maximum of 1500 bytes, or 12000 bits. Whilst it won’t be necessary to remember this number exactly, it is important to understand that frames cannot hold a lot of data.
For instance, if an MP3 file is 4MB, that is 4,194,304 bytes. This means that lots of frames will need to be transmitted to transfer the entire file.

## Incoming and Outgoing Frames
Data comes down from applications, such as a Web browser, and into the Network Interface Card (NIC).
The NIC then creates a frame, using this data, and sends it into the network to reach the destination device.
Incoming frames from the network are first checked, to see if they are intended for the card.
The data is then processed for the application running on the system and sent to it.
All used and unwanted frames are discarded.

![Incoming and Outgoing Frames](https://lh3.googleusercontent.com/NpIQqDTiCzRZSeTXQ3j8N5832ewq2DKz559cwyYNfxU0WWo7UN1groARYNZwgaj-y-G1MTZcE13HzNQPQ4cyeRFUdOqgpFukLzsdYT8YtK4Zh07hojC_pS7ncQCiUhnDr5vCc_dSbC1kFfTcON5HJZcLePtZDzXS9SBoywxPUBHpIuIjAN19X2Fk3dk01MAOoxqwo_WhM2QLntbl97PuuAnRTxeBOUU6ENgks5D8nXPDMs4yxSb1IcJs4rx1fA_yUMvKW_LyOaAVGadM6gELWpQ95rhlVw94Y2qnMY5uVAEFZsXRG6H9z8XT_boip_pFJfmfcZWAQ1IBu-uC-7dQ7OWL3fhzGc_xQFJc8mTlK7lFZTzGwXgQJoG_sXoEwIomj6n9u-rBt9dfcFC26lY3Q-sHwrytCofzuhFAwUuVkLoxXb-QvCxJs1wVHLJTKjxOIuvWFxN5p0tdWdI79hOTZ6oKJnLm67cJTzaHnOgIdLXUkTirfSV7s-IMtjCz2E9ZFsKJgSTsLOC5IohYeFcFPfGE4_C8Nm1rhs9DSrQIVT8p0YYuXCxtT7s89__PZoal880KPnNgEKmp1dBJ6JRXUrcI97gSahP_wPIEJ0PRQlsputAhH5C15O2gV25BGTYiuyQkl5QI43JBa3ogiuYmVbH3OLiIgNiPumnVG7MjXAA8xi1xv5pGD6Z4ZuPCYQbyJWLv0-olmu8EgMQO2XLzzQ7OKwTK6zzeL4Y4D-loIxiLLspD=w716-h484-no)

## Frames Traversing the Network
With a hub, outgoing frames PCA are relayed to all devices on the network. Included in the frame is the physical address of the sender and the target.
All devices will check the frame, to see if the physical address matches their own.
If the target address matches, the frame is processed. If it doesn't match, the frame is discarded.

## Cyclic Redundancy Check (CRC)
CRC is used as a way to verify the integrity of the data being sent in the frame, and to ensure that it hasn’t been corrupted.
CRCs are a part of the Frame Check Sequences (FCS). All frames that are traversing over a network are in danger of being corrupted, or damaged, by interferences on a network.
FCS can use CRCs to validate the data that has been transmitted. CRCs work in a similar way to checksums; an algorithm generates a number or string of text from a piece of data, and this algorithm can then be used to confirm the frame's integrity when it's received.

![Cyclic Redundancy Check](https://lh3.googleusercontent.com/UaSVzouzhqyIat8pqoGfH_3mHy1-MBV3Fu0Y6xzC1y4yM8yWMgD8FvFgd2952s3ce1D7nGN-jIEuKms1XjwCB8fVQJRLblrZ2V5vdamEFQzU_SRzS90_ObvigD3QpLlFlGJ0kOTMVyb8ZNMpgzdyF5IUKdqaScshibwT8B8Uu2sT_jNiMcS3HhKUq6M0KUZKim4Dk0vtcmASNzP7DtT4zau4X4tk1mZ9CvxTDqQ9x2qsiCFIoMQtlYsCkxNi_qWXQru0de1y4yeeVmK7obeDYm04kKCTJcznPRk3l0gdn9_xWx6FnrRH7Tkss42Vvit98cB_2kPCPY0G6a1DQaDyGcFEyggbw6K7foxdMNFerr5Rfh_YzYCTmjeAr6xmHClWt5f_U2KXgYaBLU2lrApBrGNU57Wm4_5I0bITzkA-dRCOx4bTG9d1kY5hKT6T8UL0ThMXW9YQL3LdwyDv5hAAOCXUhflEqxytwEM0fp6qOEp5xvZL_JdlNe2P8DjuICTLXBZ3RXCIIrqzUKLAAGHfgb_VaGyYy_GviC0534GQdAIdHTZS-QOy252Gpbn8PxSMDWLCxx6ADpldW7--g8_QtunlerwNV4ILXM9tqyXXPVVla5OKGBd-jLEg1Z3JFkK2gts7OegiM-I1uKKxGdR8A3mvgpZZfL0jxPz1azt6sPj1nBpjBvbfZPSFE_2hqjohLm0zL07OipEOpptUxZSyMdlou-kaAS2ERLkLmGBnfCpgGDvd=w1278-h411-no)

## Tasks
For the task below you will need Wireshark installed.
If you are unsure what Wireshark is, how to use or install it, please have a look at the [Wireshark Introduction Module](/topics/wireshark/modules/introduction)

### Viewing Frames with Wireshark
We can start by running a scan until some packets come in.
Once there are some packets there, you can stop the scan and click on one of the packets.

![Wireshark Frames](https://lh3.googleusercontent.com/dibVkV243q_w-BgH7Iwv4-55mJ--drOww0I1EQct98MR7l8sOH47hYx-LFpMm2Lm79d6Vsb8sBdvawUzSNf4bZPt1A-fk2lLwwhmVBUzPnnZzlv1rWxqUz0EXwrbaGa5-krA_PPBR9v3EIEzMe4TyRQEB4Zq16-C3ma7znaNSpz1sPlwfTrcY05JQ0U9cLFzBiBkCg0NXuBEvLm3kuDyGcO1A996ZfyNHLDK2Ngck6nLvBw5OGqCNuCINQlQUtwaPgwl13DV_zOUG8aSfHJIoUkHmZee8_7hoiH61d_10Lhgh6DjRhDX0SBbmJ2rqe6IMyJUxnzeewI2zWFzWAS2YGV0OW7xttHgBAlQIzrYdZ7vlHHsYje4Qy3Eli3uiwOCL7LMzPJyKhka8bKRTpKhude50RUYfP2Ymx8haT6jsCxZ_21iiNWafe1vqDA1QOBFT8jxXyUP0DgJCftPqBnJMgWJ5MXZ5ff3RaBn6bfz4X0FdRDUBgcwmtc-nvfBy_XtACdwVC_70tg8D6KB_AuxxBATmgBO-pAI_a4bZzLftfNtj9ZnDaXYFQ_SngdQwiwdDasrXCv115cTAxR2stiZBXWG6Yi6t1dRB4BImBuFWOK35xDNaRRJTQbwjc11ZF7ii0stdKlzywmyPLEn9OFmdmCRBwR_S23sbQcmvWqivM8xwf4WVj3AFeJOCzsY_NjcvwzjEYwjj6ycgax7S34Z_EVTywHFtAfEBgGkE571F_RR8bba=w1102-h430-no)

- In the bottom window pane, you will see the frame contents
- In the middle frame is properties about the frame and protocols being used in that frame.
- The example above shows properties for a TCP packet over IPV4
- You can expand the `Frame` drop down to see frame properties
    - The CRC is removed by the network interface before being sent to Wireshark, so this won't be visible
- Under the `Ethernet` section is information about the source and destination addresses.
