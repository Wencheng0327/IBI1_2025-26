from itertools import combinations
from BLOSUM62 import BLOSUM62


def read_fasta(filename):
    header = ""
    seq_parts = []

    with open(filename, "r") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            if line.startswith(">"):
                header = line[1:]
            else:
                seq_parts.append(line.upper())

    sequence = "".join(seq_parts)
    return header, sequence


def align_and_score(seq1, seq2):
    if len(seq1) != len(seq2):
        raise ValueError("Sequences must have the same length for non-gapped global alignment.")
    score = 0
    identical = 0
    marker = []
    for aa1, aa2 in zip(seq1, seq2):
        if aa1 not in BLOSUM62 or aa2 not in BLOSUM62[aa1]:
            raise ValueError(f"Invalid amino acid found: {aa1} or {aa2}")

        score += BLOSUM62[aa1][aa2]

        if aa1 == aa2:
            identical += 1
            marker.append("|")
        else:
            marker.append(" ")

    identity_percent = (identical / len(seq1)) * 100
    return score, identity_percent, "".join(marker)


def print_alignment(name1, seq1, name2, seq2, marker, width=60):
    print(f"{name1} vs {name2}")
    print("-" * 60)

    for i in range(0, len(seq1), width):
        print(seq1[i:i + width])
        print(marker[i:i + width])
        print(seq2[i:i + width])
        print()

    print("-" * 60)


def compare_files(file1, file2):
    name1, seq1 = read_fasta(file1)
    name2, seq2 = read_fasta(file2)

    score, identity_percent, marker = align_and_score(seq1, seq2)

    print("=" * 70)
    print(f"Comparison: {name1} vs {name2}")
    print(f"Length: {len(seq1)} amino acids")
    print(f"Alignment score (BLOSUM62): {score}")
    print(f"Percentage identity: {identity_percent:.2f}%")
    print()

    print_alignment(name1, seq1, name2, seq2, marker)

    return {
        "seq1": name1,
        "seq2": name2,
        "length": len(seq1),
        "score": score,
        "identity": identity_percent
    }


files = ["human.fasta", "mouse.fasta", "random.fasta"]
results = []

for file_a, file_b in combinations(files, 2):
    result = compare_files(file_a, file_b)
    results.append(result)


print("\nSUMMARY")
print("=" * 70)

for result in results:
    print(
        f"{result['seq1']} vs {result['seq2']}: "
        f"score = {result['score']}, "
        f"identity = {result['identity']:.2f}%"
    )