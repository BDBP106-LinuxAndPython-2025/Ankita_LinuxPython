#to find ecoRI restriction sites:pattern in the DNA sequence
import re

dna = "ATCGCGAATTCAC"
pattern = r"GAATTC"

# checks if pattern exists in DNA sequence
if re.search(pattern, dna):
    print("EcoRI site found in the DNA sequence.")
else:
    print("EcoRI site not found.")
