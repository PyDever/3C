

import sys
import datetime
import optparse
from scapy.all import *

# function to parse command line args
def get_arguments():
	parser = optparse.OptionParser()
	parser.add_option("-t", "--target", dest="ip_address", 
		help="Target IP.")
	options, arguments = parser.parse_args()
	return options

options = get_arguments()
victim_ip = options.ip_address

def ping ():
	global victim_ip; host = victim_ip

	# build ICMP ping packet
	conf.verb = 0; ip_header = IP(dst=host, ttl=20)
	icmp_ping = ip_header/ICMP()

	# send required amount of ICMP ping packets 
	try: 
		start = time.time() # for tracking durations
		# actual code to send and recv. one packet using scapy
		reply = sr1(icmp_ping, verbose=1) 
		end = time.time() # stop the clock
		duration = end - start

	# catch any other exceptions or errors
	except: sys.exit(1) # raise error and exit
	# back to normal ping code
	if reply: # make sure the reply exists
		# here we parse the packet to read it 
		print("\n"+"%s ONLINE duration %f" % (reply.src, 
			duration))
	# reply does not exist, host offline
	elif not reply:
		print("\n"+"%s OFFLINE duration %f" % (
			reply.src, duration))
ping()

