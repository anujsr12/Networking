#!/usr/bin/env python
import scapy.all as scapy
import optparse

def arguments():
	parser= optparse.OptionParser()
	parser.add_option("-t", "--target", dest="target", help="which tarrget-ip address want to search")
	(option,arguments)=parser.parse_args()
	if not option.target:
		print("[-] enter the target ip address")
		return option
	else:
		return option
def scan(ip):
	arp_req= scapy.ARP(pdst=ip)
	broadcast= scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
	broadcast_arp_request= broadcast/arp_req
	answered_list= scapy.srp(broadcast_arp_request, timeout=1, verbose=False)[0]
	client_list =[]
	for element in answered_list:
		client_dict={"ip": element[1].psrc, "mac":element[1].hwsrc}
		client_list.append(client_dict)
	return client_list

def print_list(client_list):
	print("IP\t\t\tMAC_ADDRESS")
	print("*---------------------------------------*")
	for element in client_list:
		print(element["ip"]+"\t\t"+elem
