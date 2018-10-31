
import sys
import datetime
import optparse
from scapy.all import *

# function to parse command line arguments
def get_arguments():
	parser = optparse.OptionParser()
	parser.add_option("-i", "--interface", dest="interface", 
		help="802.11 Wireless Interface")
	options, arguments = parser.parse_args()
	return options

# packet handler for sniffer later on
def packet_handler (packet):

	# check for the Dot11 datalink layer
	if packet.haslayer(Dot11):

		# check for packet type
		if pkt.addr2 not in ap_list:

			ap_list.append(pkt.addr2)

			# display list of APs
			print("\n %s - %s" % (
				pkt.addr2, pkt.info))

# grab arguments
options = get_arguments()
interface = options.interface 

if interface == '?':
	interface = IFACES.dev_from_index(3).name

# sniff with packet handler from before
print("[*] Scanning for 802.11 access points...")
try:
	sniff(iface=interface, prn=packet_handler)

except KeyboardInterrupt as interrupt:
	print("[!] Quitting...")
	sys.exit(0) # exit and raise no error

