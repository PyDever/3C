
import sys
import datetime
import optparse
from scapy.all import *

# function to parse command line args
def get_arguments():
	parser = optparse.OptionParser()
	parser.add_option("-a", "--access-point", dest="access_point", 
		help="Your access point (AP) or default gateway")
	options, arguments = parser.parse_args()
	return options

# some constants for packet parsing later on
SYNACK = 0x12
RSTACK = 0x14

# carefully craft information-grabbing TCP-SYN packet
options = get_arguments()
ap = options.access_point

# notice we spoof the source address as to prevent
# your access point from back-tracing

# attempt reverse DNS lookup
hostname = ''
try:
	hostname = socket.gethostbyaddr(ap)[0]
	print("\n-> Reverse DNS lookup yields: %s for %s" % (
		hostname, ap))
except:
	print("[!] Reverse DNS lookup on %s FAILED!" % ap)
	hostname = ''

if hostname != '':
	print("[*] Starting SYN scan on %s..." % hostname)
elif hostname == '':
	print("[*] Starting SYN scan on %s..." % ap)

for i in range(1):
	# spoof ttl to prevent reverse-OS-fingerprinting
	ip_header = IP(dst=ap, ttl=20)
	tcp_syn_header =TCP(sport=1500,
		dport=i,
		flags='S',seq=1000)	 # spoof TCP sequence
	tcp_syn_pkt = ip_header/tcp_syn_header

	syn_ack_pkt = sr1(tcp_syn_pkt, verbose=0)

	# sniff the SYN+ACK response for information
	if syn_ack_pkt.haslayer(TCP):
		pktflags = syn_ack_pkt.getlayer(TCP).flags

		if pktflags == SYNACK:
			print("-> Found OPEN port %i " % i)
		else: pass

	tcp_rst_pkt = IP(dst=ap)/TCP(sport=1500, 
		dport=i, flags='R')
	send(tcp_rst_pkt, verbose=0) # close connection

tcp_syn_pkt = ip_header/TCP(sport=1500,
	dport=80, flags='S', seq=1001)

print("[*] Scanning for AP's OS...")
try:
	syn_ack_pkt = sr1(tcp_syn_pkt, verbose=0)
	table = [[64,5840,"Linux [kernel 2.4 or 2.6]  "],
			[64,5720,"Google Linux                "],
			[64,32120,"Linux [kernel 2.2]	      "],
			[64,65535,"FreeBSD					  "],
			[64,16384,"OpenBSD [AIX 4.3]          "],
			[128,16384,"Windows 2000/98/95        "],
			[128,65535,"Windows XP                "],
			[128,8192,"Windows Vista/7            "],
			[255,4128, "Cisco Router [IOS 12.4]   "],
			[255,8760,"Solaris 7                  "],
			[64,65535,"MAC                        "],
			[128,254,"Windows 10/8.1/8.0          "],
			[64,0,"Linux [version,distro?]                     "]]

	OS = ''
	for OS_X in table:
		if syn_ack_pkt.ttl == OS_X[0] and syn_ack_pkt.window == OS_X[1]:
			OS = OS_X[2]
	if OS == '':
		OS = str(syn_ack_pkt.ttl) +''+ str(syn_ack_pkt.window)

	print("-> Found ttl,window pair: %s:%s" % (
		syn_ack_pkt.ttl, syn_ack_pkt.window))
	print("-> OS assumption: %s" % OS)

except:
	print("[!] AP OS scan FAILED!")

mac = ''
print("[*] Scanning for hardware address...")
try:
	arp_header = ARP(pdst=ap)
	ether_header = Ether(dst="ff:ff:ff:ff:ff:ff")
	answers = srp(ether_header/arp_header, timeout=1, verbose=False)[0]
	for element in answers:
		if element[1].psrc == ap:
			mac = element[1].hwsrc
	print("-> Found AP MAC: %s" % mac)
except KeyboardInterrupt:
	print('[!] Quitting...')
	sys.exit(0) # quit with no error 
except: sys.exit(1)

