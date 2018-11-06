import sys
import datetime
import optparse
from scapy.all import *

# function to parse command line args
def get_arguments():
        parser = optparse.OptionParser()
        parser.add_option("-t", "--target", dest="target",
                help="Target IP.")
	parser.add_option("-p", "--ports", dest="ports")

        options, arguments = parser.parse_args()
        return options

options = get_arguments()
target = options.target
ports = options.ports

TCP_REVERSE = dict((TCP_SERVICES[k], k) for k in TCP_SERVICES.keys())

# parse ports into range list
ports = ports.split('-')

ip = target
closed = 0
openp = []

def is_up(ip):
    """ Tests if host is up """
    icmp = IP(dst=ip)/ICMP()
    resp = sr1(icmp, timeout=10)
    if resp == None:
        return False
    else:
        return True

if __name__ == '__main__':
    conf.verb = 0 # Disable verbose in sr(), sr1() methods

    start_time = time.time()
    ports = range(int(ports[0]), int(ports[1])+1)
    isAP = False
    OS = ''
    if is_up(ip):
        print "\nStarting scan on %s at %s " % (ip, datetime.now())

        for port in ports:
            src_port = RandShort() # Getting a random port as source port
            p = IP(dst=ip)/TCP(sport=src_port, dport=port, flags='S') # Forging SYN packet
            resp = sr1(p, timeout=2) # Sending packet
            if not str(type(resp)) == "<type 'NoneType'>":
                if resp.haslayer(Dot11):
                    #if pkt.type == 0 and pkt.subtype == 8:
                    isAP = True

            if str(type(resp)) == "<type 'NoneType'>":
                closed += 1
            elif resp.haslayer(TCP):
                if resp.getlayer(TCP).flags == 0x12:

                    send_rst = sr(IP(dst=ip)/TCP(sport=src_port, dport=port, flags='AR'), timeout=1)

                    openp.append(port)

                    ttl = resp.ttl
                    window = resp.window

                    OS = ''

                    if ttl == 64:
                        OS = 'Linux/UNIX/BSD'
                    elif ttl == 128:
                        OS = 'Windows/NT'
                    elif ttl == 254:
                        OS = 'Solaris/AIX'
                    elif ttl == 255:
                        OS = 'IOS'
                elif resp.getlayer(TCP).flags == 0x14:
                    closed += 1
                    ttl = resp.ttl
                    window = resp.window

                    OS = ''
                    if ttl == 64:
                        OS = 'Linux/UNIX/BSD'
                    elif ttl == 128:
                        OS = 'Windows/NT'
                    elif ttl == 254:
                        OS = 'Solaris/AIX'
                    elif ttl == 255:
                        OS = 'IOS'

        print "Scan completed at %s" % datetime.now()
        if len(openp) != 0:
            print('PORT  STATE  SERVICE')
            for opp in openp:
                print "%d    open   %s" % (opp, TCP_REVERSE[opp])
	if OS != '':
           print('OS scan: %s' % OS)
        elif OS == '':
           print('ttl-window: %i:%i' % (ttl, window))
        '''
        if isAP:
           print('Target is AP/Router')
        elif not isAP:
           print('Target is host/server')'''
        try:
           print('Rev. DNS: %s' % socket.gethostbyaddr(target)[0])
        except:
           print('Rev. DNS FAILED')
else:
        print "Host %s is Down" % ip
