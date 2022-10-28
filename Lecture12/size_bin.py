#!/usr/local/bin/python

from pathlib import Path

if __name__ == "__main__":
    
    # create size range directories
    for i in range(1, 10):
        bin = Path(f"./{i*100}_{i*100+99}")
        if not bin.exists():
            bin.mkdir()
    
    # process each dna file
    pwd = Path("./")
    for dna_file in pwd.glob("x*.dna"):
        with dna_file.open("r") as f_in:
            count = 0
            for dna in f_in:
                count += 1
                dna = dna.rstrip()
                length = len(dna)
                if length < 100:
                    print(f"Warning: length < 100 in {dna_file.name}")
                    exit()
                output_name = f"{dna_file.stem}_{count}_{length}{dna_file.suffix}"
                size_bin = length // 100
                size_dir = f"{size_bin*100}_{size_bin*100 + 99}"
                output_path = Path(f"./{size_dir}/{output_name}")
                with output_path.open("w") as f_out:
                    f_out.write(dna + "\n")
                
