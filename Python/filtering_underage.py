citizen = [
    ('Hannah', 78), ('Julia', 45), 
     ('Alice', 32), ('Michael', 90), 
     ('Natalie', 19), ('Oliver', 60), 
     ('Charlie', 7), ('Linda', 42), 
     ('Kevin', 97), ('Emily', 73), 
     ('David', 29), ('Grace', 67), 
     ('Frank', 12), ('Rachel', 85), 
     ('Isaac', 56), ('Samuel', 53), 
     ('Tina', 66), ('Bob', 84), 
     ('Patricia', 39), ('Quincy', 21)
]

filter_by_age = lambda age: age[1] >= 18

not_underage = list(filter(filter_by_age, citizen))

for i in not_underage:
    print(f'{i[0]} is {i[1]} years old')