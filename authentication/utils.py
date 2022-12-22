import random, string

def get_random_string(n):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(n))
    return str(result_str)
