#!/usr/bin/env python

import subprocess

import optparse

import re



def get_argumets():

	parser= optparse.OptionParser()

	parser.add_option("-i", "--interface", dest="interface", help="interface to change its new mac address")

	parser.add_option("-m", "--mac", dest="new_mac", help="New Mac address")

	(option,arg)= parser.parse_args()

	if not option.interface:

		parser.error("[-] please enter interface")

	elif not option.new_mac:

		parser.error("[-] please enter new mac")

	return option



def change_mac(interface,new_mac):

	print("[+] changing mac of "+ interface +" to :"+ new_mac)

	subprocess.call(["ifconfig", interface, "down"])

	subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])

	subprocess.call(["ifconfig", interface, "up"])

	



def curr_mac(interface):

	read= subprocess.check_output(["ifconfig", interface])

	mac=re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", read)

	if mac:

		return mac.group(0)

	else:

		print("[-] could not read mac")		



option= get_argumets()

current_mac= curr_mac(option.interface)

print("current_mac = " + str(current_mac))



change_mac(option.interface,option.new_mac)



current_mac= curr_mac(option.interface)



if current_mac == option.new_mac:

	print("[+] mac change sucessfull :"+ current_mac)



else:

	print("[-] mac didn't change")


