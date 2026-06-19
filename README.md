# Python Password Generator

A simple, beginner-friendly command-line tool for generating strong, random passwords. The generator lets you choose exactly which character types to include and guarantees that every selected type appears in the final password.

## Features

- Custom password length (minimum 4 characters)
- Choose which character categories to include:
  - Uppercase letters (A–Z)
  - Lowercase letters (a–z)
  - Numbers (0–9)
  - Special characters (`!@#$%^&*` etc.)
- Guarantees at least one character from each selected category
- Randomly shuffles characters so output is unpredictable
- Input validation with helpful error messages
- Generate as many passwords as you like in one session
- Built using only Python's standard library (`random` and `string` modules) — no external dependencies

## Requirements

- Python 3.6 or higher

No additional packages need to be installed.

## How to Run

1. Make sure Python 3 is installed on your system.
2. Download or copy `password_generator.py` to your computer.
3. Open a terminal (or command prompt) and navigate to the folder containing the file.
4. Run the script:

   ```bash
   python3 password_generator.py
   ```

   On Windows, you may need to use:

   ```bash
   python password_generator.py
   ```

## Example Session

```
==================================================
        PYTHON PASSWORD GENERATOR
==================================================
Enter desired password length (minimum 4): 12
Include uppercase letters? (y/n): y
Include lowercase letters? (y/n): y
Include numbers? (y/n): y
Include special characters? (y/n): y

Generated Password: aB3$kP9!mQ2z

Generate another password? (y/n): n

Thank you for using the Password Generator. Goodbye!
```

## How It Works

1. **Length input** – The program asks for a password length and validates that it's a whole number of at least 4.
2. **Category selection** – The program asks yes/no questions for each character category (uppercase, lowercase, numbers, special characters).
3. **Generation algorithm**:
   - One random character is picked from each *selected* category first, guaranteeing every chosen type is represented.
   - The remaining length is filled with random characters drawn from the combined pool of all selected categories.
   - All characters are shuffled together so the guaranteed characters don't always appear in predictable positions.
4. **Output** – The final password is displayed, and you're asked whether you'd like to generate another one.

## Input Validation

The program handles invalid input gracefully and will re-prompt instead of crashing if:

- The entered length isn't a whole number
- The entered length is below 4
- No character category is selected
- A yes/no question receives anything other than `y`/`yes` or `n`/`no`

## Project Structure

```
password_generator.py   # Main script with all logic and comments
README.md                # This documentation file
```

## Notes on Security

This tool uses Python's built-in `random` module, which is suitable for generating memorable, general-purpose passwords for everyday use. For highly sensitive use cases (e.g., cryptographic keys or system secrets), consider using Python's `secrets` module instead, which is designed for cryptographic randomness.

## License

This project is free to use, modify, and distribute for personal or educational purposes.
