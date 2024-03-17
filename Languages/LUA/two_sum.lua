function add(x, y)
    return x + y
end

io.write("Enter your x: ")
local x = tonumber(io.read())

io.write("Enter your y: ")
local y = tonumber(io.read())

if x and y then
    print("Sum:", add(x, y))
else
    print("Invalid input. Please enter valid numbers.")
end
