MIN_LENGTH = 9

pass_word = input("Enter your password: ")
while len(pass_word) < MIN_LENGTH:
    print("Invalid password!!")
    pass_word = input("Enter your password: ")
else:
    print("*" * len(pass_word))