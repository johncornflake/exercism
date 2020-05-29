
codon_protein = {('AUG'): 'Methionine',
                 ('UUU', 'UUC'): 'Phenylalanine',
                 ('UUC'): 'Phenylalanine',
                 ('UUA','UUG'): 'Leucine',
                 ('UCU', 'UCC', 'UCA', 'UCG'): 'Serine',
                 ('UAU', 'UAC'): 'Tyrosine',
                 ('UGU', 'UGC'): 'Cysteine',
                 ('UGG'): 'Tryptophan',
                 ('UAA', 'UAG', 'UGA'): 'STOP'
                 }
def proteins(strand):
    codons = [strand[i:i+3] for i in range(0, len(strand), 3)]
    protein_list = []
    for c in codons:
        protein = [v for k, v in codon_protein.items() if c in k][0]
        if protein == 'STOP': break
        protein_list.append(protein)

    return protein_list
