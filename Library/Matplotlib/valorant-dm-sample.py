import matplotlib.pyplot as mpl

x = [1, 25, 300, 600]
y = [8, 10, 16, 25]


mpl.plot(x, y)
mpl.xlabel('Number of Matches Played')
mpl.ylabel('Valorant Kills (Per Match)')

mpl.title("Valorant Improvement Graph (Sample)")

mpl.show()