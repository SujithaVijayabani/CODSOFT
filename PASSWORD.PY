import random
import string
def generate_password(length, use_uppercase, use_lowercase, use_digits, use_special_chars, special_chars):
    characters = ""
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_special_chars:
        characters += special_chars
    if not characters:
        return "No character set selected for password generation."
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
while True:
    print("Password Generator Options:")
    length = int(input("Enter password length: "))
    use_uppercase = input("Include uppercase letters? (yes/no): ").lower() == "yes"
    use_lowercase = input("Include lowercase letters? (yes/no): ").lower() == "yes"
    use_digits = input("Include digits? (yes/no): ").lower() == "yes"
    use_special_chars = input("Include special characters? (yes/no): ").lower() == "yes"

    if use_special_chars:
        special_chars = input("Enter the special characters to include: ")
    else:
        special_chars = ''

    password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_special_chars, special_chars)

    print("Generated Password:", password)

    another_password = input("Generate another password? (yes/no): ").lower()
    if another_password != "yes":
        break
