import os,sys
import time
import random
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

def clearScr():
    os.system('clear')

def logo():
        clear = "\x1b[0m"
        colors = [36, 32, 34, 35, 31, 37  ]

        x = """ 


	$$\      $$\   $$\  $$$$$$\  $$$$$$\ $$\       $$\       $$$$$$$$\ 
	$$ |     $$ |  $$ |$$  __$$\ \_$$  _|$$ |      $$ |      $$  _____|
	$$ |     $$ |  $$ |$$ /  \__|  $$ |  $$ |      $$ |      $$ |      
	$$ |     $$ |  $$ |$$ |        $$ |  $$ |      $$ |      $$$$$\    
	$$ |     $$ |  $$ |$$ |        $$ |  $$ |      $$ |      $$  __|   
	$$ |     $$ |  $$ |$$ |  $$\   $$ |  $$ |      $$ |      $$ |      
	$$$$$$$$\\$$$$$$  |\$$$$$$  |$$$$$$\ $$$$$$$$\ $$$$$$$$\ $$$$$$$$\ 
	\________|\______/  \______/ \______|\________|\________|\________|																													                 																						
      		Note! : I'm Not Responsible for any illegal usage.
        	Coded by : Jason13
		Contact me : xtnjason@gmail.com


[+] 1. Information Gathering
[+] 2. Password Attacks
[+] 3. Exploitation Tools
[+] 4. Post Exploitation
[+] 5. About me
[+] 00. EXIT
			                  """
        for N, line in enumerate(x.split("\n")):
            sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
            time.sleep(0.05)						  
clearScr()
logo()

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; rv:57.0) Gecko/20100101 Firefox/57.0"}
luc = input("root@lucille:~# ")
clearScr()
class choices():
	def infomenu(self):
		if system() == 'Linux':
			os.system("cd files/1 && chmod +x infgathering.py && python infgathering.py")
		if system() == 'Windows':
			os.system('cd files/1 && infgathering.py')

	def passmenu(self):
		if system() == 'Linux':
			os.system("cd files/2 && chmod +x brute.py && python2 brute.py")
		if system() == 'Windows':
			os.system('cd files/2 && brute.py')
		
		choice2 = input("root@lucille:~# ")

	def exploitmenu(self):
		if system() == 'Linux':
			os.system("cd files/3 && chmod +x exploit.py && python2 exploit.py")
		if system() == 'Windows':
			os.system('cd files/3 && exploit.py')
		

	def postmenu(self):

		if system() == 'Linux':
			os.system("cd files/4 && chmod +x postexp.py && python2 postexp.py")
		if system() == 'Windows':
			os.system('cd files/4 && postexp.py')

	def aboutme(self):
		if system() == 'Linux':
			os.system("cd files && chmod +x aboutme.py && python2 aboutme.py")
		if system() == 'Windows':
			os.system('cd files && aboutme.py')

	def exitluc(self):
		print('\033[97m\nClosing Lucille\nPlease Wait...\033[1;m')
		time.sleep(2)
		sys.exit()

ch = choices()
if luc == '1':
	ch.infomenu()
elif luc == '2':
	ch.passmenu()
elif luc == '3':
	ch.exploitmenu()
elif luc == '4':
	ch.postmenu()
elif luc == '5':
	ch.aboutme()
elif luc == '00':
	ch.exitluc()
else:
	print("Invalid Input!")
	

    