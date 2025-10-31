import re

# Regular expression for 000–255
pattern = r'^(25[0-5]|2[0-4][0-9]|1[0-9]{2}|0[0-9]{2})$'

# Test numbers
test= ["000", "099", "100", "199", "200", "249", "255",
"256", "300", "12", "556"]

for num in test:
    if re.fullmatch(pattern, num):
        print(f"{num} is Valid (in range 000–255)")
    else:
        print(f"{num} is Invalid")