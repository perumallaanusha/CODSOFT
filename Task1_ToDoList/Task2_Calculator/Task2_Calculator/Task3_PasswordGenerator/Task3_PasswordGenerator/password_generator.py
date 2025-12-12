# Task 3 - Password Generator

import random
import string

print("---- Password Generator ----")

# Ask user for password length
length = int(input("Enter the desired password length: "))

# Characters to choose from: letters (uppercase + lowercase), digits, punctuation
characters = string.ascii_letters + string.digits + string.punctuation

# Generate password
password = "".join(random.choice(characters) for i in range(length))

print("\nYour generated password is:")
print(password)
