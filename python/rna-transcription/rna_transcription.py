def to_rna_if(dna_strand):
    rna = ""
    for n in dna_strand:
        if n == "G":
            rna += "C"
        elif n == "C":
            rna += "G"
        elif n == "A":
            rna += "U"
        elif n == "T":
            rna += "A"
    return rna


TRANSLATION = {
    "G": "C",
    "C": "G",
    "A": "U",
    "T": "A"
}

def to_rna_dict(dna_strand):
    rna = ""
    for n in dna_strand:
        rna += TRANSLATION[n]
    return rna


def to_rna(dna_strand):
    trans = str.maketrans("GCTA", "CGAU")
    return dna_strand.translate(trans)
