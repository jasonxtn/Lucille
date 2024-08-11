
import sys,os
from platform import system
import time
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
		print ("""	  \033[1mPassword Attack TOOLS""")
		print ("""------------------------------------------------""")
    
def menu():
	print("[+] 1. CMS Detector")
	print("[+] 2. Wordpress Brute Force")
	print("[+] 3. Joomla Brute force ")
	print("[+] 00. Back To Main Menu \n")

def lucillebruter():
    choice = '1' 

    while choice != '11':
        menu()
        choice = input('\033[1;91mEnter your choice:\033[1;m ')

        if choice == '1':
            if system() == 'Linux':
                os.system(" chmod +x cmsdetect.py && python cmsdetect.py")
            if system() == 'Windows':
                os.system('python cmsdetect.py')
        elif choice == '2':
            if system() == 'Linux':
                os.system(" chmod +x wpbf.py && python2 wpbf.py")
            if system() == 'Windows':
                os.system('python wpbf.py')

        elif choice == '3':
            if system() == 'Linux':
                os.system(" chmod +x jmbf.py && python2 jmbf.py")
            if system() == 'Windows':
                os.system('python jmbf.py')
        elif choice == '4':
            ip = input('\033[1;91mEnter IP Address: \033[1;m')
            geo = "http://ipinfo.io/" + ip + "/geo"
            
            try:
                pgeo = fetch(geo)
                print(pgeo)
            except URLError:
                print('\033[1;31m[-] Please provide a valid IP address!\033[1;m')
        elif choice == '00':
            print('\033[97m11. Exiting\033[1;m')
            os.system("cd ../../ && chmod +x lucille.py && python2 lucille.py")

        else:
            print('\033[1;31m[-] Invalid option!\033[1;m')
cls()
banner()


try:
	lucillebruter()
except KeyboardInterrupt:
    print('\033[97m\nGoing Back...\033[1;m')
    time.sleep(1)
    cls()
    os.system("cd ../../ && chmod +x lucille.py && python2 lucille.py")