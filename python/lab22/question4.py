def track_calls(func):
    count = 0  # keeps track of number of calls
    def wrapper(*args, **kwargs):
        nonlocal count
        count += 1  # increase the count each time
        message = f"{func.__name__} called {count} times\n"

        # opening a file in append mode and log the message
        with open("call_log.txt", "a") as f:
            f.write(message)

        return func(*args, **kwargs)  # execute the actual function

    return wrapper

@track_calls
def greet(name):
    return f"Hello, {name}!"


# ---- Test ----
print(greet("Ankita"))
print(greet("Shalmoli"))
print(greet("Vandana"))
