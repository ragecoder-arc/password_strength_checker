# Importing regular expressions module
import re  

# Function to evaluate the strength of the given password
def password_strength_checker(password):
    # Check if password is less than 8 characters
    if len(password) < 8:
        return "Weak : password must contain at least 8 characters."
    
    # Check if password has at least one digit
    if not any(char.isdigit() for char in password):
        return "Weak : password must contain at least one digit."
    
    # Check if password has at least one lowercase letter
    if not any(char.islower() for char in password):
        return "Weak : password must contain at least one lowercase letter."
    
    # Check if password has at least one uppercase letter
    if not any(char.isupper() for char in password):    
        return "Moderate : password must contain at least one uppercase letter."
    
    # Check if password has at least one special character from the specified set
    if not any(char in "!@#$%^&*()-_+=<>?{}[]|:;\"'`~" for char in password):
        return "Medium : password must contain at least one special character."
    
    # If all checks are passed, password is strong
    return "Strong : password is strong." 

# Function to repeatedly prompt the user for passwords to check their strength
def password_checker():
    while True:
        # Prompt user input
        password = input("Enter a password to check its strength (or 'exit' to quit): ")
        
        # Exit condition
        if password.lower() == 'exit':
            break
        
        # Check password strength using the defined function
        strength = password_strength_checker(password)
        
        # Display the result
        print(strength)

# Main entry point of the program
if __name__ == "__main__":
    password_checker()
