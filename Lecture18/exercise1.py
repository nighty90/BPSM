#!/usr/local/bin/python

import matplotlib.pyplot as plt

if __name__ == "__main__":
    ecoli = open("ecoli.txt").read().replace('\n', '').upper()
    base_5e4 = ecoli[0:int(5e4)]
    base_1e5 = ecoli[0:int(1e5)]
    loop_dict = {"base_5e4": base_5e4, "base_1e5": base_1e5, "ecoli": ecoli}
    window = 1000
    count = 0
    plt.figure(figsize=(21, 28))
    plt.suptitle(f"AT content in the E coli genome (window size is 1000)", fontsize=20)
    for name, seq in loop_dict.items():
        count += 1
        print(f"Calculating AT content for {name}")
        at_content = []
        for start in range(len(seq) - window):
            win = seq[start:(start + window)]
            at_content.append((win.count("A") + win.count("T")) / window)
        print(f"Drawing subplot")
        plt.subplot(3, 1, count)
        plt.plot(at_content, label="A", linewidth=1)
        plt.ylabel('AT content')
        plt.xlabel('Position on sequence')
        if name == "base_5e4":
            plt.title("In the first 5e4 bases", fontsize=14)
        elif name == "base_1e5":
            plt.title("In the first 1e5 bases", fontsize=14)
        else:
            plt.title("In the whole genome", fontsize=14)
    plt.savefig("Exercise1.png")
    plt.show()
    plt.close()
