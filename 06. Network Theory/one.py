#!/bin/env python3

import binascii
from scapy.all import *

origPcap = './one.pcap'
origPkts = rdpcap(origPcap)
crtlPkts = rdpcap(origPcap)
origReq = origPkts[0]
origRep = origPkts[1]

origReqHdr = origReq.copy()
del origReqHdr[RadioTap].payload
origReqHdr[RadioTap].mac_timestamp = 894910388
origRepHdr = origRep.copy()
del origRepHdr[RadioTap].payload


dstMac = 'c4:d9:87:e4:64:5e'
dstIp = '192.168.100.148'
# pingerMac = '4e:40:cd:16:5a:1d'
# pingerIp = '192.168.100.136'
pingerMac = '4e:40:cd:16:5a:1e'
pingerIp = '192.168.100.137'

for pkt in origPkts:

    ## To-DS
    if pkt[Dot11FCS].FCfield == 1:
        pkt[Dot11FCS].addr3 = pingerMac
        pkt[IP].dst = pingerIp

    ## From-DS
    elif pkt[Dot11FCS].FCfield == 2:
        pkt[Dot11FCS].addr3 = pingerMac
        pkt[IP].src = pingerIp

    else:
        print('Missed something')

del origReq[Dot11FCS].fcs
del origRep[Dot11FCS].fcs
del origReq[IP].chksum
del origRep[IP].chksum
# origReq = RadioTap(origReq.build())
origReq = origReq.__class__(binascii.unhexlify(hexstr(origReq, onlyhex = 1).replace(' ', '')))
origRep = origRep.__class__(binascii.unhexlify(hexstr(origRep, onlyhex = 1).replace(' ', '')))

## Done
newPkts = [origReqHdr/origReq.payload, origRepHdr/origRep.payload]
wrpcap('solution-one.pcap', newPkts)
