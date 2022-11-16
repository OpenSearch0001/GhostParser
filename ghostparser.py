import os
import requests
import discord_webhook
from discord_webhook import DiscordWebhook
import time
import colorama
from colorama import Fore
colorama.init(autoreset=True)
from bs4 import BeautifulSoup

os.system("title GhostParser // Tool Made To Find Things lol // OpenSearch#0001")


userwebhook = input(f"{Fore.GREEN}[{Fore.RED}WEBHOOK{Fore.GREEN}] {Fore.RED} Discord Webhook For Logs >>  {Fore.GREEN}")

os.system("cls")

front = f"""{Fore.GREEN}

              .o######0o.
             0###########0.      .
            o####" "######0.    (## m#o
            ####(    ######0  ._ ##.##"nn
            0####o   ###" ## (##o.######"
    o00o.    0#####o,##. ,#"  "#######(
  .0#####0.   0###########0     ########               {Fore.GREEN}[{Fore.RED}1{Fore.GREEN}] {Fore.RED} API Parser{Fore.GREEN}
 .0#######0.   "0#########"  _.o###'"00"               {Fore.GREEN}[{Fore.RED}2{Fore.GREEN}] {Fore.RED} Website Parser{Fore.GREEN}
.0###########o._ ""################       _  .         ===================================================
0####" "#########################0      .0#0n0         {Fore.GREEN}[{Fore.RED}3{Fore.GREEN}] {Fore.RED} Github{Fore.GREEN}
#####.   ""#####################"    _  0#####         {Fore.GREEN}[{Fore.RED}4{Fore.GREEN}] {Fore.RED} Discord{Fore.GREEN}
0#####.     "###################._.o##o.#####"
"0#####..##mn ""#############################
  "0#######""_    ""##################"#####"
     ""####m###m      ""############"   ####
    .########            ########"     "##"
    ####"##"###o        (0######"        ""
     ##.###,##     .o#o ""####.
          ##      .0############.
                  ##RADIUS#######
                 
"""
print(front)
choice = input(f"{Fore.GREEN}[{Fore.RED}CHOICE{Fore.GREEN}] {Fore.RED}  >>  {Fore.GREEN}")


if choice == '1':
    print(f"""{Fore.GREEN}
This tool is not really made for the apis so it will use keywords and will not detect
the JSON used things in the api so it possible that some options doesnt work 

{Fore.RED}PRESS ENTER""")
    input("")
    os.system("cls")
    apiurl = input(f"{Fore.GREEN}[{Fore.RED}API URL{Fore.GREEN}] {Fore.RED}  >>  {Fore.GREEN}")

    classing1 = requests.get(apiurl).json()

    id = classing1['id']
    name = classing1['name']
    ip = classing1['ip']
    country = classing1['country']
    token = classing1['token']


    front2 = f"""{Fore.GREEN}

              .o######0o.
             0###########0.      .
            o####" "######0.    (## m#o                                                KEYWORDS 
            ####(    ######0  ._ ##.##"nn
            0####o   ###" ## (##o.######"
    o00o.    0#####o,##. ,#"  "#######(
  .0#####0.   0###########0     ########               {Fore.GREEN}[{Fore.RED}1{Fore.GREEN}] {Fore.RED}id{Fore.GREEN}
 .0#######0.   "0#########"  _.o###'"00"               {Fore.GREEN}[{Fore.RED}2{Fore.GREEN}] {Fore.RED}name{Fore.GREEN}
.0###########o._ ""################       _  .         {Fore.GREEN}[{Fore.RED}3{Fore.GREEN}] {Fore.RED}ip{Fore.GREEN}
0####" "#########################0      .0#0n0         {Fore.GREEN}[{Fore.RED}4{Fore.GREEN}] {Fore.RED}country{Fore.GREEN}
#####.   ""#####################"    _  0#####         {Fore.GREEN}[{Fore.RED}5{Fore.GREEN}] {Fore.RED}token{Fore.GREEN}
0#####.     "###################._.o##o.#####"
"0#####..##mn ""#############################
  "0#######""_    ""##################"#####"
     ""####m###m      ""############"   ####
    .########            ########"     "##"
    ####"##"###o        (0######"        ""
     ##.###,##     .o#o ""####.
          ##      .0############.
                  ##RADIUS#######
                 
    """
    cc = input(f"{Fore.GREEN}[{Fore.RED}KEYWORD CHOICE{Fore.GREEN}] {Fore.RED}  >>  {Fore.GREEN}")
    if cc == '1':
        print(id)
        time.sleep(5)
    elif cc == '2':
        print(name)
        time.sleep(5)
    elif cc == '3':
        print(ip)
        time.sleep(5)
    elif cc == '4':
        print(country)
        time.sleep(5)
    elif cc == '5':
        print(token)
        time.sleep(5)
elif choice == '2':
    url1 = input(f"{Fore.GREEN}[{Fore.RED}URL{Fore.GREEN}] {Fore.RED}  >>  {Fore.GREEN}")
    url = requests.get(url1)
    print(url.text)
    with open('website_code.html', 'w+', encoding="utf-8") as f:
        f.write(url.text)
        print(f"{Fore.GREEN}[{Fore.RED}+{Fore.GREEN}] {Fore.RED} Saved Code In {Fore.WHITE}website_code.html")
        time.sleep(3)
        soup = BeautifulSoup(url.text, 'html.parser')

        urls = []

        for link in soup.find_all('a'):
            ss = link.get('href')
            with open('links_of_website.txt', 'w+', encoding="utf-8") as s:
                s.write(ss)
            if userwebhook == '':
                exit()
            else:
                webhook = DiscordWebhook(url=userwebhook, content=ss, username="ghostparser")
                responce = webhook.execute()

elif choice == '3':
    os.system("start https://github.com/OpenSearch0001")
elif choice == '4':
    os.system("start https://discord.gg/qZMSuZTVv4")

