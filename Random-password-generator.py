import random
import string

def generate_password(length=9):
    if length < 9:
        raise ValueError("Password must be at least 9 characters long.")
    
    special_characters = "!@#$%^&*"
    lower_case = string.ascii_lowercase
    upper_case = string.ascii_uppercase
    digits = string.digits

    # Ensure at least one of each required character type is included
    password = [
        random.choice(upper_case),
        random.choice(lower_case),
        random.choice(digits),
        random.choice(special_characters)
    ]
    
    # Fill the rest of the password length with a random mix of all character types
    all_characters = upper_case + lower_case + digits + special_characters
    password += random.choices(all_characters, k=length - len(password))
    
    # Shuffle the password to randomize the order
    random.shuffle(password)
    
    return ''.join(password)

# Example usage: Print one password at a time
if __name__ == "__main__":
    print("Generating passwords one at a time. Press Ctrl+C to stop.\n")
    try:
        while True:
            password = generate_password(length=9)
            print(f"Generated Password: {password}")
            input("Press Enter to generate the next password...")
    except KeyboardInterrupt:
        print("\nPassword generation stopped.")
