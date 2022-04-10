# -*- coding: utf-8 -*-
# Dependencies

import requests
import sys
from os import path, system, getcwd, getenv, startfile
from re import compile
from distutils.spawn import find_executable

import imp
# from os import system as terminal 
# from clint.textui import progress
# import urllib3

text = '''

\t .----------------.  .----------------.  .----------------.  .----------------.  .----------------. 
\t| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
\t| | ____    ____ | || |      __      | || |  ___  ____   | || |  _________   | || |  _______     | |
\t| ||_   \\  /   _|| || |     /  \\     | || | |_  ||_  _|  | || | |_   ___  |  | || | |_   __ \\    | |
\t| |  |   \\/   |  | || |    / /\\ \\    | || |   | |_/ /    | || |   | |_  \\_|  | || |   | |__) |   | |
\t| |  | |\\  /| |  | || |   / ____ \\   | || |   |  __'.    | || |   |  _|  _   | || |   |  __ /    | |
\t| | _| |_\\/_| |_ | || | _/ /    \\ \\_ | || |  _| |  \\ \\_  | || |  _| |___/ |  | || |  _| |  \\ \\_  | |
\t| ||_____||_____|| || ||____|  |____|| || | |____||____| | || | |_________|  | || | |____| |___| | |
\t| |              | || |              | || |              | || |              | || |              | |
\t| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
\t '----------------'  '----------------'  '----------------'  '----------------'  '----------------' 

'''

print(text)

wamp_url         = f"https://sourceforge.net/projects/wampserver/files/WampServer%203/WampServer%203.0.0/wampserver3.2.6_x64.exe/download"
#https://sourceforge.net/projects/wampserver/files/latest/download
#f"https://downloads.sourceforge.net/project/wampserver/WampServer%203/WampServer%203.0.0/wampserver3.1.9_x64.exe?r=https%3A%2F%2Fsourceforge.net%2Fprojects%2Fwampserver%2Ffiles%2FWampServer%25203%2FWampServer%25203.0.0%2Fwampserver3.1.9_x64.exe%2Fdownload&ts=1561144501"
#firefox      = f"https://download.mozilla.org/?product=firefox-stub&os=win&lang=ru"

file_firefox = 'firefox.exe'
file_wamp    = 'wamp.exe'

wamp_ans = "Are you want do Download wamp"

var_path     = getenv("PATH")
current_path = getcwd() #system("echo  %cd%")




try:
    imp.find_module('requests')
    found = True
except ImportError:
    found = False
#print(found)

def is_downloadable(url):    
    # Does the url contain a downloadable resource    
    h = requests.head(url, allow_redirects=True)
    header = h.headers
    content_type = header.get('content-type')
    if 'text' in content_type.lower():
        return False
    if 'html' in content_type.lower():
        return False
    return True


def download(url, filename):    
   with open(filename, 'wb') as f:
       response = requests.get(url, stream=True)
       print(response)
       total = response.headers.get('content-length')
       if total is None:
           f.write(response.content)
       else:
           downloaded = 0
           total = int(total)
           for data in response.iter_content(chunk_size=max(int(total/1000), 1024*1024)):
               downloaded += len(data)
               f.write(data)
               done = int(50*downloaded/total)
               sys.stdout.write('\r\t[{}{}]'.format('█' * done, '.' * (50-done)))
               sys.stdout.flush()              
   sys.stdout.write('\n')
   sys.stdout.write("\tComplete.\n")


def running_wamp():
    system("\necho \tRunning Wamp . . .")
    #startfile(f"{current_path}\\{file_wamp}")
    #command poused cli process until wamp instalation gui is running
    system(rf"{current_path}\\{file_wamp}") 



def fine_process():
    print("\n\tAll have done. Productive day . . . \n")
    print("\t© Created by ♡ | Eric ")
    input("\t")


def config_wamp():
    
    if( path.isdir("C:\\wamp64") ):
        
        httpd_conf = "C:\\wamp64\\bin\\apache\\apache2.4.39\\conf"
        httpd_vhost = "C:\\wamp64\\bin\\apache\\apache2.4.39\\conf\\extra"
        
        system(f"COPY {httpd_conf}\\httpd.conf  {httpd_conf}\\httpd.conf.bcp ")
        system(f"COPY {httpd_vhost}\\httpd-vhosts.conf  {httpd_vhost}\\httpd-vhosts.conf.bcp ")

        print("\tMaking a windows path variable for php . . .")
        print("\tAvailable versions of php is - 5.6.40, 7.0.33, 7.1.29, 7.2.18, 7.3.5")
        print("\tInput the version of php for create the windows path, by default will be maked the latest version")
        php_vers = input("\tPHP version:")

        def notice_php():
            print("\tPHP path is set to windows environment 'path' variable ")
            print("\tClose terminal (cmd) and open again for use php, for test type 'php --version'")

        
        # def check_php(vers):

        #     if(vers == ""):
        #         empty_string = compile(rf"C\:\\wamp64\\bin\\php\\php7.3.5")
        #         return empty_string
        #     else:
        #         versions = compile(rf"C:\\wamp64\\bin\\php\\{vers}") 
        #         return versions


        #fine process()

        # def mysql_config():

        #     regexp_mysql = compile(r"C:\\wamp64\\bin\\mysql\\mysql5.7.26\\bin")

        #     if( regexp_mysql == False ):

        #         print("\tMaking a windows path variable for mysql . . . ")
        #         system(f"\tsetx Path \"%PATH%;C:\\wamp64\\bin\\mysql\\mysql5.7.26\\bin\"")        
        #         print("\tComplate making system variable for mysql vesion 5.7.26 ")
        #         fine_process()


        if( php_vers == "" or php_vers == None ): 
            # regexp_php = check_php( php_vers )
            # print(regexp_php)
            # if( regexp_php.search(var_path) == False  ):

            system(f"setx Path \"C:\\wamp64\\bin\\php\\php7.3.5;C:\\wamp64\\bin\\mysql\\mysql5.7.26\\bin\"")
            notice_php()
            system("exit")
            # mysql_config()
            # else:
                # print("php variable is exists")

        else:
            # check_php(php_vers)
            system(f"setx Path \"C:\\wamp64\\bin\\php\\php{php_vers};C:\\wamp64\\bin\\mysql\\mysql5.7.26\\bin\"")
            notice_php()
            system("exit")

            # mysql_config()
            # Path system variable value -   %SystemRoot%\system32;%SystemRoot%;%SystemRoot%\System32\Wbem;%SYSTEMROOT%\System32\WindowsPowerShell\v1.0\;C:\wamp64\bin\php\php7.3.5;C:\composer;C:\Program Files\TortoiseHg\;C:\Program Files\nodejs\;C:\Users\eric\AppData\Local\Programs\Python\Python36\;C:\Users\eric\AppData\Local\Programs\Python\Python36\Scripts\;C:\Program Files\Git\cmd;%SYSTEMROOT%\System32\OpenSSH\;C:\xampp\mysql\bin;

       
def ask_user(quession):
    check = str(input(quession+ '(Y/N): ')).lower().strip()
    try:
        if check[0] == 'y':
            return True
        elif check[0] == 'n':
            return False
        else:
            print('Invalid Input')
            ask_user(quession)
    except Exception as error:
        print("Please enter valid inputs")
        print(error)
        ask_user(quession)       


def is_tool( name ):
    return find_executable(name) is not None        


    
            



# Body of process

## WAMP

def wamp():
    
    if ( not path.isdir("C:\\wamp64") ):
        
        if ( is_downloadable(wamp_url) ):
            if ( path.isfile(f"{current_path}\\{file_wamp}") ):  
                running_wamp()
                sys.stdout.flush()
                #config_wamp()
    
            else:    
                print("\tWamp Downloading . . .\n")
                download( wamp_url, file_wamp )
                running_wamp()
                sys.stdout.flush()
                config_wamp()
    
            # installation process complate , make configure wamp server , create virtual host code . . .
    else:

        system("echo \twamp directory exists in path C:\\ ")
        print("\tConfigure Wamp apache virtual host and make windows path variables . . . ")
        config_wamp()






wamp()
fine_process()
