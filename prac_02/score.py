import random

def main():

    user_input = input("Enter your score: ")
    # Get user's score and print result
    if user_input.replace(".", "", 1).isdigit():
        user_score = float(user_input)
        user_result = determine_result(user_score)
        print(f"Your result: {user_result}")
    else:
        print("Invalid input. Please enter a valid number.")

    #  Generate random score and print result
    random_score = random.uniform(0, 100)
    random_result = determine_result(random_score)
    print(f"\nRandom score: {random_score:.1f}")
    print(f"Random result: {random_result}")

def determine_result(score):
    """Determine the result category for a given score"""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

main()