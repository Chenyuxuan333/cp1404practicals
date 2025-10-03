"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    while True:
        denominator = int(input("Enter the denominator: "))
        if denominator == 0:
            print("The denominator cannot be zero")
        else:
            break
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")

#Q1: the input is not a number or a float
#Q2: When the denominator is 0