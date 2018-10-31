
import sys
import datetime
import optparse
from scapy.all import *

# function to parse command line args
def get_arguments():
	parser = optparse.OptionParser()
	parser.add_option("-t", "--target", dest="target", 
		help="Target IP / IP range.")
	options, arguments = parser.parse_args()
	return options

# carefully craft ARP ping packet with datalink access
options = get_arguments()
ip_address = options.target
arp_header = ARP(pdst=ip_address)
ether_header = Ether(dst="ff:ff:ff:ff:ff:ff")

try:
	# send the ARP ping packt crafted above
	print("\n[*] Broadcasting packet...")
	answers = srp(ether_header/arp_header, timeout=1, verbose=False)[0]

except KeyboardInterrupt as interrupt:
	print("[!] Quitting...")
	sys.exit(0) # quit and raise no error

# collect list of clients from answers
counter = -1
print("[*] List of clients obtained: ")
for element in answers:
	counter += 1

	# attempt a reverse DNS lookup
	client_name = ''
	try:
		client_name = socket.gethostbyaddr(element[1].psrc)[0]

	except (socket.error, Exception) as error:
		print("[!] Reverse DNS lookup FAILED!")
		print("[!] Displaying results anyways...")
		sys.exit(1) # exit and raise system error code

	print("%i) %s - %s - %s" % (
		counter, element[1].psrc, element[1].hwsrc,
		client_name))




