"""
CP1404/CP5632 - Practical
Program for temperature conversion
"""
from prac_02.convert import celsius_to_fahrenheit, fahrenheit_to_celsius

MENU =   """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius 
Q - Quit"""


def main():
    """Main function to handle the menu and user interactions."""
print(MENU)
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "C":
        celsius = float(input("Celsius: "))
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f"Result:{fahrenheit:.2f}")
    elif choice == "F":
        fahrenheit = float(input("Fahrenheit: "))
        celsius = fahrenheit_to_celsius(fahrenheit)
        print(f"Result:{celsius:.2f}")
    else:
        print("Invalid option")
    print(MENU)
    choice = input(">>> ").upper()
print("Thank you.")

main()