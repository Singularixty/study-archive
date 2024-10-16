import random

randomInt = random.randint(1, 100)
guesses = 0
computer = randomInt
print(f"Number: {randomInt}")

guess = input("Guess number (1-100): ")
while True:
    if not guess.isdigit():
        print(f"Only numbers are accepted!")
    else:
        guess = int(guess)
        guesses += 1
        if guess == computer:
            print(f"You won the game, took {guesses} guesses!")
            break
        elif guess > computer:
            print(f"Your guessed number is too high!")
        elif guess < computer:
            print(f"Your guessed number is too low!")

    guess = input("Guess number (1-100): ")
