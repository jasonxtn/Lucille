#!/usr/bin/python
 # -*-coding:Latin-1 -*					
import sys, re, os



def cls():
        linux = 'clear'
        windows = 'cls'
        os.system([linux, windows][os.name == 'nt'])
def print_logo():
        print ("""------------------------------------------------""")
        print ("""	  WEB SHELL CHECKER """)
        print ("""------------------------------------------------""")

cls()
print_logo()

cls()
print_logo()

port = input("Enter a port number: ")
command = f"nc -lnvp {port}"
os.system(command)
