import random
import string

def generate_password(length):
    if length < 4:
        print("Password length should be at least 4 for better security.")
        return None
    
    # Define character pools
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# User input
try:
    length = int(input("Enter the desired password length: "))
    password = generate_password(length)
    if password:
        print(f"Generated Password: {password}")
except ValueError:
    print("Please enter a valid integer for the password length.")