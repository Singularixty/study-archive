import matplotlib.pyplot as mpl
import random

x_val = []
y_val = []

for x in range(1, 100):
    x_val.append(int(x))
    y_val.append(random.randint(1, 100))

mpl.scatter(x_val, y_val, label='Virus', color='g',s=20)

mpl.legend()
mpl.show()