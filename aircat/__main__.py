

import ifaddr
import sys, datetime

from scapy.all import *

# declare constants
timeout = 2 # ms
OS_fp = False
OS = ''
IP_range = ''
interface = ''
usage = '''
Usage:

	To see this page:
		aircat -h (--help)

	To scan network and fingerprint OS's:
		aircat -os <IP range>

	For normal ARP scan:
		aircat <IP range>
'''


# parse command line arguments
del sys.argv[0]; args = sys.argv

if len(args) < 1 or len(args) > 2:
	print('[!] Length error.')
	print(usage); sys.exit(1)


elif len(args) == 1:
	IP_range = args[0].strip()

elif len(args) == 2:
	if args[0] == '-os' or '--os-fp':
		client = args[1]
		
		print('[*] Starting OS fingerprint...')

		SYNACKpkt = sr1(IP(dst=client)/TCP(sport=1500, dport=1500,
			flags='S', seq=1000), verbose=0)

		print('[*] OS information successfully retrieved.')
		print('[*] %i:%i' % (SYNACKpkt.ttl,
			SYNACKpkt.window))

		print('[*] OS table:')
		print('''	
			64,5840 Linux [kernel 2.4 or 2.6]  
			64,0 UNIX (Unknown version or distro)
			64,5720 Google Linux                
			64,32120 Linux [kernel 2.2]	      
			64,65535 FreeBSD					  
			64,16384 OpenBSD [AIX 4.3]          
			128,16384 Windows 2000/98/95        
			128,65535 Windows XP                
			128,8192 Windows Vista/7            
			255,4128 Cisco Router [IOS 12.4]   
			255,8760 Solaris 7                  
			64,65535 MAC                        
			128,254 Windows 10/8.1/8.0          ''')


		sys.exit(0)
	else:
		print(usage)

interface = 'wlp4s0'

# sanity check for arguments
'''
print('%s %s' % (
	IP_range, interface))
'''

# actual application code
# with command line interface
try:
	print('[*] Got IP range %s...' % str(IP_range))
	print('[*] Got interface %s...' %
		str(interface))

except KeyboardInterrupt:
	print('\n[!] Quitting...')
	sys.exit(1) # exit while raising system
	# exception code

# start to scan the network
print('\n[*] Scanning...')
start_time = datetime.now() 

conf.verb = 0 # actually start scanning
ans, uans = srp(Ether(dst='ff:ff:ff:ff:ff:ff')/
	ARP(pdst=IP_range), timeout=2, 
	iface=interface, inter=0.1)

# present the information weve found to the user
for snd, rcv in ans:
	try:
		print(rcv.sprintf(r"%Ether.src% - %ARP.psrc%"+" - "+
		socket.gethostbyaddr(rcv.psrc)[0]))	# should work for LANs
	except:
		print(rcv.sprintf(r"%Ether.src% - %ARP.psrc% - %s")) # should work for WLANs

stop_time = datetime.now() # stop clock for total duration
total_time = stop_time - start_time

print('\n[*] Scan complete!')
print('\n[*] Scan duration: %s' % (total_time))

