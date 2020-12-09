import ipaddress
import sys

def checkInRange(min,val,max):
	if min<=val and val<=max : 
		print("[+] Private IP")
		sys.exit(0)

if __name__ == '__main__':
	try:
		ipaddr = input("Enter Ip : ")
		addr=ipaddress.IPv4Address(ipaddr)

	# This Will Catch All Exceptions Related To Incorrec IPs
	except : 
		print("[-] Invalid IP")
		sys.exit(-1)

	checkInRange(ipaddress.IPv4Address('10.0.0.0'),addr,ipaddress.IPv4Address('10.255.255.255'))
	checkInRange(ipaddress.IPv4Address('172.16.0.0'),addr,ipaddress.IPv4Address('172.31.255.255'))
	checkInRange(ipaddress.IPv4Address('192.168.0.0'),addr,ipaddress.IPv4Address('192.168.255.255'))

	print("[+] Public IP")