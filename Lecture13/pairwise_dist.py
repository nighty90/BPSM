#!/usr/local/bin/python

if __name__ == "__main__":
	dna_list = ['ATTGTACGG', 'AATGAACCG', 'AATGAACCC', 'AATGGGAAT']
	seq_len = len(dna_list[0])
	list_len = len(dna_list)
	for i in range(list_len-1):
		for j in range(i+1, list_len):
			seq1 = dna_list[i]
			seq2 = dna_list[j]
			count = 0
			for k in range(seq_len):
				if seq1[k] == seq2[k]:
					count += 1
			similarity = count / seq_len
			print("="*60)
			print(f"seq1: {seq1}")
			print(f"seq2: {seq2}")
			print(f"similarity: {similarity:.2}")
