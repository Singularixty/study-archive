def addition(*nums):
    total = 0
    for num in nums:
        total += num
    return total

print(addition(1,4,5,6,1,2,5,1))

def name(*names):
    for name in names:
        print('Hello!', name)

print(name('Singularixty','JaneDoe', 'JohnDoe'))


def kw_args(**address):
    for address_type, address_info in address.items():
        print(address_type, address_info)

print(kw_args(address_l1='Fake Street 123', address_l2 = 'Bangkok, Thailand', zipcode = '12345'))