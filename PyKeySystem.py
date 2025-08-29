
#this is a simple script for review, you can modify it as you wish, there are no special protections, etc., so I do not recommend using it in this form in real projects

from time import sleep
from turtledemo.penrose import start

import requests
import os
import sys
import urllib3
import random
import string


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

if not sys.stdout.isatty():
    os.system('start cmd /K python "' + sys.argv[0] + '"')
    sys.exit()

os.system('cls')

cando = 0
welcome_file = 'about.txt'
text = 0
red_color = '\033[91m'
reset = '\033[0m'
green_color = '\033[92m'




print("=== shaurmaEnjoyer ===")
print()


print(f"creating {welcome_file} file...")
sleep(3)
lines = [
    "simple valid key Check system",
    "this is a simple script for review,",
    "you can modify it as you wish,",
    "there are no special protections, etc.,",
    "so I do not recommend using this code in this form in real projects"
]

with open(welcome_file, 'w') as f:
    f.write('\n'.join(lines))
os.system(f'start {welcome_file} ')



headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
}

print(f'continue? {green_color}1{reset}- yes {red_color}2{reset}- no')
Welcome = int(input())
if Welcome == 2:
    sys.exit()
else:
    print('ok')

#I recommend using the hastebin site, because I had problems with pastebin
website_url = "https://hastebin.skyra.pw/"
random_adr = ''.join(random.choices(string.ascii_lowercase, k=10))
base_url = website_url.split('/raw/', 1)[0] + f"/raw/{random_adr}/"

print(f"sending a request: {base_url}")

try:
    response = requests.get(website_url, headers=headers, verify=False)
    print(f"response status: {response.status_code}")

    if response.status_code == 200:
        valid_codes = [code.strip() for code in response.text.split('\n') if code.strip()]
        print(f"\033[91mdebug information, remove it if you don't need it\033[0m")
        print(f"receipt codes: {len(valid_codes), response.text }")
        print(f"\033[91m______________\033[0m")


        user_code = input("Enter your code: ").strip()
        print(f"code entered: {user_code}")

        if user_code in valid_codes:
            print(f"response status: 200 - {green_color}ok{reset}")
            cando = 1

        else:
            print(f"false - {red_color}was not found{reset}")
    else:
        print(f"{red_color}Error get{reset}: {red_color}{response.text}{reset}")
        print(f"{red_color}was not found{reset}")

except Exception as e:
    print(f"Error: {e}")
    print("false")

#this opens a browser and a link, you can enter a static browser name or ask the user to enter it, you can replace it with opening some program
#example:
#'start cmd' XD

if cando == 1:
    print(f"start? {green_color}1{reset}- yes {red_color}2{reset}- no")
    user_response = input(':')
    if user_response.__str__() == '1':
        print('enter file name')
        process = input(':')
        print('starting:', process)
        os.system(f'start {process} /K https://youtu.be/GJHQc2Aa3VI')
    else:
        print('get out!')

input("\nPress enter to continue...")

