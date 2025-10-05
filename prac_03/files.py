# # 1. Write a name to a file
user_name = input("Please enter your name: ")
# Open (or create) the file name.txt in write mode
name_file = open("name.txt", "w")
# Write the user's input name to the file
name_file.write(user_name)
# Close the file
name_file.close()

# # 2. Read the name from the file and print it
read_name_file = open("name.txt", "r")
# Read the content from the file
name = read_name_file.read()
# Print the content in the required format
print(f"Hi {name}!")
# Close the file
read_name_file.close()

# # 3. Read the first two numbers and calculate their sum
with open("numbers.txt", "r") as numbers_file:
    # Read the first line and convert to an integer
    first_number = int(numbers_file.readline())
    # Read the second line and convert to an integer
    second_number = int(numbers_file.readline())
# Calculate the sum of the two numbers and print the result
sum_two_numbers = first_number + second_number
print(sum_two_numbers)

# # 4. Calculate the sum of all numbers in the file
total = 0
with open("numbers.txt", "r") as all_numbers_file:
    # Read the file line by line
    for line in all_numbers_file:
        # Convert each line to an integer and add to the total
        total += int(line)
# Print the sum of all numbers
print(total)