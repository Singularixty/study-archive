import matplotlib.pyplot as mpl

x = [1, 2, 3, 4]
y = [25, 31 ,21 ,28]
x_2 = [1, 2, 3, 4]
y_2 = [10, 30, 10, 50]
mpl.bar(x, y, label = "Bar_1")
mpl.bar(x_2, y_2, label = "Bar_2")
mpl.legend()
mpl.show()