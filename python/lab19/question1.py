# for conversion of Celsius to Fahrenheit
def c_to_f(c):
    return (c * 9/5) + 32

#input values
celsius = [0, 20, 37, 100]

# map() to convert each Celsius value to Fahrenheit
fahrenheit = list(map(c_to_f, celsius)) #map function used the feature/properties of c_to_f to process the elements in celcius

print("Celsius values:", celsius)
print("Fahrenheit values:", fahrenheit)
