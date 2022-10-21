#! /usr/local/bin/python3

seq = "ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT"

ind = seq.find("GAATTC")
fragment1 = seq[0:ind+1]
fragment2 = seq[ind+1:]
print(f"DNA sequence: {seq}")
print(f"fragment 1: {fragment1}")
print(f"length: {len(fragment1)}")
print(f"fragment 2: {fragment2}")
print(f"lengths: {len(fragment2)}")
