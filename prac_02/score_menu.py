MENU = """(G)et a valid score)
(P)rint result
(S)how stars
(Q)uit"""

def main():
    """Main function with menu system (without while True)."""
    print("Welcome to the Score Program!")

    # Get initial valid score before menu loop
    current_score = get_valid_score()

    # Main menu loop
    is_running = True

    while is_running:
        print(menu)
        choice = input("Choose an option: ").upper()

        if choice == "G":
            current_score = get_valid_score()
        elif choice == "P":
            print_result(current_score)
        elif choice == "S":
            show_stars(current_score)
        elif choice == "Q":
            print("Thank you for using the program. Goodbye!")
            is_running = False  # 退出循环
        else:
            print("Invalid option. Please choose G, P, S, or Q.")

    main()