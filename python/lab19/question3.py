import math
#import math module to use sin(), cos() etc..
angles = (0, 30, 45, 60, 90) #tuple
result = list(map(lambda x: (math.sin(math.radians(x)), math.cos(math.radians(x))), angles))
print(result)
#sin and cos expects radian values, hence the angle is converted to radians
