#!/usr/bin/python
#-*- coding: utf-8 -*-
#Developer by Bafomet
import os,socket,requests,platform
import subprocess
import sys

# Set color
WHSL = '\033[1;32m'
ENDL = '\033[0m'
REDL = '\033[0;31m'
GNSL = '\033[1;34m'

os.system('clear')  
os.system("python2 psx.py")

def menu():
    print( """
\033[1;34m[\033[0;31m 1 \033[1;34m] \033[1;32m  Whois Lookup       \033[1;34m[\033[0;31m 8  \033[1;34m] \033[1;32m   HTTP Header                  
\033[1;34m[\033[0;31m 2 \033[1;34m] \033[1;32m  Просмотреть DNS    \033[1;34m[\033[0;31m 9  \033[1;34m] \033[1;32m   Host Finder
\033[1;34m[\033[0;31m 3 \033[1;34m] \033[1;32m  GeoIP Lookup       \033[1;34m[\033[0;31m 10 \033[1;34m] \033[1;32m   IP геолокация   
\033[1;34m[\033[0;31m 4 \033[1;34m] \033[1;32m  Subnet Lookup      \033[1;34m[\033[0;31m 11 \033[1;34m] \033[1;32m   Найти общие DNS-серверы 
\033[1;34m[\033[0;31m 5 \033[1;34m] \033[1;32m  Port сканер        \033[1;34m[\033[0;31m 12 \033[1;34m] \033[1;32m   Get Robots.txt   
\033[1;34m[\033[0;31m 6 \033[1;34m] \033[1;32m  Ссылки на страницу \033[1;34m[\033[0;31m 13 \033[1;34m] \033[1;32m   Host DNS Finder
\033[1;34m[\033[0;31m 7 \033[1;34m] \033[1;32m  Зона передачи      \033[1;34m[\033[0;31m 14 \033[1;34m] \033[1;32m   Выйти
               
          """)
    print()

def DOMIAN():

      
    try:
        
        if 1 > 2 :
              print("buffer")
        else:
            opciones()

            
    except socket.gaierror:
        DOMIAN()
    except UnboundLocalError:
        DOMIAN()
    except requests.exceptions.ConnectionError:
        exit
    except IndexError:
        print('?')
        DOMIAN()



def opciones():
    try:
        website = input(WHSL + "└──> Я жду от тебя ввод сайта"+GNSL+"[ "+REDL + "main_menu" + GNSL + " ]"+ENDL + " :")
            
            
        menu()
            
        valorselec = input(WHSL + "└──> Выбери опцию"+GNSL+"[ "+REDL + "main_menu" + GNSL + " ]"+ENDL + " :")

        if valorselec == '1':
            whois = 'https://api.hackertarget.com/whois/?q='+website
            info = requests.get(whois)
            print('\033[1;32m')
            print(info.text)
            record_resalt(info.text)           
            opciones()


        elif valorselec == '2':
            dnslook = 'https://api.hackertarget.com/dnslookup/?q='+website
            info = requests.get(dnslook)
            print('\033[1;32m')
            print(info.text)
            record_resalt(info.text) 
            opciones()

        elif valorselec == '3':
            ipgeo = 'https://api.hackertarget.com/geoip/?q='+website
            info = requests.get(ipgeo)
            print('\033[1;32m')
            print(info.text)
            record_resalt(info.text) 
            opciones()

        elif valorselec == '4':
            subnet = 'http://api.hackertarget.com/subnetcalc/?q='+website
            info = requests.get(subnet)
            print('\033[1;32m')
            print(info.text)
            record_resalt(info.text) 
            opciones()

        elif valorselec == '5':
            port = 'https://api.hackertarget.com/nmap/?q='+website
            info = requests.get(port)
            print('\033[1;32m')
            print(info.text)
            record_resalt(info.text) 
            opciones()

        elif valorselec == '6':
            pagelink = 'https://api.hackertarget.com/pagelinks/?q='+website
            info = requests.get(pagelink)
            print('\033[1;32m')
            print(info.text)
            record_resalt(info.text) 
            opciones()

        elif valorselec == '7':
            zone = 'https://api.hackertarget.com/zonetransfer/?q='+website
            info = requests.get(zone)
            print('\033[1;32m')
            print(info.text)
            record_resalt(info.text) 
            opciones()

        elif valorselec == '8':
            header = "https://api.hackertarget.com/httpheaders/?q="+website
            info = requests.get(header)
            print('\033[1;32m')
            print(info.text)
            record_resalt(info.text) 
            opciones()

        elif valorselec == '9':
            host = "https://api.hackertarget.com/hostsearch/?q="+website
            info = requests.get(host)
            print('\033[1;32m')
            print(info.text)
            record_resalt(info.text) 
            opciones()

        elif valorselec == '10':
            website = socket.gethostbyname(website)
            iplt = 'https://ipinfo.io/'+website+'/json'
            info = requests.get(iplt)
            print('\033[1;32m')
            print(info.text)
            record_resalt(info.text) 
            opciones()

        elif valorselec == '11':           
            shared = 'https://api.hackertarget.com/findshareddns/?q='+website
            info = requests.get(shared)
            print('\033[1;32m')
            print(info.text)
            record_resalt(info.text) 
            opciones()

        elif valorselec == '12':
            robots ='http://'+website+'/robots.txt'
            info = requests.get(robots)
            print('\033[1;32m')
            print(info.text)
            record_resalt(info.text) 
            opciones()

        elif valorselec == '13':
            hostdns = 'https://api.hackertarget.com/mtr/?q='+website
            info = requests.get(hostdns)
            print('\033[1;32m')
            print(info.text)
            record_resalt(info.text) 
            opciones()



        elif valorselec == '14':
            exit
            subprocess.call("sudo python3 errorlist.py", shell=True)

        elif valorselec == '14':
            exit

        else:
               
            DOMIAN()
            
    except KeyboardInterrupt:
        sys.exit()
       
		   
        

def record_resalt(resalt):
    from datetime import datetime
    
    now = datetime.now()
    data_time = "{}.{}.{}  {}:{}".format(now.day, now.month, now.year, now.hour, now.minute)
    
    with open('resalt_modul_27.txt', 'a') as file:
        file.write('\n' + '-'*30 + '\n\n' + data_time + '\n\n' + resalt + '\n')

DOMIAN()


 
        
        
        
        
        
        
        
        