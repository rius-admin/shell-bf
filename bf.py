#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#Editor recode Mr.Rius

import requests, os, sys
from requests.exceptions import ConnectionError, Timeout

version = "1.0"
program_name = sys.argv[0]
lem = len(sys.argv)
result = 'result-scan-admin.txt'

usage = (f"usage : python3 {program_name} <domain>")
banner = (f"""
             ;::::;                          
           ;::::; :;                          
         ;:::::'   :;                         
        ;:::::;     ;.                        
       ,:::::'       ;           OOO      
       ::::::;       ;          OOOOO    
       ;:::::;       ;         OOOOOOOO      
      ,;::::::;     ;'         / OOOOOOO      
    ;:::::::::`. ,,,;.        /  / DOOOOOO    
  .';:::::::::::::::::;,     /  /     DOOOO   
 ,::::::;::::::;;;;::::;,   /  /        DOOO  
;`::::::`'::::::;;;::::: ,#/  /          DOOO 
:`:::::::`;::::::;;::: ;::#  /            DOOO
::`:::::::`;:::::::: ;::::# /              DOO
`:`:::::::`;:::::: ;::::::#/               DOO
 :::`:::::::`;; ;:::::::::##                OO
 ::::`:::::::`;::::::::;:::#                OO
 `:::::`::::::::::::;'`:;::#                O 
  `:::::`::::::::;' /  / `:#                  
   ::::::`:::::;'  /  /   `#

{r}The Angel Of Death {reset}- {g}Admin Finder{reset}
Version : {version}
{usage}""")


def admin_checker():
	if lem != 2:
		print(banner)
		sys.exit(0)
	else:
		domain = sys.argv[1]
		if not domain.startswith("http"):
			domain = "http://" + domain
		
		get_wordlist = "https://fooster1337.github.io/assets/wordlist.txt"
		try:
			word = requests.get(get_wordlist, timeout=10)
			word.raise_for_status()
			get_word = word.content.decode('utf-8')
		except (ConnectionError, Timeout):
			print(f"{r}Failed to retrieve wordlist. Please check your connection.{reset}")
			sys.exit(0)
		
		try:
			getStatus = requests.get(domain, timeout=10)
			getCode = getStatus.status_code
		except (ConnectionError, Timeout):
			print(f"{r}Unable to reach {domain}. Please check the domain or your connection.{reset}")
			sys.exit(0)
		
		if getCode == 200:
			print(f"Scanning : {domain}")
			print(f"Result save on {result}")
			for i in get_word.splitlines():
				dom_pls = (f"{domain}/{i}")
				try:
					rq = requests.get(dom_pls, timeout=10)
					req = rq.status_code
					if req == 200:
						print(f"{g}[Found!] {reset}-> {dom_pls} [{g}{req}{reset}]")
						with open(result, 'a') as f:
							f.write(dom_pls + "\n")
					else:
						print(f"{r}[NoLuck] {reset}-> {dom_pls} [{r}{req}{reset}]")
				except (ConnectionError, Timeout):
					print(f"{r}[Error] {reset}-> {dom_pls} [Connection/Timeout Error]")
		else:
			print(f"{r}Unknown Error : {getCode}{reset}\n{usage}")
			sys.exit(0)

if __name__ == "__main__":
	try:
		admin_checker()
	except KeyboardInterrupt:
		print(f"\n{r}Exit...{reset}")
		sys.exit(0)
	except ModuleNotFoundError:
		os.system("pip3 install requests colorama")
		admin_checker()
