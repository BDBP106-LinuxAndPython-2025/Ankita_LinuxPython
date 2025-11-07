celsius = [0, 20, 37, 100]
fahrenheit = list(map(lambda c: (c * 9/5) + 32, celsius))
'''The lambda is an anonymous function that takes an argument "c", it returns values automatically without the "return" keyword'''
print(fahrenheit)
#map: applies the lambda function to each element of celsius