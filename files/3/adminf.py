from urllib2 import Request, urlopen, URLError, HTTPError
import time
import sys,os
la7mar  = '\033[91m'
lazra9  = '\033[94m'
la5dhar = '\033[92m'
movv    = '\033[95m'
lasfar  = '\033[93m'
ramadi  = '\033[90m'
blid    = '\033[1m'
star    = '\033[4m'
bigas   = '\033[07m'
bigbbs  = '\033[27m'
hell    = '\033[05m'
saker   = '\033[25m'
labyadh = '\033[00m'
cyan    = '\033[0;96m'

def cls():
        linux = 'clear'
        windows = 'cls'
        os.system([linux, windows][os.name == 'nt'])
def print_logo():
        print ("""------------------------------------------------""")
        print ("""	  Admin Panel Finder """)
        print ("""------------------------------------------------""")
        

def Space(j):
		i = 0
		while i<=j:
			print " ",
			i+=1
def findAdmin():
		f = open("login.txt","r");
		link = raw_input("\033[1;32mURL : ")
		print la7mar + "\n\n[+] Avilable links : \n"
		while True:
			sub_link = f.readline()
			if not sub_link:
				break
			req_link = link+"/"+sub_link
			req = Request(req_link)
			try:
				response = urlopen(req)
			except HTTPError as e:
				print la7mar + "HTTPError => ",req_link
				continue
			except URLError as e:
				print la7mar + "URLError => ",req_link
				continue
			else:
				print la5dhar + "OK => ",req_link

      

cls()
print_logo()
try:
	findAdmin()
except KeyboardInterrupt:
    print('\033[97m\nGoing Back...\033[1;m')
    time.sleep(1)
    cls()
    os.system(" chmod +x exploit.py && python2 exploit.py")