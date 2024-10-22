seq1= "GCAACGCACAACGAAAACCCTTAGGGACTGGATTATTTCGTGATCGTTGTAGTTATTGGAAGTACGGGCATCAACCCAGT"
seq2= "TTATCTGACAAAGAAAGCCGTCAACGGCTGGATAATTTCGCGATCGTGCTGGTTACTGGCGGTACGAGTGTTCCTTTGGGT"

transitions = 0
transversions = 0
for base1, base2 in zip(seq1, seq2):

    if base1 != base2:
        if (base1 in 'AG' and base2 in 'AG') or (base1 in 'CT' and base2 in 'CT'):
            transitions += 1
        else:
            transversions += 1

    ratio = transitions / transversions

print(ratio)
