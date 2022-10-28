#!/usr/local/bin/python

if __name__ == "__main__":
	with open("genomic_dna2.txt", "r") as f:
		genome = f.readline().rstrip()
	
	exons = []	
	with open("exons.txt", "r") as f:
		for line in f:
			position = line.rstrip().split(",")
			start = int(position[0])
			end = int(position[1])
			exon = genome[start-1:end]
			exons.append(exon)
	
	with open("exons_concat.txt", "w") as f:
		exons_concat = "".join(exons)
		f.write(exons_concat + "\n")

