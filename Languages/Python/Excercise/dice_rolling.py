import random

def RollDice(n):
    dices_result = []
    for _ in range(n):  
        roll = random.randint(1, 6)
        dices_result.append(roll)
    return dices_result

n = input("Number of dices to roll: ")

if not n.isdigit():
    print("Only numbers are accepted!")
else:
    result = RollDice(int(n))
    if len(result) == 1:
        print(f"Result: {result[0]}")
    else:
        for i, n in enumerate(result):
            print(f"Dice #{i+1}: {n}")