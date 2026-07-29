import random
import string

def generate_password(length=12):
    if length < 4:
        raise ValueError("Password length should be at least 4.")

    lower = random.choice(string.ascii_lowercase)
    upper = random.choice(string.ascii_uppercase)
    digit = random.choice(string.digits)
    symbol = random.choice("!@#$%^&*()_+-=[]{}|;:,.<>?")

    remaining = [
        random.choice(
            string.ascii_letters + string.digits + "!@#$%^&*()_+-=[]{}|;:,.<>?"
        )
        for _ in range(length - 4)
    ]

    password = [lower, upper, digit, symbol] + remaining
    random.shuffle(password)

    return "".join(password)

if __name__ == "__main__":
    print("=== Random Password Generator ===")
    try:
        length = int(input("Enter password length: "))
        print("\nGenerated Password:")
        print(generate_password(length))
    except ValueError as e:
        print("Error:", e)