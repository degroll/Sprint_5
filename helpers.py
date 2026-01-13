import random
import string

def generate_email():
    domain = "@gmail.com"
    name_length = random.randint(5, 10)
    name = "".join(random.choice(string.ascii_lowercase) for _ in range(name_length))
    return name + domain

def generate_bad_email():
    name_length = random.randint(5, 10)
    name = "".join(random.choice(string.ascii_lowercase) for _ in range(name_length))
    return name