import random
import string

def generate_password(length=12, use_uppercase=True, use_lowercase=True, use_digits=True, use_special_chars=False):
    """
    Generate a random password based on user-defined criteria.

    :param length: Length of the password (default: 12)
    :param use_uppercase: Include uppercase letters (default: True)
    :param use_lowercase: Include lowercase letters (default: True)
    :param use_digits: Include digits (default: True)
    :param use_special_chars: Include special characters (default: False)
    :return: Generated password as a string
    """
    character_set = ""
    
    if use_uppercase:
        character_set += string.ascii_uppercase
    if use_lowercase:
        character_set += string.ascii_lowercase
    if use_digits:
        character_set += string.digits
    if use_special_chars:
        character_set += string.punctuation

    if not character_set:
        raise ValueError("At least one character set must be selected.")

    password = "".join(random.choices(character_set, k=length))
    return password

def get_user_input():
    """
    Get user input for password generation settings.

    :return: Dictionary containing user preferences
    """
    try:
        length = int(input("Enter the length of the password: "))
        if length < 1:
            raise ValueError("Password length must be at least 1.")
        
        use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
        use_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
        use_digits = input("Include digits? (y/n): ").lower() == 'y'
        use_special_chars = input("Include special characters? (y/n): ").lower() == 'y'

        return {
            'length': length,
            'use_uppercase': use_uppercase,
            'use_lowercase': use_lowercase,
            'use_digits': use_digits,
            'use_special_chars': use_special_chars
        }
    except ValueError as e:
        print(f"Invalid input: {e}")
        return None

def main():
    print("Welcome to the Password Generator!")
    user_preferences = get_user_input()

    if user_preferences:
        try:
            password = generate_password(**user_preferences)
            print(f"Your generated password is: {password}")
        except ValueError as e:
            print(e)

if __name__ == "__main__":
    main()