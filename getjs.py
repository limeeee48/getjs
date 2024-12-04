import  requests , sys 
from bs4 import BeautifulSoup as bs
from datetime import datetime 
def banner():
	print("-"*20)
	print("getjs v1.1\nby lime".upper())	
	print("-"*20)
dt_now = datetime.now()
dt_all = (f"{dt_now.month}-{dt_now.day}-{dt_now.year}:{dt_now.hour}:{dt_now.minute}:{dt_now.second}")	
full_name = (f"{dt_all}.txt")
reqsession = requests.session()
try : 
	if sys.argv[1] == str("--url"):
		print("")
		banner()
		getreq = reqsession.get(f"http://{sys.argv[2]}")
		soup = bs(getreq.text , "html.parser")
		findscript = soup.find_all("script")
		get_src = [script["src"] for script in findscript if "src" in script.attrs ]
		with open(full_name , "x") as mksave : 
			print("")
			for src in get_src :
				fullurl = f"http://{sys.argv[2]}/{src}"
				getjspage = reqsession.get(fullurl)
				if getjspage.status_code == 200 or getjspage.status_code == 403 :
					print(f"Found : {getjspage.url}")
					manyequal = "="*50
					mksave.write(f"\n\njavascript file : {src}\nurl : {getjspage.url}\n\n{getjspage.text}{manyequal}")
		eq = "="*40
		print(f"\n{eq}")
		print("")
		print(f"saved to : {full_name}")
	elif sys.argv[1] == str("--help") : 
		print("")
		banner()
		print("")
		print("getjs [options] <url>")
		print("")
		print("="*15 ,"tips".upper() ,"="*15)
		print(" <options> : tool option like (--url) ")
		print(" <url> : Only Url without http:// or https:// ")
		print("")
		print("="*15 ,"options".upper() ,"="*15)
		print(" --url <domain> : to search javascript files in domain")
	else : 
		print("")
		banner()
		print("")
		print(f" ERROR: Invaild Option : {sys.argv[1]}")
		print(f" Try: (--help) to get help")
except : 
	print("")
	banner()
	print("")
	print(f" Try: (--help) to get help")
	
