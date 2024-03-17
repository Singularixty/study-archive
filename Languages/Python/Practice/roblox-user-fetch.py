import requests
import os
from datetime import datetime

user_ID = input('Insert UserId: ')
current_date = datetime.now().strftime('%Y-%m-%d')

def RetrieveUserInfo(user_ID):
    # Fetch basic userinfo
    userinfo_api = f'https://users.roblox.com/v1/users/{user_ID}'
    userinfo_request = requests.get(userinfo_api)
    userinfo_response = userinfo_request.json()
    
    # Extract user details
    user_displayname = userinfo_response['displayName']
    user_realname = userinfo_response['name']
    user_id = userinfo_response['id']
    user_bio = userinfo_response['description']
    user_banstatus = userinfo_response['isBanned']
    user_verifybadge = userinfo_response['hasVerifiedBadge']
    user_acccreationdate = userinfo_response['created']
    
    # Fetch username history
    username_history_url = f'https://users.roblox.com/v1/users/{user_id}/username-history?limit=100&sortOrder=Asc'
    username_history_request = requests.get(username_history_url)
    username_history_response = username_history_request.json()
    user_usernamehistory = username_history_response['data']
    
    def usernamehistory_fetch():
        name_list_table = [str(i['name']) for i in user_usernamehistory]
        return ', '.join(name_list_table)
    
    with open (f'./rbx_bin/{user_realname}_{current_date}.txt','w' , encoding='utf-8') as file:
    # file.write user basic info
        file.write(f'{user_displayname} (@{user_realname}): https://www.roblox.com/users/{user_ID}/profile\n')
        file.write(f'∙ Creation Date: {datetime.strptime(user_acccreationdate, "%Y-%m-%dT%H:%M:%S.%fZ")}\n')
        file.write(f'∙ ID: {user_id}\n')
        file.write(f'∙ Bio: {user_bio}\n')
        file.write(f'∙ Verified Badge: {user_verifybadge}\n')
        file.write(f'∙ User Banned?: {user_banstatus}\n')
        file.write(f'∙ Previous Names: {usernamehistory_fetch()}\n')
        
        # Fetch and file.write user avatar info
        avatar_url = f'https://avatar.roblox.com/v1/users/{user_id}/avatar'
        avatar_url = requests.get(avatar_url)
        user_avatar = avatar_url.json()
        
        bodyscale = user_avatar['scales']
        avatar_type = user_avatar['playerAvatarType']
        bodyscale_height = bodyscale['height']
        bodyscale_width = bodyscale['width']
        bodyscale_head = bodyscale['head']
        bodyscale_depth = bodyscale['depth']
        bodyscale_proportion = bodyscale['proportion']
        
        player_emote = user_avatar['emotes']
        player_accessories = user_avatar['assets']
        
        # file.write avatar info
        file.write(f'∙ Character Type: {avatar_type}\n∙ BodyScale:\n')
        file.write(f'  ∙ Height: {bodyscale_height}\n  ∙ Width: {bodyscale_width}\n  ∙ Head: {bodyscale_head}\n')
        file.write(f'  ∙ Depth: {bodyscale_depth}\n  ∙ Proportion: {bodyscale_proportion}\n')
        
        # file.write accessories
        file.write(f'∙ Accessories:\n')
        for i in player_accessories:
            asset_name = i['name']
            asset_id = i['id']
            asset_type = i['assetType']['name']
            file.write(f'  ∙ {asset_name} ({asset_type}): https://www.roblox.com/catalog/{asset_id}\n')
        
        # file.write emotes
        file.write(f'∙ Emotes:\n')
        if player_emote:
            for i in player_emote:
                asset_name = i['assetName']
                asset_id = i['assetId']
                file.write(f'  ∙ {asset_name} : https://www.roblox.com/catalog/{asset_id}\n')
        else:
            file.write(' -\n')
        
        # Fetch and file.write friends
        friend_url = f'https://friends.roblox.com/v1/users/{user_ID}/friends?userSort=1'
        friend_req = requests.get(friend_url)
        friend_json = friend_req.json()
        
        file.write(f'∙ Friends:\n')
        for i in friend_json['data']:
            friend_id = i['id']
            friend_name = i['name']
            friend_display_name = i['displayName']
            file.write(f'  ∙ {friend_display_name} (@{friend_name}): https://www.roblox.com/users/{friend_id}/profile\n')
        
        # Fetch and file.write groups
        group_url = f'https://groups.roblox.com/v2/users/{user_ID}/groups/roles'
        group_req = requests.get(group_url)
        group_json = group_req.json()
        
        file.write(f'∙ Groups:\n')
        for i in group_json['data']:
            group_id = i['group']['id']
            group_name = i['group']['name']
            group_member_count = (int(i['group']['memberCount'])).__format__(',')
            user_role = i['role']['name']
            file.write(f'  ∙ {group_name}: https://www.roblox.com/groups/{group_id}\n')
            file.write(f' Role: {user_role} - {group_member_count} Member(s)\n')
        
        # Fetch and file.write collections
        collections_url = f'https://inventory.roblox.com/v1/users/{user_ID}/collections'
        collections_req = requests.get(collections_url)
        collections_data = collections_req.json()

        file.write(f'∙ Collections:\n')
        if not 'errors' in collections_data:
            for collection in collections_data['data']:
                collection_id = collection['id']
                collection_name = collection['name']
                collection_url = f'https://www.roblox.com/collections/{collection_id}'
                file.write(f'  ∙ {collection_name}: {collection_url}\n')
        else:
            file.write(f'  {collections_data["errors"][0]["message"]}')
        file.close()
        print(f"Data has been recorded -> @root/rbx_plr_fetch/{user_realname}_{current_date}.txt")

# Clear the terminal and call the function
os.system('cls' if os.name == 'nt' else 'clear')
RetrieveUserInfo(user_ID=user_ID)
input("Press Enter to exit...")
