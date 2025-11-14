# Copyright (c) 2025 v4lkyr0/v4lkyr_
# See LICENSE file for details

from Programs.Plugins.Utils import *
from Programs.Plugins.Config import *

try:
    import time
    import sys
except Exception as e:
    MissingModule(e)

Title("Main Menu")

def Connection():
    try:
        requests.get("https://www.google.com", timeout=5)
        pass
    except:
        print(f"{ERROR} An internet connection is required to use {name_tool}-Tool!", reset)
        Continue()
        sys.exit()

Connection()

def Menu():
    update    = Update()
    interface = f"""{update}
                          ▄▄▄▄    █    ██  ██▓ ██▓    ▓█████▄  █     █░ ▄▄▄       ██▀███  ▓█████  
                         ▓█████▄  ██  ▓██▒▓██▒▓██▒    ▒██▀ ██▌▓█░ █ ░█░▒████▄    ▓██ ▒ ██▒▓█   ▀  
                         ▒██▒ ▄██▓██  ▒██░▒██▒▒██░    ░██   █▌▒█░ █ ░█ ▒██  ▀█▄  ▓██ ░▄█ ▒▒███   
                         ▒██░█▀  ▓▓█  ░██░░██░▒██░    ░▓█▄   ▌░█░ █ ░█ ░██▄▄▄▄██ ▒██▀▀█▄  ▒▓█  ▄  
                         ░▓█  ▀█▓▒▒█████▓ ░██░░██████▒░▒████▓ ░░██▒██▓  ▓█   ▓██▒░██▓ ▒██▒░▒████▒ 
                         ░▒▓███▀▒░▒▓▒ ▒ ▒ ░▓  ░ ▒░▓  ░ ▒▒▓  ▒ ░ ▓░▒ ▒   ▒▒   ▓▒█░░ ▒▓ ░▒▓░░░ ▒░ ░ 
                         ▒░▒   ░ ░░▒░ ░ ░  ▒ ░░ ░ ▒  ░ ░ ▒  ▒   ▒ ░ ░    ▒   ▒▒ ░  ░▒ ░ ▒░ ░ ░  ░ 
                          ░    ░  ░░░ ░ ░  ▒ ░  ░ ░    ░ ░  ░   ░   ░    ░   ▒     ░░   ░    ░    
                          ░         ░      ░      ░  ░   ░        ░          ░  ░   ░        ░  ░ 
{red}> {PREFIX}?{SUFFIX} {version_tool} Changelog            ░                       ░                                            {white}Exit {name_tool} {PREFIX}E{SUFFIX} {red}<
{red}> {PREFIX}!{SUFFIX} Tool Information                                                                                 Tokens File {PREFIX}F{SUFFIX} {red}<

╓──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╖
                                        {github_url}
╙──┬──────────────────────────────────────┬──────────────────────────────────────┬─────────────────────────────────────╜
   ├─ {PREFIX1}01{SUFFIX1} Discord Token Information      ├─ {PREFIX1}11{SUFFIX1} Discord Token House Changer    ├─ {PREFIX1}21{SUFFIX1} Discord Token Mass Dm
   ├─ {PREFIX1}02{SUFFIX1} Discord Token Login            ├─ {PREFIX1}12{SUFFIX1} Discord Token Theme Changer    ├─ {PREFIX1}22{SUFFIX1} Discord Token Delete Dm
   ├─ {PREFIX1}03{SUFFIX1} Discord Token Onliner          ├─ {PREFIX1}13{SUFFIX1} Discord Token Joiner           ├─ {PREFIX1}23{SUFFIX1} Discord Id To Token
   ├─ {PREFIX1}04{SUFFIX1} Discord Token Generator        ├─ {PREFIX1}14{SUFFIX1} Discord Token Leaver           ├─ {PREFIX1}24{SUFFIX1} Discord Snowflake Decoder
   ├─ {PREFIX1}05{SUFFIX1} Discord Token Disabler         ├─ {PREFIX1}15{SUFFIX1} Discord Server Information     ├─ {PREFIX1}25{SUFFIX1} Discord Bot Id To Invite
   ├─ {PREFIX1}06{SUFFIX1} Discord Token Bio Changer      ├─ {PREFIX1}16{SUFFIX1} Discord Token Nuker            ├─ {PREFIX1}26{SUFFIX1} Discord Webhook Information
   ├─ {PREFIX1}07{SUFFIX1} Discord Token Alias Changer    ├─ {PREFIX1}17{SUFFIX1} Discord Token Delete Friends   ├─ {PREFIX1}27{SUFFIX1} Discord Webhook Generator
   ├─ {PREFIX1}08{SUFFIX1} Discord Token CStatus Changer  ├─ {PREFIX1}18{SUFFIX1} Discord Token Block Friends    ├─ {PREFIX1}28{SUFFIX1} Discord Webhook Spammer
   ├─ {PREFIX1}09{SUFFIX1} Discord Token Pfp Changer      ├─ {PREFIX1}19{SUFFIX1} Discord Token Unblock Users    ├─ {PREFIX1}29{SUFFIX1} Discord Webhook Deleter
   └─ {PREFIX1}10{SUFFIX1} Discord Token Language Changer └─ {PREFIX1}20{SUFFIX1} Discord Token Spammer          └─ {PREFIX1}30{SUFFIX1} Discord Nitro Generator"""
    return interface

while True:
    try:
        Clear()

        interface = Menu()
        Scroll(Gradient(interface))

        choice = input(f"{PREFIX}{username_pc}@{name_tool}{SUFFIX} {red}->{reset} ").strip().lower()
        if choice == 'e':
            print(f"{LOADING} Exiting {name_tool}..")
            time.sleep(0.5)
            sys.exit()

        options = {
            '01': "Discord-Token-Information",      '11': "Discord-Token-House-Changer",  '21': "Discord-Token-Mass-Dm",       '?': "Changelog-Version",
            '02': "Discord-Token-Login",            '12': "Discord-Token-Theme-Changer",  '22': "Discord-Token-Delete-Dm",     '!': "Tool-Information",
            '03': "Discord-Token-Onliner",          '13': "Discord-Token-Joiner",         '23': "Discord-Id-To-Token",         'f': "Tokens-File",
            '04': "Discord-Token-Generator",        '14': "Discord-Token-Leaver",         '24': "Discord-Snowflake-Decoder",
            '05': "Discord-Token-Disabler",         '15': "Discord-Server-Information",   '25': "Discord-Bot-Id-To-Invite",
            '06': "Discord-Token-Bio-Changer",      '16': "Discord-Token-Nuker",          '26': "Discord-Webhook-Information",
            '07': "Discord-Token-Alias-Changer",    '17': "Discord-Token-Delete-Friends", '27': "Discord-Webhook-Generator",
            '08': "Discord-Token-CStatus-Changer",  '18': "Discord-Token-Block-Friends",  '28': "Discord-Webhook-Spammer",
            '09': "Discord-Token-Pfp-Changer",      '19': "Discord-Token-Unblock-Users",  '29': "Discord-Webhook-Deleter",
            '10': "Discord-Token-Language-Changer", '20': "Discord-Token-Spammer",        '30': "Discord-Nitro-Generator",
        }

        special_choices = ['?', '!', 'f']

        if choice in special_choices:
            StartProgram(options[choice] + '.py')
        elif choice.zfill(2) in options:
            StartProgram(options[choice.zfill(2)] + '.py')
        else:
            ErrorChoice()

    except Exception as e:
        Error(e)