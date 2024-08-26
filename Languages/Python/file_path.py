import os

abs_path = os.path.abspath('test.txt')
print(abs_path)

is_file = os.path.isfile(abs_path)
print(is_file)

exists_path = os.path.exists(abs_path)
print(exists_path)