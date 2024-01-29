import random

random_num = random.random()
print(random_num)

alpha = 2.0
beta = 5.0

random_beta = random.betavariate(alpha, beta)
print(random_beta)

my_list = [1, 2, 3, 4, 5]
weights = [0.9, 0.1, 0.1, 0.1, 0.1]

for i in range(0, 10):
    random_elements = random.choices(my_list, weights=weights, k=2)
    print(random_elements)

random_expo = random.expovariate(0.5)
print(random_expo)
