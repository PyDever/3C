
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

## Usage Instructions
For help, run `python aircat --help`. The following commands
are currently supported by your AirCat.

`python aircat <IP range>` - normal ARP scan to list clients connected to your access point or router.
`IP range` might look like `192.168.200.0/24`, which would return all 255 clients that are connected
to the `192.168.200.` subnet. It might be `192.168.300.0/12` which will display 130 clients that are
connected to the `192.168.300.` subnet. 

 `python aircat -os <IP>` - return OS of client `IP`
`python aircat --help` - show standard command line help page

