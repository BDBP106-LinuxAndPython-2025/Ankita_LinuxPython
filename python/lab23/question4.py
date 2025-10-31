#check if the third field of the csv contains an emails address or not

import re
line=input("Enter the line here")
fields=line.split(',') #split the csv file into the list of fields

if len(fields) > 3: #checks if the length of the fields is greater than 3
    third_field = fields[2].strip()  # get 3rd field and remove spaces

    pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$' #pattern to search email

    if re.fullmatch(pattern, third_field): #checks if th third field has the patter
        print("The 3rd field has an email address.")
    else:
        print("The 3rd field does not have an email address.")
else:
    print("The CSV line has less than 4 fields.")

