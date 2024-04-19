import matplotlib.pyplot as mpl

slices = [5, 3, 10, 6]
light_blue = '#ADD8E6'  
light_red = '#FFB6C1' 
light_green = '#90EE90'  
light_brown = '#D2B48C'
light_purple = '#98FB98' 
activities = ['Gaming','Eating','Coding','Sleeping']
colors = [light_blue, light_red, light_green, light_brown]

mpl.pie(slices, labels=activities, explode=(0.01, 0.01, 0.01, 0.01), autopct='%1.2f%%')
mpl.title("Example of 24 Hours of a person")
mpl.show()
