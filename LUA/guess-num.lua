function GenerateRandomNumber()
    local randomNumber = math.random(1, 100)
    return randomNumber
end

function StartGame()
    local Number = randomNumber()
    local total_guesses = 0
    local guess = 0
    repeat
        io.write("Enter your guess: ")
        guess = tonumber(io.read())

        if not guess then
            print("Please enter a valid number.")
        else
            if guess < Number then
                print("Too low, Guess again!")
                total_guesses = total_guesses + 1
            elseif guess > Number then
                print("Too high, Guess again!")
                total_guesses = total_guesses + 1
            else
                print("Your answer is right, you took " + total_guesses + " guesses to get it right!")
            end
        end
    until guess == Number
end