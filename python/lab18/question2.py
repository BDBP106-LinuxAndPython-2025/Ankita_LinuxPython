#To find the sum of elements in the list a from before
a= [i for i in range (1,51)]
sum_total=0
for i in a:
 sum_total = sum_total + i
print("The sum of the elements are:", sum_total)

#Define another list b (using list comprehension again!) containing prime numbers
#from 1 to 50.
b=[x for x in range(2, 51) if all (x % i != 0 for i in range(2,x))] #all is because if the value is true then only it will include the prime numbers in the list
print("The list of the prime numbers are", b )

#To create a list which will have all the common numbers between list a and b
c=[x for x in a if x in b]
print ("The list of the common numbers in both the lists are", c )