from requests import get, post
import time
import json
import os

logo = """
dP     dP                                      .d88888b  dP                dP dP 
88     88                                      88.    "' 88                88 88    By iBlaze
88aaaaa88a .d8888b. 88d888b. .d8888b. dP    dP `Y88888b. 88d888b. .d8888b. 88 88   
88     88  88'  `88 88'  `88 88ooood8 88    88       `8b 88'  `88 88ooood8 88 88    View your honeygain data from the terminal!
88     88  88.  .88 88    88 88.  ... 88.  .88 d8'   .8P 88    88 88.  ... 88 88 
dP     dP  `88888P' dP    dP `88888P' `8888P88  Y88888P  dP    dP `88888P' dP dP 
                                           .88                                   
                                       d8888P
"""

if not os.path.exists('info.txt'):
    print(logo)
    print("First time use detected!")
    print("")
    email = input("Your Honeygain Email : ")
    password = input("Your Honeygain Password : ")
    gettoken = post("https://dashboard.honeygain.com/api/v1/users/tokens", json={'email': email,'password': password}).json()['data']
    w = open('info.txt', 'w')
    w.write(gettoken["access_token"])
    w.close()
    print("Setup Done!")

with open('info.txt', 'r') as file:
    token = file.read().rstrip()

clearConsole = lambda: print('\n' * 150)
shorttoken = token[:75] + (token[75:] and ' ...')

while(True == True):
    time.sleep(5)
    clearConsole()
    aboutme = get("https://dashboard.honeygain.com/api/v1/users/me",headers={'authorization': ("Bearer " + token)}).json()['data']
    balances = get("https://dashboard.honeygain.com/api/v1/users/balances",headers={'authorization': ("Bearer " + token)}).json()['data']
    realtime = balances["realtime"]
    payout = balances["payout"]
    min_payout = balances["min_payout"]
    print(logo)
    print("Current Token  " + shorttoken)
    print("Total Devices : {}".format((aboutme["total_devices"])))
    print("Active Devices : {}".format((aboutme["active_devices_count"])))
    print("")
    print("Balance : {} / {}".format((payout["credits"]),min_payout["credits"]))
    print("Earned Today : {} ".format((realtime["credits"])))
