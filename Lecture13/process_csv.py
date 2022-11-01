#!/usr/local/bin/python

if __name__ == "__main__":
    with open("data.csv", "r") as f:
        all_lines = f.readlines()
        
    print("sub question 1".center(80, "="))
    for line in all_lines:
        row = line.rstrip().split(",")
        if (row[0] == "Drosophila melanogaster" 
                or row[0] == "Drosophila simulans"):
            print(f"species: {row[0]}\tgene name: {row[2]}")
            
    print("sub question 2".center(80, "="))
    for line in all_lines:
        row = line.rstrip().split(",")
        gene_length = len(row[1])
        if 90 <= gene_length <= 110:
            print(f"gene name: {row[2]}\tlength: {gene_length}")
    
    print("sub question 3".center(80, "="))
    for line in all_lines:
        row = line.rstrip().split(",")
        seq = row[1].upper()
        at_content = (seq.count("A") + seq.count("T")) / len(seq)
        expression = int(row[3])
        if at_content < 0.5:
            print(f"gene name: {row[2]}\tAT content: {at_content}")
        elif expression > 200:
            print(f"gene name: {row[2]}\texpression: {row[3]}")
        else:
            pass
    
    print("sub question 4".center(80, "="))
    for line in all_lines:
        row = line.rstrip().split(",")
        gene_name = row[2]
        species = row[0]
        if ((gene_name.startswith("k") or gene_name.startswith("h")) 
                and species != "Drosophila melanogaster"):
            print(f"gene name: {gene_name}\tspecies: {species}")
            
    print("sub question 5".center(80, "="))
    for line in all_lines:
        row = line.rstrip().split(",")
        seq = row[1].upper()
        at_content = (seq.count("A") + seq.count("T")) / len(seq)
        if at_content < 0.45:
            print(f"The AT content of {row[2]} is low: {at_content:.2}")
        elif at_content <= 0.65:
            print(f"The AT content of {row[2]} is medium: {at_content:.2}")
        else:
            print(f"The AT content of {row[2]} is high: {at_content:.2}")