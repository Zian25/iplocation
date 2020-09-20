import os
import sys
import socket
import requests
import json
import random
import platform

sys.path.append("modulos")
from pinghavel import Pinghavel
ping = Pinghavel()
head = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; rv:78.0) Gecko/20100101 Firefox/78.0" }

cores = ['\033[1;31m', '\033[1;32m', '\033[1;33m', '\033[1;34m', '\033[1;35m', '\033[1;36m', '\033[1;37m', '\033[90m', '\033[31m', '\033[31m', '\033[32m', '\033[33m', '\033[34m', '\033[35m', '\033[36m', '\033[37m', '\033[90m', '\033[m']

def sys_clear():
    if platform.system() == "Linux":
        os.system("clear")
    elif platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def banner():
	logo = """
 ___ ____  _                    _   _
|_ _|  _ \\| |    ___   ___ __ _| |_(_) ___  _ __
 | || |_) | |   / _ \\ / __/ _` | __| |/ _ \\| '_ \\
 | ||  __/| |__| (_) | (_| (_| | |_| | (_) | | | |
|___|_|   |_____\___/ \___\__,_|\__|_|\___/|_| |_|
"""
	print(random.choice(cores) + logo)
	print ("\t\033[1;37m--[ \033[1;31mAutor\033[1;37m: \033[1;31mHagbard Celine")
	print ("\t\033[1;37m--[ \033[1;32mGrupo\033[1;37m: \033[1;32mFHC \033[1;37m- \033[1;32mFR13NDs Hackers Club")
	print ("\t\033[1;37m--[ \033[1;33mFacebook\033[1;37m: \033[1;33mhttps://www.facebook.com/miraldino.paulodoria.3")
	print ("\t\033[1;37m--[ \033[1;35mFB Page\033[1;37m: \033[1;35mhttps://www.facebook.com/termuxoficial\n\033[m")
   	
	

sys_clear()
banner()
ip = input("\033[1;36m[\033[1;31mhagbardceline\033[1;33m@\033[1;32miplocation\033[1;36m]-[\033[1;31mIP\033[1;36m]\033[1;31m.# ")
if ip == "auto":
	ip = ping.getip()
url = f"http://api.ipstack.com/{ip}?access_key=8352f5f9bc6d52c4ee3e9193c439f822"

req = requests.get(url, headers=head)
code = req.status_code
if code == 200:
	html = req.text
	iplocation = json.loads(html)
	sys_clear()
	banner()
	print ("\033[1;37m=============== \033[1;36mRESULTADOS\033[m \033[1;37m===============")
	print ("\033[1;33mIP:" +"\033[1;31m" + f" {iplocation['ip']}")
	print ("\033[1;33mType IP:" + "\033[1;31m" +f" {iplocation['type']}")
	print("\033[1;33mOrganização:" + "\033[1;31m" + f" {socket.gethostbyaddr(ip)[0]}")
	print ("\033[1;33mContinent_code:" + "\033[1;31m" + f" {iplocation['continent_code']}")
	print ("\033[1;33mContinent_name:"+"\033[1;31m"+ f" {iplocation['continent_name']}")
	print ("\033[1;33mCountry_code:" + "\033[1;31m" + f" {iplocation['country_code']}")
	print ("\033[1;33mCountry_name:" +"\033[1;31m" + f" {iplocation['country_name']}")
	print ("\033[1;33mRegion_code:" +"\033[1;31m" + f" {iplocation['region_code']}")
	print ("\033[1;33mRegion_name:"+ "\033[1;31m" + f" {iplocation['region_name']}")
	print ("\033[1;33mCity:" + "\033[1;31m" + f" {iplocation['city']}")
	print ("\033[1;33mZip:" + "\033[1;31m" + f" {iplocation['zip']}")
	print ("\033[1;33mLatitude:" + "\033[1;31m" + f" {iplocation['latitude']}")
	print ("\033[1;33mLongitude:"+  "\033[1;31m" + f" {iplocation['longitude']}")
	print ("\033[1;33mGeoname_id:" + "\033[1;31m" + f" {iplocation['location']['geoname_id']}")
	print ("\033[1;33mCapital:" + "\033[1;31m"  + f" {iplocation['location']['capital']}")
	#print "Languages: %s" % iplocation['location']['languages'][0]
	print ("\033[1;33mCalling_code:" + "\033[1;31m"  f" {iplocation['location']['calling_code']}")
	print ("\033[1;33mIs_eu:" + "\033[1;31m" + f" {iplocation['location']['is_eu']}")
	print ("\033[1;33mPingavel:" + "\033[1;31m" + f"{ping.pingavel(ip=ip)}")
	#print "Time_zone_id: %s" % iplocation['location']['time_zone']['id']
	print ("\033[m\033[1;37m==========================================\033[m")







