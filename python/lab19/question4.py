# Generate Fibonacci series and filter odd numbers

n = int(input("Enter number of terms: "))

# to generate Fibonacci series
fib = [0, 1]
for i in range(2, n):
    fib.append(fib[-1] + fib[-2]) #last and second last term

# filter out odd numbers
odd_fib = list(filter(lambda x: x % 2 != 0, fib))

print("Fibonacci series:", fib)
print("Odd numbers:", odd_fib)
