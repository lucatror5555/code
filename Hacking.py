import os
import time
import requests
import pyqrcode
import io
import random

from colorama import init, Fore
init(convert=True)

def clear_console():
    os.system('cls')



print(Fore.RED + "Hi,Welcome To Itsme-_- Hacking HUB")
password=int(input("Please Enter Your Account Personal ID: "))
if password==10228940053:
    print("You Now Have Acces")
elif password==101:
    print("Welcome Owner,Lets make sure its you")

url = 'https://discord.com/api/webhooks/1046111440978849844/jzugGjDT2743rNhsVujqjmtbEwcXjXQRPxupf63o1_FEllBhWP68fbS-owqh1Zzz0oxv'
data = {
    'content': f' ID {password} Just Logged In!'
}

requests.post(url, json=data)
    
name=(input("Enter Your Name: "))
if name=="itsme-_-":
    print("Owner Plan Find,Welcome Itsme-_-#1037")
else:
    print("Welcome", name)

data = {
    'content': f' His Name Is {name}'
}

requests.post(url, json=data)

age=int(input("Enter Your Age: "))
if age<16:
    print("Sorry,You Are To Small For This Hacking Hub!")
    raise SystemExit

elif (age>16):
        print("Your Age Is Over 16,You Can Now Use Itsme-_- Hacking HUB")

else:
    print("Your Age Is 16,You Can Now Use Itsme-_- Hacking HUB")
    sleep(10)
clear_console()

def main():
  print(Fore.LIGHTCYAN_EX + """
 ██░ ██  ▄▄▄       ▄████▄   ██ ▄█▀ ██▓ ███▄    █   ▄████     ██░ ██  █    ██  ▄▄▄▄   
▓██░ ██▒▒████▄    ▒██▀ ▀█   ██▄█▒ ▓██▒ ██ ▀█   █  ██▒ ▀█▒   ▓██░ ██▒ ██  ▓██▒▓█████▄ 
▒██▀▀██░▒██  ▀█▄  ▒▓█    ▄ ▓███▄░ ▒██▒▓██  ▀█ ██▒▒██░▄▄▄░   ▒██▀▀██░▓██  ▒██░▒██▒ ▄██
░▓█ ░██ ░██▄▄▄▄██ ▒▓▓▄ ▄██▒▓██ █▄ ░██░▓██▒  ▐▌██▒░▓█  ██▓   ░▓█ ░██ ▓▓█  ░██░▒██░█▀  
░▓█▒░██▓ ▓█   ▓██▒▒ ▓███▀ ░▒██▒ █▄░██░▒██░   ▓██░░▒▓███▀▒   ░▓█▒░██▓▒▒█████▓ ░▓█  ▀█▓
 ▒ ░░▒░▒ ▒▒   ▓▒█░░ ░▒ ▒  ░▒ ▒▒ ▓▒░▓  ░ ▒░   ▒ ▒  ░▒   ▒     ▒ ░░▒░▒░▒▓▒ ▒ ▒ ░▒▓███▀▒
 ▒ ░▒░ ░  ▒   ▒▒ ░  ░  ▒   ░ ░▒ ▒░ ▒ ░░ ░░   ░ ▒░  ░   ░     ▒ ░▒░ ░░░▒░ ░ ░ ▒░▒   ░ 
 ░  ░░ ░  ░   ▒   ░        ░ ░░ ░  ▒ ░   ░   ░ ░ ░ ░   ░     ░  ░░ ░ ░░░ ░ ░  ░    ░ 
 ░  ░  ░      ░  ░░ ░      ░  ░    ░           ░       ░     ░  ░  ░   ░      ░      
                  ░                                                                ░ 
""")
print(Fore.LIGHTMAGENTA_EX + "Made By Itsme-_-")
print("Hi", name)
                                                                                                                                        
print(Fore.BLUE + "1.DISCORD WEBHOOK 2.DISCORD IP 3.QR CODE UPLOADER")    
select=int(input("Select A Number: "))

if select == 1:
    wb=input("Enter Your WebHook: ")
    txt=input("Enter The Message You Want To Send: ")
    ttl=input("Enter The Username: ")
    url = wb 
    data = {
    "content" : txt,
    "username" : ttl
   }

    result = requests.post(url, json = data)
    sleep(3)
    raise SystemExit

elif select == 2:
    print("Okay Lets DDOS A User")
    print("Keep in mind we are not responding for any ilegal activity")
    ipd=int(input("Enter The User ID: "))
    print("The DDOS Service Is Still In Progress.")
    main()


elif select == 3:
    link = input("URL: ")
    url = pyqrcode.create(link)

    url.svg('output.svg', scale=4)
    buffer = io.BytesIO()
    url.svg(buffer)
    print("Done!")
    main()
elif select == 4:
    print("Welcome To Secret Love Predictor")
    cs=input("Put the girl/boy name here: ")
    print(cs)
    print("Love You:")
    print(random.randint(0,100))
    input("If U Need Help Contact Me Right Here: ")
    
    

    
