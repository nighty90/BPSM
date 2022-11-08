#!/usr/local/bin/python

valid_aa = {"R", "H", "K", "D", "E", 
            "S", "T", "N", "Q", "C",
            "U", "G", "P", "A", "V",
            "I", "L", "M", "F", "Y",
            "W"}
            
default_aa_list = ["A", "I", "L", "M",
                   "F", "W", "Y", "V"]

def amino_percent_1(p_seq, aa):
    p_seq = p_seq.upper()
    aa = aa.upper()
    assert set(p_seq) - valid_aa == set()
    assert aa in valid_aa
    return p_seq.count(aa) / len(p_seq) * 100
    
def amino_percent_2(p_seq, aa_list=default_aa_list):
    p_seq = p_seq.upper()
    aa_list = [aa.upper() for aa in aa_list]
    assert set(p_seq) - valid_aa == set()
    assert set(aa_list) - valid_aa == set()
    p_seq_length = len(p_seq)
    aa_percent = [p_seq.count(aa) / p_seq_length * 100 for aa in aa_list]
    return sum(aa_percent)


if __name__ == "__main__":
    assert round(amino_percent_1("MSRSLLLRFLLFLLLLPPLP", "M")) == round(5)
    assert round(amino_percent_1("MSRSLLLRFLLFLLLLPPLP", "r")) == round(10)
    assert round(amino_percent_1("MSRSLLLRFLLFLLLLPPLP", "L")) == round(50)
    assert round(amino_percent_1("MSRSLLLRFLLFLLLLPPLP", "Y")) == round(0)
    print("q1 clear!")
    assert round(amino_percent_2("MSRSLLLRFLLFLLLLPPLP", ["M"])) == 5
    assert round(amino_percent_2("MSRSLLLRFLLFLLLLPPLP", ['F', 'S', 'L'])) == 70
    assert round(amino_percent_2("MSRSLLLRFLLFLLLLPPLP")) == 65
    print("q2 clear!")
