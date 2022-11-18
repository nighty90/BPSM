#!/usr/local/bin/python

import re


def get_fragments(digest_sites, sequence):
    digest_result = []
    start = 0
    for site in digest_sites:
        fragment = sequence[start:site]
        digest_result.append(fragment)
        start = site
    digest_result.append(sequence[start:])
    return digest_result


if __name__ == "__main__":

    with open("long_dna.txt", "r") as f:
        dna = f.read()
        dna = dna.rstrip()

    print("Digest the sequence with BpsmI")
    bpsm1_regex = r"A[ATCG]TAAT"
    single_digest_site = [match.end()-3 for match in re.finditer(bpsm1_regex, dna)]
    single_digest = get_fragments(single_digest_site, dna)
    print(f"Fragment sequences:\n{single_digest}")
    print(f"Fragment length:\n{[len(x) for x in single_digest]}")

    print("="*80)

    print("Digest the sequence with BpsmI and BpsmII")
    bpsm2_regex = r"GC[AG][AT]TG"
    bpsm2_digest_site = [match.end()-2 for match in re.finditer(bpsm2_regex, dna)]
    double_digest_site = single_digest_site + bpsm2_digest_site
    double_digest_site.sort()
    double_digest = get_fragments(double_digest_site, dna)
    print(f"Fragment sequences:\n{double_digest}")
    print(f"Fragment length:\n{[len(x) for x in double_digest]}")
