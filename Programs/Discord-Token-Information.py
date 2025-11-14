# Copyright (c) 2025 v4lkyr0/v4lkyr_
# See LICENSE file for details

from Plugins.Utils import *
from Plugins.Config import *

try:
    import requests
    from datetime import datetime, timezone
except Exception as e:
    MissingModule(e)

Title("Discord Token Information")
Connection()

try:
    token = ChoiceToken()
    
    print(f"{LOADING} Retrieving Information..", reset)

    api      = requests.get('https://discord.com/api/v8/users/@me', headers={'Authorization': token}).json()
    response = requests.get('https://discord.com/api/v8/users/@me', headers={'Authorization': token, 'Content-Type': 'application/json'})

    if response.status_code == 200:
        status = "Valid"
    else:
        status = "Invalid"

    username          = api.get('username')
    display_name      = api.get('global_name')
    user_id           = api.get('id')
    country           = api.get('locale')
    email             = api.get('email')
    email_verified    = api.get('verified')
    phone             = api.get('phone')
    
    try:
        linked_users_raw = api.get('linked_users')
        if linked_users_raw and len(linked_users_raw) > 0:
            linked_users = ', '.join([str(user) for user in linked_users_raw])
        else:
            linked_users = "None"
    except:
        linked_users = "None"
    
    avatar_decoration = api.get('avatar_decoration')
    avatar            = api.get('avatar')   
    accent_color      = api.get('accent_color')
    banner            = api.get('banner')  
    banner_color      = api.get('banner_color')
    flags             = api.get('flags')
    public_flags      = api.get('public_flags')
    nsfw_allowed      = api.get('nsfw_allowed')
    mfa_enabled       = api.get('mfa_enabled')
    
    try:
        mfa_type_raw = api.get('authenticator_types')
        if mfa_type_raw and len(mfa_type_raw) > 0:
            mfa_types = []
            for mfa in mfa_type_raw:
                if mfa == 1:
                    mfa_types.append('SMS')
                elif mfa == 2:
                    mfa_types.append('App')
                elif mfa == 3:
                    mfa_types.append('WebAuthn')
                else:
                    mfa_types.append(f'Other ({mfa})')
            mfa_type = ', '.join(mfa_types)
        else:
            mfa_type = "None"
    except:
        mfa_type = "None"
    
    bio = api.get('bio')

    try:
        created_at_raw = datetime.fromtimestamp(((int(user_id) >> 22) + 1420070400000) / 1000, timezone.utc)
        created_at = created_at_raw.strftime('%Y-%m-%d %H:%M:%S')
    except:
        created_at = "None"

    try:
        premium_type = api.get('premium_type')
        if premium_type == 0:
            nitro_type = "No Nitro"
        elif premium_type == 1:
            nitro_type = "Nitro Classic"
        elif premium_type == 2:
            nitro_type = "Nitro Boost"
        else:
            nitro_type = "No Nitro"
    except:
        nitro_type = "No Nitro"

    try:
        avatar_url = f"https://cdn.discordapp.com/avatars/{user_id}/{avatar}.gif" if requests.get(f"https://cdn.discordapp.com/avatars/{user_id}/{avatar}.gif").status_code == 200 else f"https://cdn.discordapp.com/avatars/{user_id}/{avatar}.png"
    except:
        avatar_url = "No Avatar"

    try:
        billing = requests.get('https://discord.com/api/v6/users/@me/billing/payment-sources', headers={'Authorization': token}).json()
        if billing:
            payment_methods = []

            for method in billing:
                if method['type'] == 1:
                    payment_methods.append('Credit Card')
                elif method['type'] == 2:
                    payment_methods.append('PayPal')
                else:
                    payment_methods.append('Other')
            payment_methods = ', '.join(payment_methods)
        else:
            payment_methods = 'No Payment Methods'
    except:
        payment_methods = 'No Payment Methods'

    try:
        gift_codes = requests.get('https://discord.com/api/v9/users/@me/outbound-promotions/codes', headers={'Authorization': token}).json()
        if gift_codes:
            codes = []
            for gift in gift_codes:
                gift_name = gift.get['promotion']['outbound_title']
                gift_code = gift.get['code']
                msg_gift = f"Gift: {gift_name}\nCode: {gift_code}"
                if len(gift) > 0:
                    gift = '\n\n'.join(gift) + len()
            else:
                gift = 'No Gift Codes'
        else:
            gift = 'No Gift Codes'
    except:
        gift = 'No Gift Codes'

    try:
        response = requests.get('https://discord.com/api/v9/users/@me/guilds?with_counts=true', headers={'Authorization': token})
        if response.status_code == 200:
            guilds = response.json()
            try:
                guild_count = len(guilds)
            except:
                guild_count = 'None'
            try:
                owner_guilds       = [guild for guild in guilds if guild.get('owner')]
                owner_guilds_count = len(owner_guilds)
                if owner_guilds:
                    owner_guilds_list = []
                    for guild in owner_guilds:
                        owner_guilds_list.append(f"{guild.get('name')} {red}({white}{guild.get('id')}{red})")
                    owner_guilds_names = '\n' + ', '.join(owner_guilds_list)
                else:
                    owner_guilds_names = ''
            except:
                owner_guilds_count = 'None'
                owner_guilds_names = ''
    except:
        guild_count        = 'None'
        owner_guilds_count = 'None'
        owner_guilds_names = ''
        owner_guilds_names = 'None'

    try:
        response = requests.get('https://discord.com/api/v8/users/@me/relationships', headers={'Authorization': token}).json()
        if response:
            friends_list = []
            for friend in response:
                try:
                    if friend.get('type') != 1:
                        continue
                    
                    user_data = friend.get('user', {})
                    username = user_data.get('username', 'Unknown')
                    user_id_friend = user_data.get('id', 'Unknown')
                    friends_names = f"{username} {red}({white}{user_id_friend}{red})"
                    
                    if len('\n'.join(friends_list)) + len(friends_names) >= 1024:
                        continue
                    
                    friends_list.append(friends_names)
                except:
                    continue

            if len(friends_list) > 0:
                friends_count = len(friends_list)
                friends = f"{friends_count}\n" + ', '.join(friends_list)
            else:
                friends = 'None'
        else:
            friends = 'None'
    except:
        friends = 'None'

    Scroll(f"""
 {INFO} Status            :{red} {status}
 {INFO} Token             :{red} {token}
 {INFO} Username          :{red} {username}
 {INFO} Display Name      :{red} {display_name}
 {INFO} User Id           :{red} {user_id}
 {INFO} Created At        :{red} {created_at}
 {INFO} Country           :{red} {country}
 {INFO} Email             :{red} {email}
 {INFO} Email Verified    :{red} {email_verified}
 {INFO} Phone             :{red} {phone}
 {INFO} Nitro             :{red} {nitro_type}
 {INFO} Linked Users      :{red} {linked_users}
 {INFO} Avatar Decoration :{red} {avatar_decoration}
 {INFO} Avatar            :{red} {avatar}
 {INFO} Avatar Url        :{red} {avatar_url}
 {INFO} Accent Color      :{red} {accent_color}
 {INFO} Banner            :{red} {banner}
 {INFO} Banner Color      :{red} {banner_color}
 {INFO} Flags             :{red} {flags}
 {INFO} Public Flags      :{red} {public_flags}
 {INFO} NSFW Allowed      :{red} {nsfw_allowed}
 {INFO} MFA Enabled       :{red} {mfa_enabled}
 {INFO} MFA Type          :{red} {mfa_type}
 {INFO} Billing           :{red} {payment_methods}
 {INFO} Gift Codes        :{red} {gift}
 {INFO} Guilds            :{red} {guild_count}
 {INFO} Owner Guilds      :{red} {owner_guilds_count}{owner_guilds_names}
 {INFO} Bio               :{red} {bio}
 {INFO} Friends           :{red} {friends}{reset}
""")
    Continue()
    Reset()

except Exception as e:
    Error(e)