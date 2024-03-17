function generateFibonacci(n)
    local fibonacciSequence = {0, 1}

    for i = 3, n do
        local nextTerm = fibonacciSequence[i - 1] + fibonacciSequence[i - 2]
        table.insert(fibonacciSequence, nextTerm)
    end

    return fibonacciSequence
end


io.write("Enter the number of Fibonacci terms: ")
local numTerms = tonumber(io.read())

if numTerms and numTerms > 0 then
    local fibonacciSequence = generateFibonacci(numTerms)
    print("Fibonacci sequence up to", numTerms, "terms:", table.concat(fibonacciSequence, ", "))
else
    print("Invalid input. Please enter a valid positive integer.")
end
