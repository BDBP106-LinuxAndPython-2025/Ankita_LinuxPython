#To extract all email addresses from a given piece of text

import re

text = input("Enter your text: ")

# it will find all email addresses using regex
emails = re.findall(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}', text)

# remove the duplicate ones
unique_emails = set(emails)

# prints all unique email addresses
print("Unique email addresses found:")
for email in unique_emails:
    print(email)
