"""
Emails
Estimated time: 30 minutes
Actual time: [Fill in actual time] minutes
"""

def extract_name(email):
    """Extract a name from an email address."""
    # Split the email at '@' and take the part before
    prefix = email.split('@')[0]
    # Split the prefix at '.' and join the parts, then capitalize each word
    name_parts = prefix.split('.')
    name = ' '.join(name_parts).title()
    return name

email_to_name = {}

while True:
    email = input("Email: ")
    if not email:
        break
    # Extract name from email
    name = extract_name(email)
    # Ask user to confirm name
    confirm = input(f"Is your name {name}? (Y/n) ").lower()
    if confirm != '' and confirm != 'y':
        name = input("Name: ")
    # Store in dictionary
    email_to_name[email] = name

# Print out all emails and names
for email, name in email_to_name.items():
    print(f"{name} ({email})")