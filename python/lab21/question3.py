# defining a custom error class
class AgeTooYoungError(Exception):
    pass

# defining a function that checks age
def checkAge(age):
    try:
        if age < 18:
            # to raise the custom error
            raise AgeTooYoungError("Age must be more than 18")
        else:
            print("Age is valid.")
    except AgeTooYoungError as e:
        # to handle the exception and print the message
        print("Error:", e)

checkAge(3)
