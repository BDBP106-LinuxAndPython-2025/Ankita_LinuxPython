'''Write a decorator log_function_call that prints Running DNA analysis.... before
and Analysis complete! after any function. Apply it to the above function that returns
the GC % of a DNA sequence.'''
# decorator definition
def log_function_call(func):
    def wrapper(*args, **kwargs):
        print("Running DNA analysis....")
        result = func(*args, **kwargs)
        print("Analysis complete!")
        return result
    return wrapper

@log_function_call
def gc_content(dna):
    g = dna.upper().count('G')
    c = dna.upper().count('C')
    gc_percent = (g + c) / len(dna) * 100
    return gc_percent

# call the function and input the values
gc = gc_content("ATGCGCGTA")
print("GC% =", round(gc, 2))
