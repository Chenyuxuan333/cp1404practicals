MIN_LENGTH = 9

def main():
    password = get_password()
    print_asterisks(password)

def get_password():
    password = input("Enter your password: ")
    while len(password) < MIN_LENGTH:
        print("Invalid password!!")
        password = input("Enter your password: ")
    return password

def print_asterisks(password):
    print("*" * len(password))

main()