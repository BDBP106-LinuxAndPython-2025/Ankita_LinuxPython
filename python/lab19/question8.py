def protein_energy(temp):
    def calculate_free_energy(enthalpy, entropy):
        return enthalpy - temp * entropy

    # take user input for ΔH and ΔS
    H = float(input("Enter ΔH (enthalpy): "))
    S = float(input("Enter ΔS (entropy): "))

    G = calculate_free_energy(H, S)

    if G < 0:
        return "stable"
    else:
        return "unstable"

print(protein_energy(310))
