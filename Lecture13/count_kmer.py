#!/usr/local/bin/python

from random import shuffle

if __name__ == "__main__":
	# prepare the DNA sequence
	seq = "ATCG"*100
	seq = list(seq)
	shuffle(seq)
	seq = "".join(seq)
	
	# count kmer
	k = 3
	offset = 3
	n = 4
	count = {}
	for i in range(0, len(seq)-k, offset):
		kmer = seq[i:i+k]
		if kmer in count:
			count[kmer] += 1
		else:
			count[kmer] = 1
	output = []
	for key, value in count.items():
		if value > n:
			output.append(f"{key}:{value}")
	print(f"DNA sequence: {seq}")
	print(f"{k=}, {offset=}, {n=}")
	print(count)
	print(output)
