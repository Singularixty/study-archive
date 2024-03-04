your_loved_food = []
while (food := input('What food do you like?: ').lower()) not in ['q', 'quit']:
    print(f'You like {food}')
    your_loved_food.append(food)
else:
    print('Awwww sad, Time to quit!')
    loved_food_str = ', '.join(your_loved_food)
    print('Your loved foods:', loved_food_str)
