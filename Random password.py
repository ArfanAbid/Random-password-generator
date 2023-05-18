import random
import string

def generate_password(length):
    """
    Generate a random password of specified length
    """
    # Define the character sets to use in the password
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    numbers = string.digits
    symbols='!@#$%^&*()'
    
    # Combine the character sets into a single set of possible characters
    possible_chars = lowercase + uppercase + numbers+symbols
    # Generate a random password by selecting characters from the possible set
    password = ""
    for i in range(length):
        password =password + random.choice(possible_chars)
    
    return password


length=int(input("Enter the size of password :"))
password = generate_password(length)
print("The password generated is:" ,password)
