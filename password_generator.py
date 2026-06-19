"""
Password Generator
-------------------
A command-line tool that generates strong, random passwords based on
user-selected character categories (uppercase, lowercase, numbers,
special characters).

Author: Generated with Claude
"""

import random
import string


def get_password_length():
    """
    Ask the user for the desired password length and validate the input.
    Keeps prompting until a valid integer >= 4 is entered.
    """
    while True:
        length_input = input("Enter desired password length (minimum 4): ").strip()

        # Make sure the input is a digit before converting to int
        if not length_input.isdigit():
            print("Invalid input. Please enter a whole number.\n")
            continue

        length = int(length_input)

        if length < 4:
            print("Password length must be at least 4 to support all character types.\n")
            continue

        return length


def get_yes_no(prompt):
    """
    Ask a yes/no question and validate the input.
    Returns True for 'y' / 'yes' and False for 'n' / 'no'.
    """
    while True:
        answer = input(prompt).strip().lower()
        if answer in ("y", "yes"):
            return True
        elif answer in ("n", "no"):
            return False
        else:
            print("Invalid input. Please answer with 'y' or 'n'.\n")


def get_character_categories():
    """
    Ask the user which character categories to include in the password.
    Returns a dictionary mapping category names to the actual character sets,
    only including categories the user selected.
    """
    categories = {}

    if get_yes_no("Include uppercase letters? (y/n): "):
        categories["uppercase"] = string.ascii_uppercase

    if get_yes_no("Include lowercase letters? (y/n): "):
        categories["lowercase"] = string.ascii_lowercase

    if get_yes_no("Include numbers? (y/n): "):
        categories["numbers"] = string.digits

    if get_yes_no("Include special characters? (y/n): "):
        categories["special"] = string.punctuation

    return categories


def generate_password(length, categories):
    """
    Generate a random password of the given length using the provided
    character categories.

    Guarantees that at least one character from each selected category
    appears in the final password, then fills the remaining length with
    random characters from the combined pool, and finally shuffles the
    result so the guaranteed characters aren't always in the same position.
    """
    if not categories:
        raise ValueError("At least one character category must be selected.")

    if length < len(categories):
        raise ValueError(
            f"Password length must be at least {len(categories)} "
            f"to include one character from each selected category."
        )

    # Combine all selected character sets into one pool to choose from
    all_characters = "".join(categories.values())

    # Step 1: Guarantee at least one character from each selected category
    password_chars = [random.choice(char_set) for char_set in categories.values()]

    # Step 2: Fill the rest of the password length with random characters
    # from the combined pool of all selected categories
    remaining_length = length - len(password_chars)
    password_chars += [random.choice(all_characters) for _ in range(remaining_length)]

    # Step 3: Shuffle so the guaranteed characters aren't predictably placed
    random.shuffle(password_chars)

    # Join the list of characters into a final password string
    return "".join(password_chars)


def main():
    """
    Main program loop: gathers user preferences, generates a password,
    displays it, and asks whether to generate another one.
    """
    print("=" * 50)
    print("        PYTHON PASSWORD GENERATOR")
    print("=" * 50)

    while True:
        length = get_password_length()
        categories = get_character_categories()

        # Make sure the user picked at least one category
        if not categories:
            print("\nYou must select at least one character category. Try again.\n")
            continue

        try:
            password = generate_password(length, categories)
            print(f"\nGenerated Password: {password}\n")
        except ValueError as error:
            print(f"\nError: {error}\n")

        # Ask if the user wants another password
        if not get_yes_no("Generate another password? (y/n): "):
            print("\nThank you for using the Password Generator. Goodbye!")
            break

        print()  # blank line for readability between rounds


# Standard Python entry point check
if __name__ == "__main__":
    main()
