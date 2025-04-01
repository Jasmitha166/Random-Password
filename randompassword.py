import random
import string

def generate_password(length=12, use_digits=True, use_special=True):
    characters = string.ascii_letters  # Includes both uppercase and lowercase letters
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    length = int(input("Enter the password length: "))
    use_digits = input("Include digits? (y/n): ").strip().lower() == 'y'
    use_special = input("Include special characters? (y/n): ").strip().lower() == 'y'
    
    password = generate_password(length, use_digits, use_special)
    print(f"Generated Password: {password}")
