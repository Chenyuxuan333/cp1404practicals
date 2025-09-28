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
        print(MENU)
        choice = input("Choose an option: ").upper()

        if choice == "G":
            current_score = get_valid_score()
        elif choice == "P":
            print_result(current_score)
        elif choice == "S":
            show_stars(current_score)
        elif choice == "Q":
            print("Thank you for using the program. Goodbye!")
            is_running = False
        else:
            print("Invalid option. Please choose G, P, S, or Q.")

def is_valid_number(input_str):
    """Check if input is a valid number (integer or float)."""
    parts = input_str.split('.')
    if len(parts) > 2:
        return False
    for part in parts:
        if not part.isdigit():
            return False
    return True

def get_valid_score():
    """Get a valid score (0-100 inclusive) using input validation."""
    valid = False
    score = 0.0
    while not valid:
        user_input = input("Enter score (0-100): ")
        if is_valid_number(user_input):
            score = float(user_input)
            if 0 <= score <= 100:
                valid = True
            else:
                print("Score must be between 0 and 100.")
        else:
            print("Invalid input. Please enter a number.")
    return score

def calculate_result(score):
    """Determine the result category for a given score."""
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

def print_result(score):
    """Print the result category for the given score."""
    result = calculate_result(score)
    print(f"Result: {result}")

def show_stars(score):
    """Print as many stars as the rounded score value."""
    stars = "*" * round(score)
    print(stars)

main()