'''Write a program to concatenate a list of strings to make a sentence using reduce function.'''
from functools import reduce

words = ["Ankita", "is", "studying", "at", "ibab"]
sentence = reduce(lambda x, y: x + " " + y, words)

print(sentence)
