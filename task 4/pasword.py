import random
import string


def generate_password(length=12):
    # Define character sets
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"

    # Ensure at least one character from each set
    password = [
        random.choice(uppercase),
        random.choice(lowercase),
        random.choice(digits),
        random.choice(special_chars)
    ]

    # Fill the rest of the password length
    all_chars = uppercase + lowercase + digits + special_chars
    for _ in range(length - 4):
        password.append(random.choice(all_chars))

    # Shuffle the password
    random.shuffle(password)

    # Join characters into string
    return ''.join(password)


# Generate and print a password
print("Generated Password:", generate_password(12))