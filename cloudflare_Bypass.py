import os
import sys
import socket
import time
from colorama import Fore , init , Style , Back

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
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
def __CB__():
    os.system( "echo off" and "cls" )
    _sub_ = ['ftp', 'cpanel', 'webmail', 'localhost', 'local', 'mysql' , 'forum', 'driect-connect', 'blog', 'vb', 'forums', 'home', 'direct', 'forums', 'mail', 'access', 'admin', 'administrator', 'email', 'downloads', 'ssh', 'owa', 'bbs', 'webmin', 'paralel', 'parallels', 'www0', 'www', 'www1', 'www2', 'www3', 'www4', 'www5', 'shop', 'api', 'blogs', 'test', 'mx1', 'cdn', 'mysql', 'mail1', 'secure', 'server', 'ns1', 'ns2', 'smtp', 'vpn', 'm', 'mail2', 'postal', 'support', 'web', 'dev']
    print ( baner )
    print ( Y + " ⁂ welcom in the bypass cloude flare ⁂ \n\n" +
    LR + "⇛     " + C + "Using the protocols on the site, this tool \n      brings their ip to the right and passes through it \n      if the site has clude flare." + LR + "     ⇚\n\n" + Fore.WHITE)
    print( R + "[!]" + B + "Please enter the site address" + R + "[!]\n") 
    web_site = input(ENTERIN + G)
    if web_site == "" :
        try:
            print( R + "[!]" +  LG + "You have not entered any addresses, re-enter." + R + "[!]")
            time.sleep(3)
            sys.exit
        except :
            return
    
    
    for  subdomin in _sub_ :
        try:
            IP_CLB = str(subdomin) + (".") + str(web_site)
            _BE_ = socket.gethostbyname (IP_CLB)
            print ( R + "Original IP is : ‖ " +  LB + (_BE_) + R + " ‖ " + G + "⇨  " + R + "Address: ‖ " + LB + (IP_CLB) + R + " ‖ " +W+"\n")   
        except:
            pass
    
    input (W + "[*] It's over. 'Enter' to return to menu [*]")
    # __menu__()
os.system("echo off" and "cls")
try:
    __CB__()
except:
    time.sleep(0.5)
    W
    sys.exit()
   