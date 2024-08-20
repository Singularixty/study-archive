my_info = {
    'Name' : "Penny",
    'Age' : 30,
    'City' : 'Texas'
}

print(my_info['Name'])

my_info['Age'] = 20
my_info['Career'] = "Software Engineer"

print(my_info)

del my_info['City']

print(my_info)

print(my_info.keys())
print(my_info.values())
print(my_info.items())