local print = {}

print.print = setmetatable({}, {
	__index = function()
		error("function!")
	end,
	__call = function(_, ...)
		print(...)
	end,
})

return print