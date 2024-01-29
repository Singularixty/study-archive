path = input('Path: ')

with open(path, 'r') as file:
    g = file.read()
    print(g)
    file.close()