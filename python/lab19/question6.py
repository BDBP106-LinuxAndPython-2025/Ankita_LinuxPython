def cell_metabolism(glucose, oxygen):
    def energy_output(g, o):
        return (g * 6 <= o) * (g * 38)  # ensures enough oxygen
    return energy_output(glucose, oxygen)

# Example:
print(cell_metabolism(2, 12))  # 2 glucose + 12 oxygen → 76 ATP
