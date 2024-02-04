import matplotlib.pyplot as mpl

years = [1980, 1990, 2000, 2010]
Electric = [2000, 2100, 2500, 1400]
Industrial = [1000, 3000, 2000, 3000]
Residential = [3000, 2400, 2410, 1200]
Transportation = [1400, 2300, 2400, 2500]

light_blue = '#ADD8E6'  
light_red = '#FFB6C1' 
light_green = '#90EE90'  
light_brown = '#D2B48C'
light_purple = '#98FB98' 

mpl.plot([], [], color=light_blue, label='Electric')
mpl.plot([], [], color=light_red, label='Industrial')
mpl.plot([], [], color=light_green, label='Residential')
mpl.plot([], [], color=light_brown, label='Transportation')

mpl.stackplot(years, Electric, Industrial, Residential, Transportation, colors=[light_blue, light_red, light_green, light_brown, light_purple])
mpl.title("Carbon Dioxide Emissions from Energy Consumption")
mpl.xlabel('Years')
mpl.ylabel('CO2 (mmt)')

mpl.xlim(min(years), max(years))
mpl.legend()
mpl.show()
