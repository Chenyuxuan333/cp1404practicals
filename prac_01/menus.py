name = input("Enter name: ")
MENU = """(H)ello
(G)oodbye
(Q)uit"""
print(MENU)
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "H":
        print(f"HELLO {name}")
    elif choice == "G":
        print(f"GOOD BYE {name}")
    else:
        print("invalid choice")
    print (MENU)
    choice = input(">>> ").upper()

print("Finished")