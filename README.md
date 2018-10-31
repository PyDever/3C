
<img src="https://github.com/PyDever/AirCat/blob/master/img/3c%20(1).png" width="250">

 [![Build status](https://ci.appveyor.com/api/projects/status/pjxh5g91jpbh7t84?svg=true)](https://ci.appveyor.com/project/tygerbytes/resourcefitness) 
[![Coveralls](https://coveralls.io/repos/github/tygerbytes/ResourceFitness/badge.svg?branch=master)](https://coveralls.io/github/tygerbytes/ResourceFitness?branch=master) 
[![License](https://img.shields.io/badge/License-BSD%202--Clause-orange.svg)](https://opensource.org/licenses/BSD-2-Clause)
<br>

# AirCat
Send your AirCat through the sky to prowl around 
and give you some information. 

* device addresses
* port information
* OS and device details

## Installation 
Make sure to have `scapy` installed already.
```shell
$ git clone https://github.com/PyDever/AirCat
```
Run this command in Linux (VERY IMPORTANT):
```shell
$ iptables -I OUTPUT -p tcp --tcp-flags ALL RST,ACK -j DROP
```
```shell
$ python aircat --help
```

