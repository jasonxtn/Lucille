
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
		print ("""	 \033[1m POST EXPLOITATION TOOLS""")
		print ("""------------------------------------------------""")
    
def menu():
	print("[+] 1. WEB SHELL CHECKER")
	print("[+] 2. WORDPRESS SHELL UPLOADER")
	print("[+] 3. JOOMLA SHELL UPLOADER")
	print("[+] 00. Back To Main Menu \n")

def lucillex():
    choice = '1' 
    

    while choice != '11':
        menu()
        choice = input('\033[1;91mEnter your choice:\033[1;m ')

        if choice == '1':
            if system() == 'Linux':
                os.system(" chmod +x checker.py && python checker.py")
            if system() == 'Windows':
                os.system('python checker.py')
        elif choice == '2':
            if system() == 'Linux':
                os.system(" chmod +x wp_revshell.py && python wp_revshell.py")
            if system() == 'Windows':
                os.system('python python wp_revshell.py')
        elif choice == '3':
            if system() == 'Linux':
                os.system(" chmod +x jm_revshell.py && python jm_revshell.py")
            if system() == 'Windows':
                os.system('python jm_revshell.py')
        elif choice == '00':
            print('\033[97m11. Exiting\033[1;m')
            os.system("cd ../../ && chmod +x lucille.py && python2 lucille.py")

        else:
            print('\033[1;31m[-] Invalid option!\033[1;m')


cls()
banner()

try:
	lucillex()
except KeyboardInterrupt:
    print('\033[97m\nGoing Back...\033[1;m')
    time.sleep(1)
    cls()
    os.system("cd ../../ && chmod +x lucille.py && python2 lucille.py")