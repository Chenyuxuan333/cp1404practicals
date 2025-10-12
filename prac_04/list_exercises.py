# Part 1: Basic list operations
numbers = []
for i in range(5):
    num = float(input(f"Number: "))
    numbers.append(num)

first = numbers[0]
last = numbers[-1]
smallest = min(numbers)
largest = max(numbers)
total = sum(numbers)
average = total / len(numbers)

print(f"The first number is {first}")
print(f"The last number is {last}")
print(f"The smallest number is {smallest}")
print(f"The largest number is {largest}")
print(f"The average of the numbers is {average}")

# Part 2: Woefully inadequate security checker
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command']
user_input = input("Enter your username: ")
if user_input in usernames:
    print("Access granted")
else:
    print("Access denied")