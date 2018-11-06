import os
import sys
import random
import time
import shutil
import subprocess
import socket

# setup program flags
NMAP_INSTALLED = False
ARP_INSTALLED = False

# ensure that nmap is intalled
NMAP_INSTALLED = True
ARP_INSTALLED = True

# check variable and exit if nmap was not found
if NMAP_INSTALLED == False or ARP_INSTALLED == False:
	print("""ERROR: One or more programs not found.
		try:
			apt install nmap arp
			apt update
			""")
	sys.exit(1) # exit and raise error
else:
	print("SUCCESS: found Nmap")
	print("SUCCESS: found ARP")

# create nmap functions for pythonic use
"""script starts here"""

# discover hosts with 'arp -a'
def ARP_dis ():
	try:
		subprocess.call(["arp"])
	except OSError as e:
		# handle error
		print("ERROR: ARP scan failed. Quitting...")
		sys.exit(1) # exit and raise error

# resolve hostname from above output
def res (host='localhost'):
	return socket.gethostbyname(host)

# run a TCP-SYN scan over network
def SYN_scan (ports=(0,80), host='0.0.0.0', os_det=False, ttl=20, src='0.0.0.0'):
	try:
		if os_det == False:
			subprocess.call(["nmap", "-sS", "-p%i-%i" % (ports[0], ports[1]+1), host, "-ttl %i" % ttl, "-S %s" % src])
		elif os_det == True:
			subprocess.call(["nmap", "-sS", "-p%i-%i" % (ports[0], ports[1]+1), host, "-O"])
	except OSError as e:
		print(e)
		print("ERROR: Nmap scan failed. Quitting...")
		sys.exit(1) # exit and raise error

def CONN_scan (ports=(0,80), host='0.0.0.0'):
        try:
                subprocess.call(["nmap", "-sT", "-p%i-%i" % (ports[0], ports[1]+1), host])
        except OSError as e:
                print(e)
                print("ERROR: Nmap scan failed. Quitting...")
                sys.exit(1) # exit and raise error


# run a UDP-DGRAM scan over network
def UDP_scan (ports=(0,80), host='0.0.0.0', os_det=False):
        try:
                if os_det == False:
                        subprocess.call(["nmap", "-sU", "-p%i-%i" % (ports[0], ports[1]+1), host])
                elif os_det == True:
                        subprocess.call(["nmap", "-sU", "-p%i-%i" % (ports[0], ports[1]+1), host, "-O"])
        except OSError as e:
                print(e)
                print("ERROR: Nmap scan failed. Quitting...")
                sys.exit(1) # exit and raise error


# run a UDP-DGRAM scan over network
def XMas_scan (ports=(0,80), host='0.0.0.0', os_det=False):
        try:
                if os_det == False:
                        subprocess.call(["nmap", "-sX", "-p%i-%i" % (ports[0], ports[1]+1), host])
                elif os_det == True:
                        subprocess.call(["nmap", "-sX", "-p%i-%i" % (ports[0], ports[1]+1), host, "-O"])
        except OSError as e:
                print(e)
                print("ERROR: Nmap scan failed. Quitting...")
                sys.exit(1) # exit and raise error



# run a TCP-ACK scan over network
def ACK_scan (ports=(0,80), host='0.0.0.0', os_det=False):
        try:
                if os_det == False:
                        subprocess.call(["nmap", "-sA", "-p%i-%i" % (ports[0], ports[1]+1), host])
                elif os_det == True:
                        subprocess.call(["nmap", "-sA", "-p%i-%i" % (ports[0], ports[1]+1), host, "-O"])
        except OSError as e:
                print(e)
                print("ERROR: Nmap scan failed. Quitting...")
                sys.exit(1) # exit and raise error


def SVER_scan (ports=(0,80), host='0.0.0.0', os_det=False, ttl=20, src='0.0.0.0'):
        try:
                if os_det == False:
                        subprocess.call(["nmap", "-sS", "-p%i-%i" % (ports[0], ports[1]+1), host, "-ttl %i" % ttl, "-S %s" % src])
                elif os_det == True:
                        subprocess.call(["nmap", "-sS", "-p%i-%i" % (ports[0], ports[1]+1), host, "-O"])
        except OSError as e:
                print(e)
                print("ERROR: Nmap scan failed. Quitting...")
                sys.exit(1) # exit and raise error


