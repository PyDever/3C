
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

