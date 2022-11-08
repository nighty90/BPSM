#!/usr/local/bin/python

def high_unknown(n_seq, threshold=0.3):
    n_seq = n_seq.upper()
    known_base_prop = [n_seq.count(base) for base in "ATCG"]
    return 1 - sum(known_base_prop)/len(n_seq) > threshold
    
if __name__ == "__main__":
    assert high_unknown("atcggghioxyukatagatc") == True
    assert high_unknown("atcggghioxyukatagatc", 0.5) == False
    assert high_unknown("atcggghioxyaaatagatc") == False
    print("clear!")