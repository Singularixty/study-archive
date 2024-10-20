import random
import string

def generate_password(length=12, times=1):
    total_char = string.ascii_letters + string.ascii_lowercase + string.ascii_uppercase + string.octdigits + string.punctuation
    for i in range(1, times+1):
        password = ''.join(random.choice(total_char) for i in range(length))
        print(f"Password #{i}: {password}")

generate_password(20, 20)