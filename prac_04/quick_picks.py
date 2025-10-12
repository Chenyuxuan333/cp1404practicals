def main():
    num_quick_picks = int(input("How many quick picks? "))
    for _ in range(num_quick_picks):
        quick_pick = generate_quick_pick()
        # Format each number to be at least 2 characters wide
        print()

main()