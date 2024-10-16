n = input("Number of Fibonacci numbers to generate: ")
total_fibonacci_sequence = None
last_num = None
if not n.isdigit():
    print("Only numbers are allowed!")
else:
    fibonacci_sequence = [0, 1]
    for i in range(1, int(n)):
        next_pos = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_pos)
    total_fibonacci_sequence = fibonacci_sequence[:int(n)]
    last_num = fibonacci_sequence[int(n)-1]

print(total_fibonacci_sequence)
print(f"Last Number: {last_num}")