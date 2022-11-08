#!/usr/local/bin/python

def kmer_count(seq, k_size, minfreq):
    count = {}
    for i in range(0, len(seq)-k_size):
        kmer = seq[i:i+k_size]
        if kmer in count:
            count[kmer] += 1
        else:
            count[kmer] = 1
    return [key for key in count if count[key] > minfreq]


if __name__ == "__main__":
    dna = input("Please input the sequence:\n")
    k = int(input("Please input the kmer length:\n"))
    threshold = int(input("Please input the threshold:\n"))
    result = kmer_count(dna, k, threshold)
    print(result)
