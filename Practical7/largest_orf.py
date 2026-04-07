#import re

seq = 'AAGAUACAUGCAAGUGGUGUGUCUGUUCUGAGAGGGCCUAAAAG'
# another solution
# pattern = r'(?=(AUG(?:...)*?(?:UAA|UAG|UGA)))'
# matches = re.findall(pattern, seq) # find all matching ORFs in the RNA sequence

# longest_orf = ""

# for orf in matches:
    # if len(orf) % 3 == 0: #ensure the sequence length is a mutiple of 3
        # if len(orf) > len(longest_orf):
            # longest_orf = orf

# print("Longest ORF:", longest_orf)
# print("Length:", len(longest_orf))


 
start_codon = "AUG"
stop_codons = {"UAA", "UAG", "UGA"}
longest_orf = ""

for i in range(len(seq) - 2): #iterate seq three by three
    if seq[i:i+3] == start_codon:
        for j in range(i + 3, len(seq) - 2, 3): #find the stop codons
            codon = seq[j:j+3]
            if codon in stop_codons:
                orf = seq[i:j+3]
                if len(orf) > len(longest_orf):
                    longest_orf = orf
                break

print("Longest ORF:", longest_orf)
print("Length:", len(longest_orf))