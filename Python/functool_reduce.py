from functools import reduce

fruit_list = {8,7,6,5,4,3,2,1}

def CombineCharacter(first, second):
    return first * second

result = reduce(CombineCharacter, fruit_list)
print(result)