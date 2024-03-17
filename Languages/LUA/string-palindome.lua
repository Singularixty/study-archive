io.write("Your String: ")
local inputString = io.read()
function preprocessString(str)
    return str:gsub("[^%w]", ""):lower()
end

local processedString = preprocessString(inputString)

if processedString == string.reverse(processedString) then
    print("The entered string is a palindrome.")
else
    print("The entered string is not a palindrome.")
end
