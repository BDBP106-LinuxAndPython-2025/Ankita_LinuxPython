import re

# Input string
text = input("Enter a string: ")

# Simple pattern (no \w or \b)
# allows multiple dots after the main domain (e.g., .ac.in)
pattern = r'[A-Za-z0-9._-]+@[A-Za-z0-9._-]+\.[A-Za-z.]+'
if re.search(pattern, text):
    print(f"{text}  is an email address")
else:
    print(f"{text} is not an email address")
