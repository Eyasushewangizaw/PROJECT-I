import random
import string
import argparse


class PasswordGenerator:
    def __init__(self, length=12, use_lowercase=True, use_uppercase=True, use_digits=True, use_special_chars=True):
        self.length = length
        self.use_lowercase = use_lowercase
        self.use_uppercase = use_uppercase
        self.use_digits = use_digits
        self.use_special_chars = use_special_chars

    def generate_password(self):
        characters = ''

        if self.use_lowercase:
            characters += string.ascii_lowercase
        if self.use_uppercase:
            characters += string.ascii_uppercase
        if self.use_digits:
            characters += string.digits
        if self.use_special_chars:
            characters += string.punctuation

        if not any([self.use_lowercase, self.use_uppercase, self.use_digits, self.use_special_chars]):
            print("Error: At least one character type should be selected.")
            return None

        password = ''.join(random.choice(characters) for _ in range(self.length))
        return password

    def validate_password(self, password):
        # Check if the given password meets the specified criteria
        required_characters = ''
        if self.use_lowercase:
            required_characters += string.ascii_lowercase
        if self.use_uppercase:
            required_characters += string.ascii_uppercase
        if self.use_digits:
            required_characters += string.digits
        if self.use_special_chars:
            required_characters += string.punctuation

        return all(char in required_characters for char in password)


def main():
    parser = argparse.ArgumentParser(description="Password Generator App")
    parser.add_argument("-l", "--length", type=int, default=12, help="Length of the password")
    parser.add_argument("--no-lowercase", action="store_false", dest="use_lowercase", help="Exclude lowercase letters")
    parser.add_argument("--no-uppercase", action="store_false", dest="use_uppercase", help="Exclude uppercase letters")
    parser.add_argument("--no-digits", action="store_false", dest="use_digits", help="Exclude digits")
    parser.add_argument("--no-special-chars", action="store_false", dest="use_special_chars",
                        help="Exclude special characters")

    args = parser.parse_args()

    password_generator = PasswordGenerator(
        length=args.length,
        use_lowercase=args.use_lowercase,
        use_uppercase=args.use_uppercase,
        use_digits=args.use_digits,
        use_special_chars=args.use_special_chars
    )

    generated_password = password_generator.generate_password()
    print("Generated Password:", generated_password)

    user_input_password = input("Enter a password to validate: ")
    is_valid = password_generator.validate_password(user_input_password)

    if is_valid:
        print("The password is valid.")
    else:
        print("The password does not meet the specified criteria.")


if __name__ == "__main__":
    main()
