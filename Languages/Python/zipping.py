username = {'singularixty','robloxmaster555'}
password = {'singuilarixty123','robloxprogamer'}

credential = dict(zip(username, password))
print(credential)

for user, password in credential.items():
    print(f'{user}:{password}')