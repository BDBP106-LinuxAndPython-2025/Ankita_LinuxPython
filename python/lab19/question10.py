import time
import math

# this is a decorator to measure execution time
def measure_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print("Time taken:", end - start, "seconds")
        return result
    return wrapper

@measure_time
def population_growth(initial, rate, time_):
    def exponential_growth():
        return initial * math.exp(rate * time_)

    for _ in range(1_000_000):  # loop 1 million times
        exponential_growth()

    population = exponential_growth()
    print("Population after time:", round(population))

# call the function
population_growth(1000, 0.05, 10)
