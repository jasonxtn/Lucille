import os,sys,time
BOLD = "\033[1m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
RESET = "\033[0m"
def cls():
        linux = 'clear'
        windows = 'cls'
        os.system([linux, windows][os.name == 'nt'])
cls()
        
about_me = '''\n\nLucille is a penetration testing application dedicated to security testing of web applications.
This application provides a comprehensive suite of user-friendly tools to detect potential flaws and vulnerabilities
in web applications. The project was undertaken as part of my studies in cybersecurity and aims to provide a practical
and effective tool for cybersecurity professionals..\n\n'''

about_me_lines = about_me.split("\n")

print(GREEN + "===============================================================================" + RESET)
print(BOLD + YELLOW + "                        ABOUT " + RESET)
print(GREEN + "===============================================================================" + RESET)

for line in about_me_lines:
    print(BOLD + line + RESET)

print(GREEN + "================================================================================\n" + RESET)
print(YELLOW + BOLD +"Lucille Current Version : 2.0\nContact me via email : xtnjason@gmail.com" + RESET)


abt = raw_input("\nPress Enter to go back ...")
if abt == "":
    print('\033[97m\nGoing Back...\033[1;m')
    time.sleep(1)
    cls()
    os.system("cd ../ && chmod +x lucille.py && python2 lucille.py")