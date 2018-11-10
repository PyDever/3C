

import sys
import datetime
import optparse
from scapy.all import *

# function to parse command line args
def get_arguments():
	parser = optparse.OptionParser()
	parser.add_option("-f", "--filter", dest="filter", 
		help="Protocol filter.")
	parser.add_option ("-n", "--number", dest="number",
		help="Number of packets to sniff for.")
	parser.add_option ("-d", "--dump", dest="dump")
	options, arguments = parser.parse_args()
	return options

options = get_arguments()
iface = "Intel(R) Dual Band Wireless-AC 7260" # options.iface

Xfilter = options.filter
number = options.number
dump = options.dump

dump = int(dump)

def expand(x):
	yield x.name	
	while x.payload:
		x = x.payload
		yield x.name

def handle (p):
	network_layer = p.getlayer(IP)
	transport_layer = p.getlayer(TCP)
	time = datetime.now()
	if dump == 1:
		try:
			load = p.load
			print("%s  %s    " % (
				time, hexdump(load)) + p.summary())
		except:
			print("%s    " % (
				time) + p.summary())
	elif dump == 0 or None:
		print("%s    " % (
			time) + p.summary())

sniff(count=int(number), iface=iface, 
	filter=Xfilter, prn=handle)
