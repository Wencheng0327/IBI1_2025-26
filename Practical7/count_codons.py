import matplotlib.pyplot as plt

input_file = "Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa"# Input FASTA file containing yeast cDNA sequences
valid_stops = {"TAA", "TAG", "TGA"}# Three valid stop codons

# Three valid stop codons
def parse_fasta(filename):# convert the file
    records = []
    header = None
    seq_parts = []

    with open(filename, "r") as file:# Open the FASTA file for reading
        for line in file:
            line = line.strip()
            if not line:
                continue
            if line.startswith(">"):# A new FASTA header starts with ">"
                if header is not None:
                    records.append((header, "".join(seq_parts)))# A new FASTA header starts with ">"
                header = line[1:]
                seq_parts = []
            else:
                seq_parts.append(line.upper())# Collect sequence lines and convert them to uppercase
        if header is not None:
            records.append((header, "".join(seq_parts)))

    return records

# Collect sequence lines and convert them to uppercase
def longest_orf_for_stop(sequence, stop_codon):
    longest_orf = ""

    for i in range(len(sequence) - 2):
        if sequence[i:i+3] == "ATG":# Search for a start codon
            for j in range(i + 3, len(sequence) - 2, 3):# Move forward in-frame, one codon at a time
                codon = sequence[j:j+3]
                if codon == stop_codon:# Move forward in-frame, one codon at a time
                    orf = sequence[i:j+3]
                    if len(orf) > len(longest_orf):
                        longest_orf = orf
                    break
                elif codon in valid_stops:# Stop if another in-frame stop codon appears first
                    break

    return longest_orf

# Ask the user to enter one stop codon
user_stop = input("Enter a stop codon (TAA, TAG, or TGA): ").strip().upper()
# Exit if the input is not valid
if user_stop not in valid_stops:
    print("Invalid stop codon.")
    raise SystemExit

records = parse_fasta(input_file)

codon_counts = {}

for header, sequence in records:# Process each gene sequence in the FASTA file
    best_orf = longest_orf_for_stop(sequence, user_stop)

    if best_orf:
        upstream_region = best_orf[3:-3]# Remove the start codon and the stop codon

        for i in range(0, len(upstream_region) - 2, 3):# Count all in-frame codons upstream of the stop codon
            codon = upstream_region[i:i+3]
            codon_counts[codon] = codon_counts.get(codon, 0) + 1

if not codon_counts:
    print(f"No genes found containing an in-frame {user_stop} stop codon.")
    raise SystemExit

print(f"Codon counts upstream of {user_stop}:")
for codon, count in sorted(codon_counts.items()):
    print(f"{codon}: {count}")

labels = list(codon_counts.keys())
sizes = list(codon_counts.values())

plt.figure(figsize=(10, 10))
plt.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=90)
plt.title(f"Distribution of in-frame codons upstream of {user_stop}")
plt.tight_layout()

output_file = f"codon_usage_{user_stop}.png"
plt.axis("equal")
plt.savefig(output_file, dpi=300)

print(f"Pie chart saved as {output_file}")