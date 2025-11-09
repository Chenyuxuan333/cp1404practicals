from guitar import Guitar

def main():
    guitars = []
    # Read data from guitars.csv
    with open('guitars.csv', 'r') as file:
        for line in file:
            line = line.strip()  # Remove newline characters
            parts = line.split(',')
            name = parts[0]
            year = int(parts[1])
            cost = float(parts[2])
            guitars.append(Guitar(name, year, cost))

    # Display original list
    print("Original list:")
    for guitar in guitars:
        print(guitar)

    # Sort the list by year (oldest to newest)
    guitars.sort()

    # Display sorted list
    print("\nSorted by year (oldest to newest):")
    for guitar in guitars:
        print(guitar)

if __name__ == "__main__":
    main()