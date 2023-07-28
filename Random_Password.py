import random

def generate_random_password(length):
    password = ""
    for i in range(length):
        character = random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
        password += character
    return password

def main():
    password = generate_random_password(12)
    print("The random password is:", password)

if __name__ == "__main__":
    main()
