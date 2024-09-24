import random
import string

def generate_random_string(length):
  
    characters = string.ascii_letters + string.digits
 
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string


length = 10 
random_str = generate_random_string(length)
print(f"Random String of length {length}: {random_str}")
