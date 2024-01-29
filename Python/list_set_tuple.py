my_list = []
my_list.append('Monday')
my_list.insert(1, 'hlelo')
my_list.append('hello2')
optional_list = ['zzzzzz','21rjusjauif']
my_list.extend(optional_list)
my_list.extend(['Multipleval_1','Multipleval_2'])
print(my_list)
my_set = {1,2}
my_set.add('hello')
my_set.update([5,4,3,2,6])
print(my_set)
my_dict = {}
my_dict['username'] = 'Singularixty'
my_dict['password'] = 'singulaixty1234'
my_dict['email'] = 'singularixty@gmail.com'
for k, v in my_dict.items():
    print(f'{k} = {v}')