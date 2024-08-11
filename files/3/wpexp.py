import os
import sys
import subprocess
import threading
import random
import time


def cls():
        linux = 'clear'
        windows = 'cls'
        os.system([linux, windows][os.name == 'nt'])
def print_logo():
        print ("""------------------------------------------------""")
        print ("""	  WP SCAN TOOL """)
        print ("""------------------------------------------------""")

cls()
try:
    print("\033[1m\033[33m\n[+] Note : This tool hasn't been completed yet.\nI hope it will be available soon.")    
    print("\033[1;34mInstead, I will open the integrated WPScan Tool\033[0m\n")
    print_logo()
    url = input("\n\033[1;31mEnter the URL to scan: \033[0m")
    wpscan_command = "wpscan --url {} ".format(url)
    print("Opening WPScan tool. Please wait...")
    time.sleep(3)  
    os.system(wpscan_command)
except KeyboardInterrupt:
    print('\033[97m\nGoing Back...\033[1;m')
    time.sleep(1)
    cls()
    sys.exit()
    os.system(" chmod +x exploit.py && python2 exploit.py")
      