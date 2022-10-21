#!/usr/local/bin/python3

seq = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
print(f"DNA sequence: {seq}")
print(f"A+T content: {(seq.count('A') + seq.count('T')) / len(seq)}")
