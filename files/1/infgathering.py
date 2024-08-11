import sys,os
from platform import system
import time
import whois
import socket
import requests
from bs4 import BeautifulSoup
VER = 2

try:
    if sys.version_info >= (3,0):
        VER = 3
        from urllib.request import urlopen
        from urllib.error import URLError
    else:
        input = raw_input
        from urllib2 import urlopen
        from urllib2 import URLError
except:
        pass

def cls():
        linux = 'clear'
        windows = 'cls'
        os.system([linux, windows][os.name == 'nt'])
        
def fetch(url, decoding='utf-8'):
    "Fetches content of URL"
    return urlopen(url).read().decode(decoding)

def banner():
		print ("""------------------------------------------------""")
		print ("""	\033[1m  INFORMATION GATHERING TOOLS""")
		print ("""------------------------------------------------""")
    
def menu():
	print("[+] 1. Whois Lookup")
	print("[+] 2. DNS Lookup + Cloudflare Detector")
	print("[+] 3. Zone Transfer ")
	print("[+] 4. Geo-IP Lookup ")
	print("[+] 5. HTTP Header Info")
	print("[+] 6. Link Grabber")
	print("[+] 7. Reverse IP Lookup")
	print("[+] 00. Back To Main Menu \n")

def lucillegatherer():
    choice = '1' 
    try:
        while choice != '11':
            menu()
            choice = input('\033[1;91mEnter your choice:\033[1;m ')
            if choice == '1':
                domip = input('\033[1;91mEnter Domain or IP Address: \033[1;m')
                command = "whois {}".format(domip)
                raw_output = os.popen(command).read()
                print('\n')
                print(raw_output)
            elif choice == '2':
                domain = input('\033[1;91mEnter Domain: \033[1;m')
                ns = "http://api.hackertarget.com/dnslookup/?q=" + domain
                pns = fetch(ns)
                print(pns)

                if 'cloudflare' in pns:
                    print("\033[1;31mCloudflare Detected!\033[1;m")
                else:
                    print("\033[1;31mNot Protected By cloudflare\033[1;m")

            elif choice == '3':
                domain = input('\033[1;91mEnter Domain: \033[1;m')
                zone = "http://api.hackertarget.com/zonetransfer/?q=" + domain
                pzone = fetch(zone)
                print(pzone)
                if 'failed' in pzone:
                    print("\033[1;31mZone transfer failed\033[1;m")

            elif choice == '4':
                ip = input('\033[1;91mEnter IP Address: \033[1;m')
                geo = "http://ipinfo.io/" + ip + "/geo"
                
                try:
                    pgeo = fetch(geo)
                    print(pgeo)
                except URLError:
                    print('\033[1;31m[-] Please provide a valid IP address!\033[1;m')


            elif choice == '5':
                domip = input('\033[1;91mEnter Domain or IP Address: \033[1;m')
                header = "http://api.hackertarget.com/httpheaders/?q=" + domip
                pheader = fetch(header)
                print(pheader)      

            elif choice == '6':
                page = input('\033[1;91mEnter URL: \033[1;m')

                if not (page.startswith('http://') or page.startswith('https://')):
                    page = 'http://' + page
                crawl = "https://api.hackertarget.com/pagelinks/?q=" + page
                pcrawl = fetch(crawl)
                print (pcrawl)
                
            elif choice == '7':
                ip = input('\033[1;91mEnter IP Address: \033[1;m')
                lookup = "http://api.hackertarget.com/reverseiplookup/?q=" + ip
                rvs = fetch(lookup)
                print(rvs)

            elif choice == '00':
                print('\033[97m11. Exiting\033[1;m')
                os.system("cd ../../ && chmod +x lucille.py && python lucille.py")

            else:
                print('\033[1;31m[-] Invalid option!\033[1;m')

    except KeyboardInterrupt:
        print('\033[97m\nGoing Back...\033[1;m')
        time.sleep(1)
        cls()
        os.system("chmod +x infgathering.py && python2 infgathering.py")
      
cls()
banner()
lucillegatherer()
