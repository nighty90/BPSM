#!/usr/local/bin/python

import re

if __name__ == "__main__":
    accessions = ["xkn59438", "yhdck2", "eihd39d9", "chdsye847",
                  "hedle3455", "xjhd53e", "45da", "de37dp"]
    print("Condition: contain the number 5")
    print([x for x in accessions if re.search(r"5", x)])
    print("Condition: contain the letter d or e")
    print([x for x in accessions if re.search(r"[de]", x)])
    print("Condition: contain the letters d and e in that order")
    print([x for x in accessions if re.search(r"d.*e", x)])
    print("Condition: contain the letters d and e in that order with a single letter between them")
    print([x for x in accessions if re.search(r"d.e", x)])
    print("Condition: contain both the letters d and e in any order")
    print([x for x in accessions if re.search(r"d.*e", x) or re.search(f"e.*d", x)])
    print("Condition: start with x or y")
    print([x for x in accessions if re.search(r"^[xy]", x)])
    print("Condition: start with x or y and end with e")
    print([x for x in accessions if re.search(r"^[xy].*e$", x)])
    print("Condition: contains any 3 numbers in any order")
    print([x for x in accessions if len(re.findall(r"\d", x)) == 3])
    print("Condition: contains 3 different numbers in the accession")
    print([x for x in accessions if len(set(re.findall(r"\d", x))) == 3])
    print("Condition: contain three or more numbers in a row")
    print([x for x in accessions if re.search(r"\d{3,}", x)])
    print("Condition: end with d followed by either a, r or p")
    print([x for x in accessions if re.search(r"d[arp]$", x)])
