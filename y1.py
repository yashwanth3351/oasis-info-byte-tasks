import random
import string

# Define character sets
lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
digits = string.digits
symbols = string.punctuation

# Get user input
length = int(input("Enter desired password length: "))
use_uppercase = input("Include uppercase letters (y/n)? ").lower() == 'y'
use_digits = input("Include digits (y/n)? ").lower() == 'y'
use_symbols = input("Include symbols (y/n)? ").lower() == 'y'

# Build character set based on user preferences
char_set = ""
if use_uppercase:
    char_set += uppercase
if use_digits:
    char_set += digits
if use_symbols:
    char_set += symbols
if not char_set:
    char_set = lowercase  # Default to lowercase if no other set chosen

# Generate random password
password = ''.join(random.choices(char_set, k=length))

# Display the password
print("Your generated password:", password)

print("Remember to keep your password secure and don't share it with anyone.")
