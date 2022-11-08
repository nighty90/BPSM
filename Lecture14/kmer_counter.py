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
    dna = "ATGCATCATG"
    assert kmer_count(dna, 2, 2) == ["AT"]
    print("clear!")
