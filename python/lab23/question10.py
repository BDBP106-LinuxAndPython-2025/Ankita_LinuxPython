'''  Take a DNA sequence and determine whether or not it contains any ambiguous bases –
i.e. any bases that are not A, T, G or C. If there is a non ambiguous base, print the non
ambiguous bases. dna = ”ATCGCGYAATTCAC”
'''
import re
dna = "ATCGCGYAATTCAC"

# to find all characters that are NOT A, T, G, or C
ambiguous = re.findall(r'[^ATGC]', dna)

if ambiguous:
    print("The DNA sequence contains ambiguous bases:")
    print(ambiguous)
else:
    print("The DNA sequence contains no ambiguous bases).")
