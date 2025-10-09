#Create a string by joining the numbers in the above list a using the comma
a= [i for i in range (1,51)]
s = ','.join([str(x) for x in a])
print(s)

#Create a string by joining the numbers in the above list a using the period.
t = '.'.join([str(x) for x in a])
print(t)

#Create a string by joining the numbers in the above list a using the ‘—’
u = '---'.join([str(x) for x in a])
print(u)

#Create a new string by first creating a list of squares of the elements in a,
#then listing them alongside the elements of a line by line.
v = '\n'.join([f"{x} {x**2}" for x in a]) #\n separates the line and arranges it side by side
print(v)

#(a) Convert each element in the list to upper case using list comprehension
people = [ "ankita bose", "anik das", "shalmoli dutta", "vandana sah", "peter parker", "mary jane", "rohit sharma", "lisa ray", "dinesh kotha", "harris brother"]
upper_ppl = [name.upper() for name in people]
print(upper_ppl)

#b) Swap the first name and surname of each element
swapped_people = [' '.join(name.split()[::-1]) for name in people]
print(swapped_people)

#c) Join the first name and surname as 'First.Last'
cap_people = [f"{name.split()[0].capitalize()}.{name.split()[1].capitalize()}" for name in people]
print(cap_people)

#(iii) Find the longest word in this sentence using list comprehension: ”She sells sea shells that she collects from the sea floor”
sentence= "she sells sea shells that she collects from the sea floor"
words = sentence.split()                         # split the sentence into words
longestWord = [word for word in words if len(word) == max(len(w) for w in words)][0] #[0] looks for the first word incase there are multiple max length words
print("Longest word:", longestWord)

#Create a list of the words that are repeated in the above sentence
sentence = "She sells sea shells that she collects from the sea floor"
words1 = sentence.lower().split()
repeated_words = [word for word in words1 if words1.count(word) > 1 and words.index(word) == words1.index(word)]
print("Repeated words:", repeated_words)
