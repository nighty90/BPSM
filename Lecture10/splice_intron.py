#! /usr/local/bin/python3

seq = "ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"

exon1 = seq[:63]
exon2 = seq[91-1:]

coding_seq = exon1 + exon2

print(f"exon 1: {exon1}")
print(f"exon 2: {exon2}")
print(f"coding sequence: {coding_seq}")

print(f"coding percentage: {len(coding_seq)/len(seq)*100}%")

intron = seq[63:91-1]

formated_seq = exon1 + intron.lower() + exon2
print(f"formated sequence: {formated_seq}")

print(f"check length: formated_seq-{len(formated_seq)}, original_seq-{len(seq)}")
