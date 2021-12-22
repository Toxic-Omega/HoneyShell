from requests import get, post
import time
import json
import os

logo = """
\033[93mdP     dP                                      \033[32m.d88888b  dP                dP dP 
\033[93m88     88                                      \033[32m88.    "' 88                88 88   \033[31m By iBlaze
\033[93m88aaaaa88a .d8888b. 88d888b. .d8888b. dP    dP \033[32m`Y88888b. 88d888b. .d8888b. 88 88   
\033[93m88     88  88'  `88 88'  `88 88ooood8 88    88 \033[32m      `8b 88'  `88 88ooood8 88 88   \033[31m View your honeygain data from the terminal!
\033[93m88     88  88.  .88 88    88 88.  ... 88.  .88 \033[32md8'   .8P 88    88 88.  ... 88 88 
\033[93mdP     dP  `88888P' dP    dP `88888P' `8888P88 \033[32m Y88888P  dP    dP `88888P' dP dP 
\033[93m                                           .88                                   
\033[93m                                       d8888P

"""

if not os.path.exists('info.txt'):
    print(logo)
    print("First time use detected!")
    print("")
    email = input("Your Honey Email : ")
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
    print("\033[33mCurrent Token \033[37m:\033[91m " + shorttoken)
    print("\033[33mTotal Devices \033[37m:\033[91m {}".format((aboutme["total_devices"])))
    print("\033[33mActive Devices \033[37m:\033[91m {}".format((aboutme["active_devices_count"])))
    print("")
    print("\033[33mBalance \033[37m:\033[91m {} \033[37m/ \033[91m{}".format((payout["credits"]),min_payout["credits"]))
    print("\033[33mEarned Today \033[37m:\033[91m {} ".format((realtime["credits"])))
