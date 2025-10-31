'''
Check for the presence of an AvaII recognition site, which can have two different se-
quences: GGACC and GGTCC. Use regular expressions. dna = ”ATCGCGAATTCAC” pattern = GGACC and GGTCC
'''
import re

dna = "ATCGCGAATTCAC"
pattern = r"GGACC|GGTCC"   # either GGACC or GGTCC

# Checks if the pattern exists in the DNA sequence
if re.search(pattern, dna):
    print("AvaII recognition site found in the DNA sequence.")
else:
    print("AvaII recognition site not found.")
