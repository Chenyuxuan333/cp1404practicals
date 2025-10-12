import random

# Constants
MIN_NUMBER = 1
MAX_NUMBER = 45
NUMBERS_PER_LINE = 6

def main():
    """Asks the user for the number of quick picks."""
    """Generates and prints each quick pick line, formatting numbers to align neatly with 2 characters per number."""
    num_quick_picks = int(input("How many quick picks? "))
    for _ in range(num_quick_picks):
        quick_pick = generate_quick_pick()
        # Format each number to be at least 2 characters wide
        print(" ".join(f"{num:2}" for num in quick_pick))

def generate_quick_pick():
    """Generates 6 unique random numbers between 1 and 45 (using a loop to check for duplicates).
Sorts the numbers in ascending order."""
    numbers = []
    while len(numbers) < NUMBERS_PER_LINE:
        num = random.randint(MIN_NUMBER, MAX_NUMBER)
        if num not in numbers:
            numbers.append(num)
    numbers.sort()
    return numbers

main()