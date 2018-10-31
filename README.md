
<img src="https://github.com/PyDever/AirCat/blob/master/img/3c%20(1).png" width="250">

 [![Build status](https://ci.appveyor.com/api/projects/status/pjxh5g91jpbh7t84?svg=true)](https://ci.appveyor.com/project/tygerbytes/resourcefitness) 
[![Coveralls](https://coveralls.io/repos/github/tygerbytes/ResourceFitness/badge.svg?branch=master)](https://coveralls.io/github/tygerbytes/ResourceFitness?branch=master) 
[![License](https://img.shields.io/badge/License-BSD%202--Clause-orange.svg)](https://opensource.org/licenses/BSD-2-Clause)
<br>

# 3C
3C allows you to dominate your access point. 
```shell
$ python 3C -t <IP range>
```

## Installation 
Make sure to have `scapy`, `wifi`, and `wireless` installed. Also, run `iptables` to disable
automatic kernel RST forwarding, or else `osfp` will be useless. 
```shell
$ git clone <this repo>
```
