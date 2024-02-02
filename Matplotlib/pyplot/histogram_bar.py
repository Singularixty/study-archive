import matplotlib.pyplot as mpl

ages = [12, 45, 124, 24, 55, 125, 5, 22, 61, 52, 52, 54, 16, 56, 47, 23, 45]

bins = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130]

mpl.hist(ages, bins, histtype='bar', rwidth=0.8, label = "Bar_1")
mpl.legend()
mpl.show()