#!/usr/local/bin/python

if __name__ == "__main__":
    # get cds of AJ223353
    with open("AJ223353.fa", "r") as f:
        lines = f.readlines()
    
    lines = [line.rstrip() for line in lines[1:]]
    dna = "".join(lines)
    cds = dna[29-1:409]
    
    # prepare
    offset = 3
    window = 30
    length = len(cds)
    end = length - window + 1
    
    # print each window segment
    for i in range(0, end, offset):
        print(cds[i:i+window])
    
    # print GC
    for i in range(0, end, offset):
        segment = cds[i:i+window]
        gc_content = (segment.count("G") + segment.count("C")) / len(segment) * 100
        print(f"{segment}: {gc_content}%")
    
    # output to individual fasta files
    for i in range(0, end, offset):
        segment = cds[i:i+window]
        name = f"segment_{i+1}_{i+window}"
        with open(f"./segments/{name}.txt", "w") as f:
            f.write(f">AJ223353 segment {i+1} to {i+window}\n")
            f.write(segment + "\n")
    
    # output to single fasta file
    f_out = open("AJ223353_segments.fasta", "w")
    for i in range(0, end, offset):
        segment = cds[i:i+window]
        name = f"segment_{i+1}_{i+window}"
        f_out.write(f">AJ223353 segment {i+1} to {i+window}\n")
        f_out.write(segment + "\n")
    f_out.close()
    
    
