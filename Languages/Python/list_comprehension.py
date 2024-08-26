## [expression for item in iterable]
squares = [i**2 for i in range(10)]
print(squares)

## [expression condition for item in iterable]
even_square = [i**2 if i % 2 == 0 else 'not even' for i in range(20)]
print(even_square)