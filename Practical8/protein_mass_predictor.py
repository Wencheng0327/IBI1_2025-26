def predict_protein_mass(sequence):
    residue_masses = {
        "G": 57.02,
        "A": 71.04,
        "S": 87.03,
        "P": 97.05,
        "V": 99.07,
        "T": 101.05,
        "C": 103.01,
        "I": 113.08,
        "L": 113.08,
        "N": 114.04,
        "D": 115.03,
        "Q": 128.06,
        "K": 128.09,
        "E": 129.04,
        "M": 131.04,
        "H": 137.06,
        "F": 147.07,
        "R": 156.10,
        "Y": 163.06,
        "W": 186.08
    }# initialize the residue masses

    total_mass = 0

    for amino_acid in sequence.upper():# iterate the supplied amino acid sequence
        if amino_acid not in residue_masses:
            return f"Error: amino acid '{amino_acid}' has no recorded mass."
        total_mass += residue_masses[amino_acid]

    return total_mass

# Example function call
protein_sequence = "QGWACV"
mass = predict_protein_mass(protein_sequence)
print(f"Protein sequence: {protein_sequence}")
print(f"Total mass: {mass}")