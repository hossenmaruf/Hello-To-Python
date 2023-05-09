import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters

chars = list(chars)
key = chars.copy()
random.shuffle(key)

#Encryption
user_text = input("Enter your secret text: ")
encrypt_text = ""

for letter in user_text:
    index = chars.index(letter)
    encrypt_text += key[index]

print(f"your original text : {user_text}")
print(f"encryption text    : {encrypt_text}")

#Decryption

encrypt_text = input("Enter your secret text: ")
user_text = ""

for letter in encrypt_text:
    index = key.index(letter)
    user_text += chars[index]

print(f"encryption text    : {encrypt_text}")
print(f"your original text : {user_text}")
