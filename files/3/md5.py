import requests as s
import sys,os
import time

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
def print_logo():
        print ("""------------------------------------------------""")
        print ("""	  MD5 DEHASHER """)
        print ("""------------------------------------------------""")
def cls():
        linux = 'clear'
        windows = 'cls'
        os.system([linux, windows][os.name == 'nt'])
def decrypt():
  
    md5_hash = raw_input("\033[1;32mEnter Your MD5 hash: ")

    response = s.get("http://www.nitrxgen.net/md5db/{}".format(md5_hash)).text

    if response != "":
        print("\033[92m[+]Md5({})= {}".format(md5_hash, response)+"\n\n\n\nUse another tool ?\n")
    else:
        print("[\033[91m-] Md5({}) NOT FOUND.".format(md5_hash)+"\n\n\n\n")

cls()
print_logo()
try:
  decrypt()
except KeyboardInterrupt:
    print('\033[97m\nGoing Back...\033[1;m')
    time.sleep(1)
    cls()
    os.system(" chmod +x exploit.py && python2 exploit.py")