import matplotlib.pyplot as mpl

ages = [12, 45, 124, 24, 55, 125, 5, 22, 61, 52, 52, 54, 16, 56, 47, 23, 45]

ids = [x for x in range(len(ages))]

mpl.bar(ids,ages, label = "Bar_1")
mpl.legend()
mpl.show()