io.write("Enter non-negative number: ")
local Number = tonumber(io.read())

if Number and Number >= 0 then
    local total = 1
    local original_number = Number
    repeat
        total = total * Number
        Number = Number - 1
    until Number == 0
    print("Factorial of", original_number," is ",total)
end