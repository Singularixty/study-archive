import math

# Find the highest and lowest value
array_of_number = {4,1,4,5,1}
lowest_num = min(array_of_number)
highest_num = max(array_of_number)
print(f"Lowest number is {lowest_num}")
print(f"Highest number is {highest_num}")

# Find an absolute of a number
x = -124
ab_x = abs(x)
print(f"Absolute of x is {ab_x}")

# Find a power of y
base = 20
power = 2
result = pow(base, power)
print(f"Result: {base} power of {power} is {result}")

# Rounding x up, down to nearest integer
x = 123.412
rounded = round(x)
rounded_up = math.ceil(x)
rounded_down = math.floor(x)
print("Rounded up x:", rounded_up)
print("Rounded down x:", rounded_down)
print("Rounded x based on mathematics:", rounded)
print(f"Current type of x: {type(x)}")

# Distance Calculation
pos_1 = [1, 2]
pos_2 = [2, 9]
distance = math.dist(pos_1, pos_2)
print(f"Distance between 2 positions are: {distance:.2f}")