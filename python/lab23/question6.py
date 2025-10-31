
import re
text = input("Enter your text: ")

# finds all email addresses
emails = re.findall(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}', text)

# masks each email and replace it in the text
for email in emails:
    name, domain = email.split('@')
    if len(name) > 2:
        masked_name = name[0] + '*'*(len(name)-2) + name[-1]
    else:
        masked_name = '*' * len(name)
    masked_email = masked_name + '@' + domain
    text = text.replace(email, masked_email)

print("Masked text:")
print(text)
