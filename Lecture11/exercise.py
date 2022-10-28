#!/usr/local/bin/python
import re

# preprocess the DNA sequences
with open("./plain_genomic_seq.txt") as f:
	plain = f.read()

plain_seq = plain.replace("\n", "").upper()
plain_seq = re.sub(r"[^ATCG]", "", plain_seq)


with open("./AJ223353.fa") as f:
	fa = f.readlines()
    
fa_seq = "".join(fa[1:])
fa_seq = fa_seq.replace("\n", "").upper()

# split the genomic DNA

