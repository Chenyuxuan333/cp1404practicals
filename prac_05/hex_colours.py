# Define a dictionary mapping color names to their corresponding hex codes
COLORS = {
    "AliceBlue": "#f0f8ff",
    "AntiqueWhite": "#faebd7",
    "Aqua": "#00ffff",
    "Aquamarine": "#7fffd4",
    "Azure": "#f0ffff",
    "Beige": "#f5f5dc",
    "Bisque": "#ffe4c4",
    "Black": "#000000",
    "BlanchedAlmond": "#ffebcd",
    "Blue": "#0000ff"
}

# Prompt the user to enter a color name
color_name = input("Enter a color name (blank to stop): ")

# Loop until the user enters an empty string
while color_name != "":
    # Format the input to match the dictionary key case (e.g., "aliceblue" → "AliceBlue")
    formatted_color = color_name.title()

    # Check if the color exists in the dictionary and output the result
    if formatted_color in COLORS:
        print(f"The hex code for {formatted_color} is {COLORS[formatted_color]}")
    else:
        print("Invalid color name")

    # Get the next input from the user
    color_name = input("Enter a color name (blank to stop): ")