import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters

print(chars)

chars = list(chars)
key = chars.copy()

random.shuffle(key)

print(f"chars: {chars}")
print(f"key : {key}")
