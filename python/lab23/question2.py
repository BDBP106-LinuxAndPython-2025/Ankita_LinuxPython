import re
pattern = r'^(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9][0-9]|[0-9])$'
test_numbers = ["0", "7", "09", "99", "100", "199", "200", "249",
"255", "256", "300", "-5", "3.14"]

for num in test_numbers:
    if re.fullmatch(pattern, num):
        print(f"{num} Valid (in range 0–255)")
    else:
        print(f"{num} is Invalid")
