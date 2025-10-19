"""
Program to process Wimbledon champions data.

Estimated time: 30 minutes
Actual time: 25 minutes
"""
def main():
    """Main function to execute the program."""
    filename = "wimbledon.csv"
    data = read_data(filename)
    champions_count = count_champions(data)
    countries = get_countries(data)

    print("Wimbledon Champions:")
    for champion, count in champions_count.items():
        print(f"{champion} {count}")

    print(f"\nThese {len(countries)} countries have won Wimbledon:")
    print(", ".join(countries))

def read_data(filename):
    """Read the data from the CSV file and return a list of lists."""
    data = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        for line in in_file:
            line = line.strip()
            if line:
                data.append(line.split(","))
    return data

def count_champions(data):
    """Count the number of times each champion has won and return a dictionary."""
    champions_count = {}
    for row in data:
        champion = row[2]
        if champion in champions_count:
            champions_count[champion] += 1
        else:
            champions_count[champion] = 1
    return champions_count

def get_countries(data):
    """Get the countries of the champions and return a sorted set."""
    countries = set()
    for row in data:
        country = row[1]
        countries.add(country)
    return sorted(countries)

main()