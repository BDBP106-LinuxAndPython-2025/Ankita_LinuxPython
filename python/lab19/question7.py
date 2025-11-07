def analyse_dna(sequence):
    def gc_content(seq):
        g = seq.count('G')
        c = seq.count('C')
        return (g + c) / len(seq) * 100

    gc = gc_content(sequence.upper())

    if gc > 50:
        print("GC rich sequence")
    else:
        print("AT rich sequence")
analyse_dna("AAAATTTTGCCAAA")
