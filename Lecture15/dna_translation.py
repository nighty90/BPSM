#!/usr/local/bin/python

if __name__ == "__main__":

    gencode = {
        "ATA": "I", "ATC": "I", "ATT": "I", "ATG": "M",
        "ACA": "T", "ACC": "T", "ACG": "T", "ACT": "T",
        "AAC": "N", "AAT": "N", "AAA": "K", "AAG": "K",
        "AGC": "S", "AGT": "S", "AGA": "R", "AGG": "R",
        "CTA": "L", "CTC": "L", "CTG": "L", "CTT": "L",
        "CCA": "P", "CCC": "P", "CCG": "P", "CCT": "P",
        "CAC": "H", "CAT": "H", "CAA": "Q", "CAG": "Q",
        "CGA": "R", "CGC": "R", "CGG": "R", "CGT": "R",
        "GTA": "V", "GTC": "V", "GTG": "V", "GTT": "V",
        "GCA": "A", "GCC": "A", "GCG": "A", "GCT": "A",
        "GAC": "D", "GAT": "D", "GAA": "E", "GAG": "E",
        "GGA": "G", "GGC": "G", "GGG": "G", "GGT": "G",
        "TCA": "S", "TCC": "S", "TCG": "S", "TCT": "S",
        "TTC": "F", "TTT": "F", "TTA": "L", "TTG": "L",
        "TAC": "Y", "TAT": "Y", "TAA": "_", "TAG": "_",
        "TGC": "C", "TGT": "C", "TGA": "_", "TGG": "W"
    }
    
    dna = input("Please input the DNA sequence:\n").upper()
    for strand in ("top", "bottom"):
        for frame in (1, 2, 3):
            if strand == "top":
                dna_processed = dna[frame-1:]
            else:
                trans_table = str.maketrans({"A": "T", "T": "A", "C": "G", "G": "C"})
                dna_processed = dna.translate(trans_table)
                dna_processed = dna_processed[::-1]
                dna_processed = dna_processed[frame-1:]
            dna_len = len(dna_processed)
            codon_list = [dna_processed[i:i+3] for i in range(0, dna_len-2, 3)]
            aa = [gencode.get(codon, "?") for codon in codon_list]
            trans = "".join(aa)
            print(f"{strand} {frame}: {' '.join(codon_list)}")
            print(f"protein: {trans}")


