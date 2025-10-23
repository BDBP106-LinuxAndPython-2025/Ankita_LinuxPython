import time

def measure_the_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()              # record start time
        result = func(*args, **kwargs)   # call the function
        end = time.time()                # record end time
        print(f"{func.__name__} took {end - start} seconds")  # end - start = total time
        return result
    return wrapper

@measure_the_time
def slow_add(a, b):
    time.sleep(2)   # simulate slow work (wait for 2 seconds)
    return a + b

print("Result:", slow_add(5, 10))
