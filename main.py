# importing the libraries
import random


def main():
    password_length = 32  # the length of the password
    password = ""

    while len(password) < password_length:
        password += random.choice(
            "abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()-_=+'[]{}|;:,.<>/?`~ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    print(password)


# calling the main function
if __name__ == "__main__":
    main()
