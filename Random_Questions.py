#!/usr/bin/env python2
# written by Moses Arocha


from random import randint


record = 0

def main():
	while (record == 0):
    	randomnumber = randint(0,5)
    	print "\n Random Question Number ", randomnumber
    	if 0 == randomnumber:
        	print "\n\n Sara, the security administrator, must configure the corporate firewall to allow all public IP addresses on the internal interface of the firewall to be translated to one public IP address on the external interface of the same firewall. Which of the following should Sara configure? \n"
			x = int(raw_input("\t 1. PAT \n\t 2. NAP \n\t 3. DNAT \n\t 4. NAC\n\n\t\t Answer Choice: "))
			if 1 == x:
	    		print "\n Correct!\n\n "
			else:
	    	    print "\n WRONG.\n\n "
    	elif 1 == randomnumber:
	  		print "\n\n Which of the following devices is MOST likely being used when processing the following? \n\t 1 PERMIT IP ANY ANY EQ 80 \n\t 2 DENY IP ANY ANY \n"
	  		x = int(raw_input("\n\t 1. Firewall \n\t 2. NIPS \n\t 3. Load Balancer \n\t 4. URL filer\n\n\t\t Answer Choice : "))
	  		if 1 == x:
	      		print "\n Correct!\n\n "
 	  		else:
	       		print "\n WRONG.\n\n "
    	elif 2 == randomnumber:
	  		print "\n\n The security administrator at ABC company received the following log information from an external party:\n 10:45:01 EST, SRC 10.4.3.7:3056, DST 8.4.2.1:80, ALERT, Directory traversal \n 10:45:02 EST, SRC 10.4.3.7:3057, DST 8.4.2.1:80, ALERT, Account brute force \n 10:45:03 EST, SRC 10.4.3.7:3058, DST 8.4.2.1:80, ALERT, Port scan \n\n The external party is reporting attacks coming from abc-company.com. Which of the following is the reason the ABC company's security administrator is unable to determine the origin of the attack?\n"
	  		x = int(raw_input("\n\t 1. A NIDS was used in place of a NIPS. \n\t 2. The log is not in UTC.  \n\t 3. The external party uses a firewall. \n\t 4. ABC company uses PAT.\n\n\t\t Answer Choice : "))
	  		if 4 == x:
	      		print "\n Correct!\n\n "
 	  		else:
	       		print "\n WRONG.\n\n "
    	elif 3 == randomnumber:
	  		print "\n\n Which of the following security devices can be replicated on a Linux based computer using IP tables to inspect and properly handle network based traffic?\n"
	  		x = int(raw_input("\n\t 1. Sniffer \n\t 2. Router  \n\t 3. Firewall \n\t 4. Switch \n\n\t\t Answer Choice : "))
	  		if 3 == x:
	      		print "\n Correct!\n\n "
 	  		else:
	       		print "\n WRONG.\n\n "
    	elif 4 == randomnumber:
	  		print "\n\n Which of the following firewall types inspects Ethernet traffic at the MOST levels of the OSI model?\n"
	  		x = int(raw_input("\n\t 1. Packet Filter Firewall \n\t 2. Stateful Firewall  \n\t 3. Proxy Firewall \n\t 4. Application Firewall \n\n\t\t Answer Choice : "))
	  		if 2 == x:
	      		print "\n Correct!\n\n "
 	  		else:
	       		print "\n WRONG.\n\n "
    	elif 5 == randomnumber:
	  		print "\n\n The Chief Information Security Officer (CISO) has mandated that all IT systems with credit card data be segregated from the main corporate network to prevent unauthorized access and that access to the IT systems should be logged. Which of the following would BEST meet the CISO's requirements?\n"
	  		x = int(raw_input("\n\t 1. Sniffers \n\t 2. NIDS \n\t 3. Firewalls \n\t 4. Web Proxies \n\t 5. Layer 2 Switches  \n\n\t\t Answer Choice : "))
	  		if 3 == x:
	      		print "\n Correct!\n\n "
 	  		else:
	       		print "\n WRONG.\n\n "


main()
