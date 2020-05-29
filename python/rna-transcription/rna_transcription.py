def to_rna(dna_strand):
    dna_to_rna = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'}
    rna_strand = ''
    for s in dna_strand:
        rna_strand += dna_to_rna.get(s, '')
    return rna_strand
