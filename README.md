
<img src="https://github.com/PyDever/AirCat/blob/master/img/3c%20(1).png" width="250">

 [![Build status](https://ci.appveyor.com/api/projects/status/pjxh5g91jpbh7t84?svg=true)](https://ci.appveyor.com/project/tygerbytes/resourcefitness) 
[![Coveralls](https://coveralls.io/repos/github/tygerbytes/ResourceFitness/badge.svg?branch=master)](https://coveralls.io/github/tygerbytes/ResourceFitness?branch=master) 
[![License](https://img.shields.io/badge/License-BSD%202--Clause-orange.svg)](https://opensource.org/licenses/BSD-2-Clause)
<br>

***All included scripts are illegal to run without permission of target.***

3C gives you an arsenal of Wi-Fi tools to perform DoS, ARP poisons, and more. 
```
$ python scan -r <IP range>
```
```
$ python poison -t <victim IP> -m <victim MAC>
```
<hr>

### (v2.0 update)

***New feature!***
3C can now perform SYN flood DoS attacks.
```
$ python flood -t <victim IP> -p <port> -l <payload>
```
It will take out a port in about 3-5 minutes.

### (v2.1 update)

***New feature!*** 
3C can now perform Nmap-esk port/OS scans.
```
$ python map -t <victim IP> -p <port range>
```
Port range should look like `0-80` or maybe `22-1024`.
Here is a scan I did on my home router:
```
Starting scan on 192.168.200.1 at 2018-11-06 11:09:27.232626 
Scan completed at 2018-11-06 11:12:37.628803
PORT  STATE  SERVICE
80    open   http
443    open   https
OS scan: Linux/UNIX/BSD
Rev. DNS: gateway.ht.net
```

***New feature!***
`flood` is now multi-threaded. Refer to v2.0 update
for details on how to use it.

### (v3.0 update) ###

***New feature!***
3C can now perform detailed packet sniffs on local area network traffic.
```
$ python watch -f <protocol> -n <count> --dump <hex?>
```
the `--dump` or `-d` flag should be set to `1` if you wish to view
the data in the packet if any, or `0` if not. 
```
2018-11-13 09:30:20.153000    Ether / IP / TCP 52.184.193.103:https > 10.193.124.129:49819 PA / Raw
2018-11-13 09:30:20.372000    Ether / IP / TCP 10.193.124.129:49819 > 52.184.193.103:https A
2018-11-13 09:30:20.591000    Ether / IP / TCP 52.167.231.222:5280 > 10.193.124.129:50043 PA / Raw
2018-11-13 09:30:20.591000    Ether / IP / TCP 10.193.124.129:50043 > 52.167.231.222:5280 A
2018-11-13 09:30:20.919000    Ether / IP / TCP 52.167.231.222:5280 > 10.193.124.129:50043 PA / Raw
```
If you will notice, on the left hand side of the report, there is a very 
specific time stamp. Time stamps are often vital in traffic analysis.
If you enabled the dumping option, you might see something like this in between
the packts. It is a hexadecimal dumping of the payload layer.
```
0000  17030301582A3E7E6539F8CBFFC26597 ....X*>~e9....e.
0010  A8E9AE26611205C0DC88076B1990EFDD ...&a......k....
0020  9A6C780F03B6DA2682BE918E3160CC40 .lx....&....1`.@
0030  97FDDC66F834DBF38F7EACDC831D793F ...f.4...~....y?
0040  495B9C53F79CA4179DAC6BC51EAAC04C I[.S......k....L
0050  0D64ACCF19E4C18C3FC8829157986E39 .d......?...W.n9
0060  A8ACAE77F91CC4E8101B3ACDA25ECCFC ...w......:..^..
0070  AB7B5AE5C76FDF877FB8BEEEDDA51B3E .{Z..o.........>
0080  6962D931719488EF6502B583B393370B ib.1q...e.....7.
0090  AA0D4D89F853D79F9B07068F308A9129 ..M..S......0..)
00a0  CD1D152ECAFCF247B0EBBCC62BC55B55 .......G....+.[U
00b0  E3439D54DB3A724D66EC8EA74297510C .C.T.:rMf...B.Q.
00c0  9BC143D21ECDC44645A9B6A99685A769 ..C....FE......i
00d0  6574764C0780F3023C4EA6103CFE8290 etvL....<N..<...
00e0  A9E59046B9CA85AABD4E12691229D4B7 ...F.....N.i.)..
00f0  1E452403276414A8555472EA215EA80F .E$.'d..UTr.!^..
0100  FD55BB1B4808DEF38F2594E24E369E19 .U..H....%..N6..
0110  0383989DE9966FF13328CDCD7A404855 ......o.3(..z@HU
0120  CFA3AD3929F595605FC48A4489C2C02A ...9)..`_..D...*
0130  6398CECB8B2F419D9A66BC2D9DA435FB c..../A..f.-..5.
0140  459250622FCA0DC9B791532C8095D8DA E.Pb/.....S,....
0150  717FE2883B75145A02BFC61B21       q...;u.Z....!
```

## Installation 
Make sure to have `scapy` fully installed and tested.
```
$ git clone <this repo>
```

### ARP Poison Explanation
3C injects your access point with venomous ARP packets that kick the victim offline. 
```
                         (no connection)
You -----[3C_pkt]-----> AP -----X-----> victim
```

