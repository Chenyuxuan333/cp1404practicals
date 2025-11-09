"""
CP1404/CP5632 Practical
File and class example - reads programming language data with pointer arithmetic support
"""

import csv
from collections import namedtuple

from programming_language import ProgrammingLanguage


def main():
    """Read file of programming language details (including pointer arithmetic), save as objects, display."""
    languages = []
    in_file = open('languages.csv', 'r')
    # Read and skip header
    in_file.readline()
    for line in in_file:
        parts = line.strip().split(',')
        # Convert string values to appropriate types
        reflection = parts[2] == "Yes"
        year = int(parts[3])
        pointer_arithmetic = parts[4] == "Yes"
        # Create ProgrammingLanguage object with new field
        language = ProgrammingLanguage(
            parts[0], parts[1], reflection, year, pointer_arithmetic
        )
        languages.append(language)
    in_file.close()

    # Display all languages
    for language in languages:
        print(language)

    # Demonstrate pointer arithmetic check
    print("\nLanguages with pointer arithmetic support:")
    for language in languages:
        if language.has_pointer_arithmetic():
            print(f"- {language.name}")


main()


def using_csv():
    """Language file reader version using the csv module with pointer arithmetic field."""
    in_file = open('languages.csv', 'r', newline='')
    in_file.readline()  # Skip header
    reader = csv.reader(in_file)
    for row in reader:
        print(row)
    in_file.close()


def using_namedtuple():
    """Language file reader version using a named tuple with pointer arithmetic."""
    in_file = open('languages.csv', 'r', newline='')
    file_field_names = in_file.readline().strip().split(',')
    print(file_field_names)
    Language = namedtuple('Language', 'name, typing, reflection, year, pointer_arithmetic')
    reader = csv.reader(in_file)

    for row in reader:
        language = Language._make(row)
        print(repr(language))
    in_file.close()


def using_csv_namedtuple():
    """Language file reader version using both csv module and named tuple with pointer arithmetic."""
    Language = namedtuple('Language', 'name, typing, reflection, year, pointer_arithmetic')
    in_file = open("languages.csv", "r")
    in_file.readline()  # Skip header
    for language in map(Language._make, csv.reader(in_file)):
        print(f"{language.name} ({language.year}) - Pointer arithmetic: {language.pointer_arithmetic}")
        print(repr(language))

# Uncomment to test other readers
# using_csv()
# using_namedtuple()
# using_csv_namedtuple()