''' Write a regular expression to split the DNA string wherever we see a base that isn’t A,
T, G or C. if the dna = ”ACTNGCATRGCTACGTYACGATSCGAWTCG”, the output
should be [’ACT’, ’GCAT’, ’GCTACGT’, ’ACGAT’, ’CGA’, ’TCG’]
'''
import re

dna = "ACTNGCATRGCTACGTYACGATSCGAWTCG"

# to split wherever the base is NOT A, T, G, or C
parts = re.split(r'[^ATGC]+', dna)

# Remove any empty strings that may appear in the list
parts = [p for p in parts if p] #list comprehension here which means : Make a new list with every p in parts
# , but only include it if p is not empty: since if the dna strand starts with "N" which is not ATG or C, it creates an empty string
print(parts)
