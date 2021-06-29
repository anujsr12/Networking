import subprocess

import re

import optparse



def get_arguments():

	parser= optparse.OptionParser()

	parser.add_option("-i","--interface" , dest="interface" , help="interface that you waant to restore the mac")

	(option, argument)= parser.parse_args()

	if not option.interface:

		print("enter interface for help use --help")

	else:

		return option



def curr_mac(interface):

	read= subprocess.check_output(["ifconfig", interface])

	mac= re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", read)

	if mac:

		return mac.group(0)

	else:

		print("couldn't read mac")



def default_mac(interface):

	read= subprocess.check_output(["macchanger", interface])

	mac= re.findall(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", read)

	if mac:

		return mac[1]

	else:

		print("[-] couldn't read mac")



def change_mac_to_default(default,interface):

	print("[+] changing mac of "+ interface +" to default : " +default)

	subprocess.call(["ifconfig", interface, "down"])

	subprocess.call(["ifconfig", interface, "hw", "ether", default])

	subprocess.call(["ifconfig", interface, "up"])



option = get_arguments()

current_mac= curr_mac(option.interface)

print("current_mac : " +str(current_mac))



default= default_mac(option.interface)



change_mac_to_default(default, option.interface)

current_mac= curr_mac(option.interface)

if current_mac== default:

	print("[+] mac got changed to : " +current_mac)

else:

	print("[-] mac didn't change")

