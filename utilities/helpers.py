import random
import string

# Generate random string
def generate_random_string(length=6):
    return ''.join(random.choices(string.ascii_letters, k=length))

# Generate random number
def generate_random_number(length=4):
    return ''.join(random.choices(string.digits, k=length))