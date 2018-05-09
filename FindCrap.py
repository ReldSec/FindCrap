#!/usr/bin/env python
#_*_ coding: utf8 _*_

import requests
import random
import time
import sys
from datetime import datetime
import argparse
from os import path
import os
from colorama import Fore
import socket

print(Fore.LIGHTRED_EX)
cmd = os.system("reset")
args = argparse.ArgumentParser()
args.add_argument("-u","--url",help="Url attack")
args.add_argument("-t","--timesec",help="Tiempo de espera")
args.add_argument("-s","--sensiblepaths",help="Discover sensible paths")
argss = args.parse_args()

agents_list = []
agents = open("dbcore/agents/user-agents.txt","r")
for ax in agents:
	ac = ax.replace("\n","")
	agents_list.append(ac)

random_agent_pos = random.randint(0,len(agents_list))

random_agent = agents_list[random_agent_pos]
user_agent = {'User-agent': random_agent}
hour = datetime.now()
hour_style = hour.strftime("%Y:%m")
paths = path.realpath(sys.argv[0])

def logo():
	print(Fore.LIGHTRED_EX + "/$$$$$$$$ /$$                 /$$  /$$$$$$                              ")
	print(Fore.LIGHTRED_EX + "| $$_____/|__/                | $$ /$$__  $$                             ")
	print(Fore.LIGHTRED_EX + "| $$_____/|__/                | $$ /$$__  $$                             ")
	print(Fore.LIGHTRED_EX + "| $$       /$$ /$$$$$$$   /$$$$$$$| $$  \__/  /$$$$$$  /$$$$$$   /$$$$$$ ")
	print(Fore.LIGHTRED_EX + "| $$$$$   | $$| $$__  $$ /$$__  $$| $$       /$$__  $$|____  $$ /$$__  $$")
	print(Fore.LIGHTGREEN_EX + "| $$__/   | $$| $$  \ $$| $$  | $$| $$      | $$  \__/ /$$$$$$$| $$  \ $$")
	print(Fore.LIGHTGREEN_EX + "| $$      | $$| $$  | $$| $$  | $$| $$    $$| $$      /$$__  $$| $$  | $$")
	print(Fore.LIGHTGREEN_EX + "| $$      | $$| $$  | $$|  $$$$$$$|  $$$$$$/| $$     |  $$$$$$$| $$$$$$$/")
	print(Fore.LIGHTGREEN_EX + "|__/      |__/|__/  |__/ \_______/ \______/ |__/      \_______/| $$____/ ")
	print(Fore.LIGHTGREEN_EX + "                                                              | $$      ")
	print(Fore.LIGHTGREEN_EX + "                                                              | $$      ")
	print(Fore.LIGHTGREEN_EX + "                                                              |__/      ")
	print(Fore.LIGHTWHITE_EX + "Twitter: @IDX4CKS\thttps://www.facebook.com/reldsec/")
	print(Fore.LIGHTWHITE_EX + "\n=========================================================================================\n")


def testnet():
	test = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	try:
		test.connect(('www.google.com', 80))
		print(Fore.LIGHTGREEN_EX + "\n\nEstamos Online\n\n")
	        test.close()
	except:
		print(Fore.LIGHTRED_EX + "\nError de conexión\n")
		exit()

def slowprint(letter):
	for l in letter:
		print l,
		time.sleep(0.1)

def attack_time_sleep(urla,time_sleep):
	victory = []
	admin_list = open("dbcore/admin/default_admin_list.txt")
	list_attack = []
	for url in admin_list:
		ad = url.replace("\n","")
		list_attack.append(ad)

	num_request = len(list_attack) - 1
	print(Fore.LIGHTWHITE_EX + "Numero de peticiones =>\t{}".format(num_request))
	print(Fore.LIGHTWHITE_EX + "Tiempo de espera entre peticion => {}".format(time_sleep))
	print(Fore.LIGHTWHITE_EX + "Random Agent => {}".format(random_agent))
	print("\n")
	for link in range(0,num_request):
		urlopen = requests.get(urla+list_attack[link],headers=user_agent)
		time.sleep(time_sleep)
		if urlopen.status_code == 404:
			print(Fore.LIGHTRED_EX + "Status: {}".format(str(urlopen.status_code) + "  " +urla+list_attack[link]))
		elif urlopen.status_code == 200:
			print("\n" + Fore.LIGHTGREEN_EX + "Status: {}".format(str(urlopen.status_code) + "  " +urla+list_attack[link]) + "\n")
			victory.append(urla+list_attack[link])
		elif urlopen.status_code == 500:
			print("\n" + Fore.CYAN + "Status: {}".format(str(urlopen.status_code) + "  " +urla+list_attack[link]) + "\n")

	if len(victory) > 0:
		print(Fore.LIGHTWHITE_EX + "===============================================================")
		for a in range(0,len(victory)):
			print(Fore.LIGHTGREEN_EX + victory[a])
	else:
		print(Fore.LIGHTRED_EX + "No results found")
		exit()

def attack_sensible(urla):
	dicc = open('dbcore/sensitive/dicc.txt','r')
	dicc_list = []
	for ic in dicc:
		ad = ic.replace("\n","")
		dicc_list.append(ad)

	fies = open('dbcore/sensitive/files.txt','r')
	fies_list = []
	for fi in fies:
		ad = fi.replace("\n","")
		fies_list.append(ad)

	passwords = open('dbcore/sensitive/passwords.txt','r')
	passwords_list = []
	for pi in passwords:
		ad = pi.replace("\n","")
		passwords_list.append(ad)

	php = open('dbcore/sensitive/php.txt','r')
	php_list = []
	for phi in php:
		ad = phi.replace("\n","")
		php_list.append(ad)

	unixfiles = open('dbcore/sensitive/unixfiles.txt','r')
	unixfiles_list = []
	for uni in unixfiles:
		ad = uni.replace("\n","")
		unixfiles_list.append(ad)

	unix_locations = open('dbcore/sensitive/unix_locations.txt','r')
	unix_locations_list = []
	for li in unix_locations:
		ad = li.replace("\n","")
		unix_locations_list.append(ad)

	victory = []
	admin_list = open("dbcore/admin/default_admin_list.txt")
	list_attack = []
	for url in admin_list:
		ad = url.replace("\n","")
		list_attack.append(ad)

	num_request = len(list_attack) - 1
	all_request = num_request + len(dicc_list) + len(fies_list) + len(passwords_list) + len(php_list) + len(unixfiles_list) + len(unix_locations_list)
	print(Fore.LIGHTWHITE_EX + "Numero de peticiones =>\t{}".format(all_request))
	print(Fore.LIGHTWHITE_EX + "Random Agent => {}".format(random_agent))
	print(Fore.LIGHTRED_EX + "Sensible Paths Mode!")
	print(Fore.LIGHTGREEN_EX + "\tPHP\n\tUNIX LOCATIONS\n\tPasswords")
	print("\n")

	for link in range(0,num_request):
		urlopen = requests.get(urla+list_attack[link],headers=user_agent)
		if urlopen.status_code == 404:
			print(Fore.LIGHTRED_EX + "Status: {}".format(str(urlopen.status_code) + "  " +urla+list_attack[link]))
		elif urlopen.status_code == 200:
			print("\n" + Fore.LIGHTGREEN_EX + "Status: {}".format(str(urlopen.status_code) + "  " +urla+list_attack[link]) + "\n")
			victory.append(urla+list_attack[link])
		elif urlopen.status_code == 500:
			print("\n" + Fore.CYAN + "Status: {}".format(str(urlopen.status_code) + "  " +urla+list_attack[link]) + "\n")

	print(Fore.LIGHTWHITE_EX + "\n=======================================================")
	print(Fore.LIGHTGREEN_EX + "\tIniciando Primer modo")
	print(Fore.LIGHTWHITE_EX + "=======================================================\n")

	for i in range(0,len(dicc_list)-1):
		url = requests.get(urla+dicc_list[i],headers=user_agent)
		if url.status_code == 404:
			print(Fore.LIGHTRED_EX + "Status: {}".format(str(url.status_code)) + "  " + urla+dicc_list[i])
		elif url.status_code == 200:
			print("\n" + Fore.LIGHTGREEN_EX + "Status: {}".format(str(url.status_code)) + "  " + urla+dicc_list[i] + "\n")
			victory.append(urla+dicc_list[i])
		if url.status_code == 500:
			print(Fore.CYAN + "Status: {}".format(str(url.status_code)) + "  " + urla+dicc_list[i])

	print(Fore.LIGHTWHITE_EX + "\n=======================================================")
	print(Fore.LIGHTGREEN_EX + "\tIniciando Segundo modo")
	print(Fore.LIGHTWHITE_EX + "=======================================================\n")

	for i in range(0,len(fies_list)-1):
		url = requests.get(urla+fies_list[i],headers=user_agent)
		if url.status_code == 404:
			print(Fore.LIGHTRED_EX + "Status: {}".format(str(url.status_code)) + "  " + urla+fies_list[i])
		elif url.status_code == 200:
			print("\n" + Fore.LIGHTGREEN_EX + "Status: {}".format(str(url.status_code)) + "  " + urla+fies_list[i] + "\n")
			victory.append(urla+fies_list[i])
		if url.status_code == 500:
			print(Fore.CYAN + "Status: {}".format(str(url.status_code)) + "  " + urla+fies_list[i])

	print(Fore.LIGHTWHITE_EX + "\n=======================================================")
	print(Fore.LIGHTGREEN_EX + "\tIniciando Tercer modo")
	print(Fore.LIGHTWHITE_EX + "=======================================================\n")

	for i in range(0,len(passwords_list)-1):
		url = requests.get(urla+passwords_list[i],headers=user_agent)
		if url.status_code == 404:
			print(Fore.LIGHTRED_EX + "Status: {}".format(str(url.status_code)) + "  " + urla+passwords_list[i])
		elif url.status_code == 200:
			print("\n" + Fore.LIGHTGREEN_EX + "Status: {}".format(str(url.status_code)) + "  " + urla+passwords_list[i] + "\n")
			victory.append(urla+passwords_list[i])
		if url.status_code == 500:
			print(Fore.CYAN + "Status: {}".format(str(url.status_code)) + "  " + urla+passwords_list[i])

	print(Fore.LIGHTWHITE_EX + "\n=======================================================")
	print(Fore.LIGHTGREEN_EX + "\tIniciando Cuarto modo")
	print(Fore.LIGHTWHITE_EX + "=======================================================\n")

	for i in range(0,len(php_list)-1):
		url = requests.get(urla+php_list[i],headers=user_agent)
		if url.status_code == 404:
			print(Fore.LIGHTRED_EX + "Status: {}".format(str(url.status_code)) + "  " + urla+php_list[i])
		elif url.status_code == 200:
			print("\n" + Fore.LIGHTGREEN_EX + "Status: {}".format(str(url.status_code)) + "  " + urla+php_list[i] + "\n")
			victory.append(urla+php_list[i])
		if url.status_code == 500:
			print(Fore.CYAN + "Status: {}".format(str(url.status_code)) + "  " + urla+php_list[i])

	print(Fore.LIGHTWHITE_EX + "\n=======================================================")
	print(Fore.LIGHTGREEN_EX + "\tIniciando quinto modo")
	print(Fore.LIGHTWHITE_EX + "=======================================================\n")

	for i in range(0,len(unixfiles_list)-1):
		url = requests.get(urla+unixfiles_list[i],headers=user_agent)
		if url.status_code == 404:
			print(Fore.LIGHTRED_EX + "Status: {}".format(str(url.status_code)) + "  " + urla+unixfiles_list[i])
		elif url.status_code == 200:
			print("\n" + Fore.LIGHTGREEN_EX + "Status: {}".format(str(url.status_code)) + "  " + urla+unixfiles_list[i] + "\n")
			victory.append(urla+unixfiles_list[i])
		if url.status_code == 500:
			print(Fore.CYAN + "Status: {}".format(str(url.status_code)) + "  " + urla+unixfiles_list[i])

	print(Fore.LIGHTWHITE_EX + "\n=======================================================")
	print(Fore.LIGHTGREEN_EX + "\tIniciando sexto modo")
	print(Fore.LIGHTWHITE_EX + "=======================================================\n")

	for i in range(0,len(unix_locations_list)-1):
		url = requests.get(urla+unix_locations_list[i],headers=user_agent)
		if url.status_code == 404:
			print(Fore.LIGHTRED_EX + "Status: {}".format(str(url.status_code)) + "  " + urla+unix_locations_list[i])
		elif url.status_code == 200:
			print("\n" + Fore.LIGHTGREEN_EX + "Status: {}".format(str(url.status_code)) + "  " + urla+unix_locations_list[i] + "\n")
			victory.append(urla+unix_locations_list[i])
		if url.status_code == 500:
			print(Fore.CYAN + "Status: {}".format(str(url.status_code)) + "  " + urla+unix_locations_list[i])

	if len(victory) > 0:
		print(Fore.LIGHTWHITE_EX + "\n===============================================================")
		for a in range(0,len(victory)):
			print(Fore.LIGHTGREEN_EX + "Fund! => " + victory[a])
	else:
		print(Fore.LIGHTRED_EX + "No results found")
		exit()

def default(urla):
	victory = []
	admin_list = open("dbcore/admin/default_admin_list.txt")
	list_attack = []
	for url in admin_list:
		ad = url.replace("\n","")
		list_attack.append(ad)

	num_request = len(list_attack) - 1
	print(Fore.LIGHTWHITE_EX + "Numero de peticiones =>\t{}".format(num_request))
	print(Fore.LIGHTWHITE_EX + "Random Agent => {}".format(random_agent))
	print("\n")

	for link in range(0,num_request):
		urlopen = requests.get(urla+list_attack[link],headers=user_agent)
		if urlopen.status_code == 404:
			print(Fore.LIGHTRED_EX + "Status: {}".format(str(urlopen.status_code) + "  " +urla+list_attack[link]))
		elif urlopen.status_code == 200:
			print("\n" + Fore.LIGHTGREEN_EX + "Status: {}".format(str(urlopen.status_code) + "  " +urla+list_attack[link]) + "\n")
			victory.append(urla+list_attack[link])
		elif urlopen.status_code == 500:
			print("\n" + Fore.CYAN + "Status: {}".format(str(urlopen.status_code) + "  " +urla+list_attack[link]) + "\n")

	if len(victory) > 0:
		print(Fore.LIGHTWHITE_EX + "===============================================================")
		for a in range(0,len(victory)):
			print(Fore.LIGHTGREEN_EX + victory[a])
	else:
		print(Fore.LIGHTRED_EX + "No results found")
		exit()

def attack_time_sensible(urla,time_sleep):
	dicc = open('dbcore/sensitive/dicc.txt','r')
	dicc_list = []
	for ic in dicc:
		ad = ic.replace("\n","")
		dicc_list.append(ad)

	fies = open('dbcore/sensitive/files.txt','r')
	fies_list = []
	for fi in fies:
		ad = fi.replace("\n","")
		fies_list.append(ad)

	passwords = open('dbcore/sensitive/passwords.txt','r')
	passwords_list = []
	for pi in passwords:
		ad = pi.replace("\n","")
		passwords_list.append(ad)

	php = open('dbcore/sensitive/php.txt','r')
	php_list = []
	for phi in php:
		ad = phi.replace("\n","")
		php_list.append(ad)

	unixfiles = open('dbcore/sensitive/unixfiles.txt','r')
	unixfiles_list = []
	for uni in unixfiles:
		ad = uni.replace("\n","")
		unixfiles_list.append(ad)

	unix_locations = open('dbcore/sensitive/unix_locations.txt','r')
	unix_locations_list = []
	for li in unix_locations:
		ad = li.replace("\n","")
		unix_locations_list.append(ad)

	victory = []
	admin_list = open("dbcore/admin/default_admin_list.txt")
	list_attack = []
	for url in admin_list:
		ad = url.replace("\n","")
		list_attack.append(ad)

	num_request = len(list_attack) - 1
	all_request = num_request + len(dicc_list) + len(fies_list) + len(passwords_list) + len(php_list) + len(unixfiles_list) + len(unix_locations_list)
	print(Fore.LIGHTWHITE_EX + "Numero de peticiones =>\t{}".format(all_request))
	print(Fore.LIGHTWHITE_EX + "Tiempo de espera entre peticion => {}".format(time_sleep))
	print(Fore.LIGHTWHITE_EX + "Random Agent => {}".format(random_agent))
	print(Fore.LIGHTRED_EX + "Sensible Paths Mode!")
	print(Fore.LIGHTGREEN_EX + "\tPHP\n\tUNIX LOCATIONS\n\tPasswords")
	print("\n")

	for link in range(0,num_request):
		urlopen = requests.get(urla+list_attack[link],headers=user_agent)
		time.sleep(time_sleep)
		if urlopen.status_code == 404:
			print(Fore.LIGHTRED_EX + "Status: {}".format(str(urlopen.status_code) + "  " +urla+list_attack[link]))
		elif urlopen.status_code == 200:
			print("\n" + Fore.LIGHTGREEN_EX + "Status: {}".format(str(urlopen.status_code) + "  " +urla+list_attack[link]) + "\n")
			victory.append(urla+list_attack[link])
		elif urlopen.status_code == 500:
			print("\n" + Fore.CYAN + "Status: {}".format(str(urlopen.status_code) + "  " +urla+list_attack[link]) + "\n")

	print(Fore.LIGHTWHITE_EX + "\n=======================================================")
	print(Fore.LIGHTGREEN_EX + "\tIniciando Primer modo")
	print(Fore.LIGHTWHITE_EX + "=======================================================\n")

	for i in range(0,len(dicc_list)-1):
		url = requests.get(urla+dicc_list[i],headers=user_agent)
		time.sleep(time_sleep)
		if url.status_code == 404:
			print(Fore.LIGHTRED_EX + "Status: {}".format(str(url.status_code)) + "  " + urla+dicc_list[i])
		elif url.status_code == 200:
			print("\n" + Fore.LIGHTGREEN_EX + "Status: {}".format(str(url.status_code)) + "  " + urla+dicc_list[i] + "\n")
			victory.append(urla+dicc_list[i])
		if url.status_code == 500:
			print(Fore.CYAN + "Status: {}".format(str(url.status_code)) + "  " + urla+dicc_list[i])

	print(Fore.LIGHTWHITE_EX + "\n=======================================================")
	print(Fore.LIGHTGREEN_EX + "\tIniciando Segundo modo")
	print(Fore.LIGHTWHITE_EX + "=======================================================\n")

	for i in range(0,len(fies_list)-1):
		url = requests.get(urla+fies_list[i],headers=user_agent)
		time.sleep(time_sleep)
		if url.status_code == 404:
			print(Fore.LIGHTRED_EX + "Status: {}".format(str(url.status_code)) + "  " + urla+fies_list[i])
		elif url.status_code == 200:
			print("\n" + Fore.LIGHTGREEN_EX + "Status: {}".format(str(url.status_code)) + "  " + urla+fies_list[i] + "\n")
			victory.append(urla+fies_list[i])
		if url.status_code == 500:
			print(Fore.CYAN + "Status: {}".format(str(url.status_code)) + "  " + urla+fies_list[i])

	print(Fore.LIGHTWHITE_EX + "\n=======================================================")
	print(Fore.LIGHTGREEN_EX + "\tIniciando Tercer modo")
	print(Fore.LIGHTWHITE_EX + "=======================================================\n")

	for i in range(0,len(passwords_list)-1):
		url = requests.get(urla+passwords_list[i],headers=user_agent)
		time.sleep(time_sleep)
		if url.status_code == 404:
			print(Fore.LIGHTRED_EX + "Status: {}".format(str(url.status_code)) + "  " + urla+passwords_list[i])
		elif url.status_code == 200:
			print("\n" + Fore.LIGHTGREEN_EX + "Status: {}".format(str(url.status_code)) + "  " + urla+passwords_list[i] + "\n")
			victory.append(urla+passwords_list[i])
		if url.status_code == 500:
			print(Fore.CYAN + "Status: {}".format(str(url.status_code)) + "  " + urla+passwords_list[i])

	print(Fore.LIGHTWHITE_EX + "\n=======================================================")
	print(Fore.LIGHTGREEN_EX + "\tIniciando Cuarto modo")
	print(Fore.LIGHTWHITE_EX + "=======================================================\n")

	for i in range(0,len(php_list)-1):
		url = requests.get(urla+php_list[i],headers=user_agent)
		time.sleep(time_sleep)
		if url.status_code == 404:
			print(Fore.LIGHTRED_EX + "Status: {}".format(str(url.status_code)) + "  " + urla+php_list[i])
		elif url.status_code == 200:
			print("\n" + Fore.LIGHTGREEN_EX + "Status: {}".format(str(url.status_code)) + "  " + urla+php_list[i] + "\n")
			victory.append(urla+php_list[i])
		if url.status_code == 500:
			print(Fore.CYAN + "Status: {}".format(str(url.status_code)) + "  " + urla+php_list[i])

	print(Fore.LIGHTWHITE_EX + "\n=======================================================")
	print(Fore.LIGHTGREEN_EX + "\tIniciando quinto modo")
	print(Fore.LIGHTWHITE_EX + "=======================================================\n")

	for i in range(0,len(unixfiles_list)-1):
		url = requests.get(urla+unixfiles_list[i],headers=user_agent)
		time.sleep(time_sleep)
		if url.status_code == 404:
			print(Fore.LIGHTRED_EX + "Status: {}".format(str(url.status_code)) + "  " + urla+unixfiles_list[i])
		elif url.status_code == 200:
			print("\n" + Fore.LIGHTGREEN_EX + "Status: {}".format(str(url.status_code)) + "  " + urla+unixfiles_list[i] + "\n")
			victory.append(urla+unixfiles_list[i])
		if url.status_code == 500:
			print(Fore.CYAN + "Status: {}".format(str(url.status_code)) + "  " + urla+unixfiles_list[i])

	print(Fore.LIGHTWHITE_EX + "\n=======================================================")
	print(Fore.LIGHTGREEN_EX + "\tIniciando sexto modo")
	print(Fore.LIGHTWHITE_EX + "=======================================================\n")

	for i in range(0,len(unix_locations_list)-1):
		url = requests.get(urla+unix_locations_list[i],headers=user_agent)
		time.sleep(time_sleep)
		if url.status_code == 404:
			print(Fore.LIGHTRED_EX + "Status: {}".format(str(url.status_code)) + "  " + urla+unix_locations_list[i])
		elif url.status_code == 200:
			print("\n" + Fore.LIGHTGREEN_EX + "Status: {}".format(str(url.status_code)) + "  " + urla+unix_locations_list[i] + "\n")
			victory.append(urla+unix_locations_list[i])
		if url.status_code == 500:
			print(Fore.CYAN + "Status: {}".format(str(url.status_code)) + "  " + urla+unix_locations_list[i])

	if len(victory) > 0:
		print(Fore.LIGHTWHITE_EX + "\n===============================================================")
		for a in range(0,len(victory)):
			print(Fore.LIGHTGREEN_EX + "Fund! => " + victory[a])
	else:
		print(Fore.LIGHTRED_EX + "No results found")
		exit()

def main():
	logo()
	print(Fore.LIGHTRED_EX + "Probando conexión...")
	testnet()
	if len(sys.argv) < 2:
		print(Fore.LIGHTRED_EX + "Url no set\n\n")
		exit()
	ext = argss.url
	ext_end = ext.find("http")
	if ext_end == -1:
		print(Fore.LIGHTRED_EX + "http://\t=>" + Fore.LIGHTGREEN_EX + "\tNo defined")
		exit()
	else:
		print(Fore.LIGHTWHITE_EX + "Attack => {}".format(argss.url))

	if argss.sensiblepaths:
		if argss.sensiblepaths != "all":
			print("\nUse -s all")
			exit()

	if argss.timesec and argss.url and argss.sensiblepaths:
		directory_end = argss.url[-1]
		if directory_end != "/":
			custom_url = argss.url+"/"
		else:
			custom_url = argss.url
		time_sleep = int(argss.timesec)
		attack_time_sensible(custom_url,time_sleep)

	elif argss.url and argss.sensiblepaths:
		directory_end = argss.url[-1]
		if directory_end != "/":
			custom_url = argss.url+"/"
		else:
			custom_url = argss.url

		attack_sensible(custom_url)

	elif argss.timesec and argss.url:
		directory_end = argss.url[-1]
		if directory_end != "/":
			custom_url = argss.url+"/"
		else:
			custom_url = argss.url

		time_sleep = int(argss.timesec)

		attack_time_sleep(custom_url,time_sleep)

	elif argss.url:
		directory_end = argss.url[-1]
		if directory_end != "/":
			custom_url = argss.url+"/"
		else:
			custom_url = argss.url

		default(custom_url)

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		print(Fore.BLUE + "\n\nDeteniendo...")
		time.sleep(1)
		print(Fore.LIGHTRED_EX + "\n\nSaliendo..\n")
		time.sleep(0.1)
		exit()
