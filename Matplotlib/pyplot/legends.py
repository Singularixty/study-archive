import matplotlib.pyplot as mpl

x = [1, 2, 3, 4]
x1 = [1, 2, 3, 4]
y = [2, 1, 6, 20]
y1 = [4, 1, 4, 10]

mpl.plot(x, y, label = "First line")
mpl.plot(x1, y1, label = 'Second Line')
mpl.legend()
mpl.show()