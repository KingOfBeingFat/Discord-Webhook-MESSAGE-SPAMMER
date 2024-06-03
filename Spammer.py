import discord_webhook
from discord_webhook import DiscordEmbed, DiscordWebhook
import string
import random
import time
import requests
import colorama
from colorama import Fore

colorama.init()

print("""
              ,AAAAAAAA,
             .8888888888b
             888888888888nd8P~''8g,
             88888888888888   _  `'~\.  .n.
             `Y888888888888. / _  |~\\ (8"8b
            ,nnn.. 8888888b.  |  \ \m\|8888P
          ,d8888888888888888b. \8b|.\P~ ~P8~
          888888888888888P~~_~  `8B_|      |
          ~888888888~'8'   d8.    ~      _/
           ~Y8888P'   ~\ | |~|~b,__ __--~
       --~~\   ,d8888888b.\`\_/ __/~
            \_ d88888888888b\_-~8888888bn.
              \8888P   "Y888888888888"888888bn.
           /~'\_"__)      "d88888888P,-~~-~888
          /  / )   ~\     ,888888/~' /  / / 8'
       .-(  / / / |) )-----------(/ ~  / /  |---.
______ | (   '    /_/    MADE     (__/     /   |_______
\      |   (_(_ ( /~      By       \___/_/'    |      /
 \     |               KING ;}!                |     /
 /     (________________________________________)     \
/__________)                                (__________\
WEB HOOK SPAM                               WEB HOOK SPAM
      King's Special Tools To Annoy Friends (Only)


""")

def webhkspammer():
    webhook = input(Fore.YELLOW + "-> Enter The Webhook Link: ")
    message = input(Fore.GREEN + "--> Enter The Message: ")
    delay = float(input(Fore.RED + "---> Enter The Delay Between Messages: "))

    while True:
        print(Fore.BLUE + "Sending --> " + message)
        try:
            time.sleep(delay)
            response = requests.post(webhook, json={'content': message})

            if response.status_code == 204:
                print(Fore.GREEN + "Sent --> " + message)
            else:
                print(Fore.RED + "Failed to send message. Status code: " + str(response.status_code))
        except Exception as e:
            print(Fore.RED + "An error occurred: " + str(e))
            time.sleep(5)
            exit()

if __name__ == "__main__":
    webhkspammer()
