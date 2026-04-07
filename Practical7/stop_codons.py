input_file = "Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa"
output_file = "stop_genes.fa"
stop_codons = {"TAA", "TAG", "TGA"}

def parse_fasta(filename): # define a function called parse_fasta( ) to read the file 
    sequences = []
    header = None
    seq_parts = []
    with open(filename, "r") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            if line.startswith(">"):
                if header is not None:
                    sequences.append((header, "".join(seq_parts))) # insert gene and its DNA sequence 
                header = line[1:]
                seq_parts = []
            else:
                seq_parts.append(line.upper())
        if header is not None:
            sequences.append((header, "".join(seq_parts)))
    return sequences

def get_gene_name(header): # define a function to get gene name from header
    return header.split()[0].replace("_mRNA", "")

def find_in_frame_stop_codons(sequence): # define a function to find stop codons
    found = set()
    for i in range(len(sequence) - 2): #iterate DNA sequence
        if sequence[i:i+3] == "ATG":
            for j in range(i + 3, len(sequence) - 2, 3):
                codon = sequence[j:j+3]
                if codon in stop_codons:
                    found.add(codon)
                    break
    return sorted(found)

records = parse_fasta(input_file)

with open(output_file, "w") as out: # output a file
    for header, sequence in records:
        gene_name = get_gene_name(header)
        found_stops = find_in_frame_stop_codons(sequence)

        if found_stops:
            out.write(f">{gene_name} {'/'.join(found_stops)}\n")
            for i in range(0, len(sequence), 60):
                out.write(sequence[i:i+60] + "\n")