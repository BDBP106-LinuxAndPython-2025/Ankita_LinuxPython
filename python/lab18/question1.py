#part:1
a= [i for i in range(1, 51)]
print("(i) list a:")
print(a)
print(" ")

#part 2
print("part2: Slicing - positive step:")
print(" (a) =", a[1:5])
print(" (b) =", a[3:20:2])
print(" (c) =", a[::2])
print(" (d) =", a[::])
print(" (e) =", a[10::2])
print(" (f) =", a[1:1:1])
print(" (g) =", a[:0:])
print(" (h) =", a[-7::1])
print(" (i) =", a[-6:])
print(" (j) =", a[-10:-4])
print(" ")

#part3
print("part3: Slicing - negative step:") #default value for negative slicing is -1, -2 and so on
print(" (a) =", a[::-1])
print(" (b) =", a[::-3])
print(" (c) =", a[:1:-2])
print(" (d) =", a[-1:-1:-1])
print(" (e) =", a[-5:-1])
print(" (f) =", a[:0:-1])
print(" (g) =", a[:-1:-1])
print(" (h) =", a[0:-5:-1])
print(" (i) =", a[-1:5:-1])
print(" (j) =", a[2:2:-1])
print(" (k) =", a[2:1:-1])
print(" (l) =", a[0:5])
print(" ")

#part4
print("part4 Modifications using slicing:")
#parta
list_even_numbers = a[1::2]
print("a :", list_even_numbers)

#partb
combined_list = a[:10] + a[34:50:2] #starts from index number 34 and slices before 50
print("b :", combined_list)