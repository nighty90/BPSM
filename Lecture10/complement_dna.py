#! /usr/local/bin/python3

seq = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
trans = str.maketrans({"A":"T", "C":"G", "T":"A", "G":"C"})
print(f"{'DNA sequence: '.ljust(25)}{seq}")
print(f"{'complement sequence: '.ljust(25)}{seq.translate(trans)}")
