'''
Check for the presence of a BisI restriction site using regular expression character groups:
A character group is a pair of square brackets with a list of characters inside them. dna
= ”ATCGCGAATTCAC” pattern = GCNGC, where N represents any base, i.e. A, T,
G, C
'''

import re
dna = "ATCGCGAATTCAC"
pattern = r"GC[ATGC]GC"   # N can be A, T, G, or C

# it checks if the pattern exists in the DNA sequence
if re.search(pattern, dna):
    print("BisI recognition site found in the DNA sequence.")
else:
    print("BisI recognition site not found.")
