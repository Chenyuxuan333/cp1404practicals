MIN_LENGTH = 9

def main():
    password = get_password()
    print("*" * len(password))

def get_password():
    password = input("Enter your password: ")
    while len(password) < MIN_LENGTH:
        print("Invalid password!!")
        password = input("Enter your password: ")
    return password
main()