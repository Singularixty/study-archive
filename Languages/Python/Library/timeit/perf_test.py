import timeit

def measure_import_time(import_statement, iterations=100000):
    # Measure the time taken to execute the import statement
    time_taken = timeit.timeit(import_statement, number=iterations)
    # Format the time taken to a more readable format
    formatted_time = f"Time taken for '{import_statement}': {time_taken:.4f} seconds for {iterations} iterations"
    return formatted_time

# Test the import times
time_from_math_import_sqrt = measure_import_time('from flask import Flask')
time_import_math = measure_import_time('import flask')

print(time_from_math_import_sqrt)
print(time_import_math)

