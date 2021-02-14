# <With this tool, you can find the sections on a web page>
import subprocess
import sys
import os
import requests
import time
from colorama import Fore , init , Style , Back
#list page defolte
D_Page = ['robots.txt','search/','admin/','login/','sitemap.xml','sitemap2.xml','config.php','wp-login.php','log.txt','update.php','INSTALL.pgsql.txt','user/login/','INSTALL.txt','profiles/','scripts/','LICENSE.txt','CHANGELOG.txt','themes/','inculdes/','misc/','user/logout/','user/register/','cron.php','filter/tips/','comment/reply/','xmlrpc.php','modules/','install.php','MAINTAINERS.txt','user/password/','node/add/','INSTALL.sqlite.txt','UPGRADE.txt','INSTALL.mysql.txt']
#--==--==--==--==--Variable--==--==--==--==-----------------------------------------------------------------------------------------------------------------------------------------------------------
R  = Fore.RED
LR = Fore.LIGHTRED_EX
G  = Fore.GREEN
LG = Fore.LIGHTGREEN_EX
W  = Fore.LIGHTWHITE_EX
Y  = Fore.YELLOW
LY = Fore.LIGHTYELLOW_EX
B  = Fore.BLUE
LB = Fore.LIGHTBLUE_EX
C  = Fore.CYAN
LC = Fore.LIGHTCYAN_EX
baner = (Fore.LIGHTYELLOW_EX + '██╗  ██████╗  ██╗\n'+'██║ ██╔════╝  ██║\n'+'██║ ██║  ███╗ ██║\n'+'╚═╝ ██║   ██║ ╚═╝\n'+'██╗ ╚██████╔╝ ██╗\n'+'╚═╝  ╚═════╝  ╚═╝\n')
ENTERIN =(str( LC + "┌─⫣⫼ " + R + "!" + LG + "G" + R + "!" + W + "/" + LR + "CloudeFlare" + W + "/" + G + "@A" + LC + " ⫼" + LC + "\n└──⫸  ⫻   "))
#Fungtion-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def __RPE__():
    os.system("echo off" and "cls")
    # print( LB + "Enter your URdL")
    # _Si_te = str(input(ENTERIN + LG))
    # print( LB + "Enter your list address to check")
    # Address_L = str(input(ENTERIN + LG))
    # Address_L = subprocess.check_output(Address_L)
    # TXlist = open(Address_L).readline
    # # TXlist = TXlist.split()
    # print(TXlist)
#Fungtion-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def __DPE__():
    os.system("echo off" and "cls")
    print( LB + "Enter your URL")
    _Si_te = str(input(ENTERIN + LG))
    if _Si_te == "" :
        try :
            print(R + "[!] " + LR +"Please enter an address" + R + " [!]" +W)
            time.sleep(3)
            sys.exit
        except :
            return    
    
    URL = "https://"+_Si_te+"/"
    for _Existence_ in D_Page :
        PageX = requests.get(URL+_Existence_)
        Scode = str(PageX.status_code)
        if Scode[0] == '2':
            print(G + "[+] |" + LG + URL+_Existence_ +G+ '| >>>' + LG + _Existence_ + G + "| [+] \n")
        else:
            print(R + "[-] |" + LR + URL+_Existence_ +R+ '| >>>' + LR + _Existence_ + R + "| [-] \n")
    input (W + "[*] It's over. 'Enter' to return to menu [*]")
    # __menu__()
               
        
    
#Fungtion-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def __SPE__():
    os.system("echo off" and "cls")
    print(baner + "\n\n")
    print (R + " [?] " + B + "With this tool, you can find the sections on a web page" + R + " [?] \n")
    print(C + 'If you want to do so as requested, type the word '+  LY + '"--requested"' + C + '\n' + LC + '   (With this choice, you will find your own)\n' + W)
    select = str(input())
    if select == "--requested":
        __RPE__()
    else:
        __DPE__()    
#_start--------------------------------------------------------------------------------------------------------------------------------------
# *******************************************************************************************************************************************        
os.system("echo off" and "cls")
try:
    __SPE__()
except:
    time.sleep(0.5)
    W
    sys.exit()            




































































































