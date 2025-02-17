def transcribe_dna_to_rna(dna_sequence: str) -> str:
    return dna_sequence.replace("T", "U")


def translate_rna_to_protein(rna_sequence: str) -> str:
    genetic_code: Dict[str, str] = {
        "AUA": "I", "AUC": "I", "AUU": "I", "AUG": "M",
        "ACA": "T", "ACC": "T", "ACG": "T", "ACU": "T",
        "AAC": "N", "AAU": "N", "AAA": "K", "AAG": "K",
        "AGC": "S", "AGU": "S", "AGA": "R", "AGG": "R",
        "CUA": "L", "CUC": "L", "CUG": "L", "CUU": "L",
        "CCA": "P", "CCC": "P", "CCG": "P", "CCU": "P",
        "CAC": "H", "CAU": "H", "CAA": "Q", "CAG": "Q",
        "CGA": "R", "CGC": "R", "CGG": "R", "CGU": "R",
        "GUA": "V", "GUC": "V", "GUG": "V", "GUU": "V",
        "GCA": "A", "GCC": "A", "GCG": "A", "GCU": "A",
        "GAC": "D", "GAU": "D", "GAA": "E", "GAG": "E",
        "GGA": "G", "GGC": "G", "GGG": "G", "GGU": "G",
        "UCA": "S", "UCC": "S", "UCG": "S", "UCU": "S",
        "UUC": "F", "UUU": "F", "UUA": "L", "UUG": "L",
        "UAC": "Y", "UAU": "Y", "UAA": "*", "UAG": "*",
        "UGC": "C", "UGU": "C", "UGA": "*", "UGG": "W"
    }
    
    protein = ""
    for i in range(0, len(rna_sequence) - 2, 3):
        codon = rna_sequence[i:i+3]
        protein += genetic_code.get(codon, "?")  # "?" for unknown codons

    return protein

def dna_to_protein(dna_sequence: str) -> str:
    # Step 1: Transcription (DNA → RNA)
    rna_sequence = transcribe_dna_to_rna(dna_sequence)
    
    # Step 2: Translation (RNA → Protein)
    protein_sequence = translate_rna_to_protein(rna_sequence)
    
    return protein_sequence

# task:
dna_sequence = "ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG"
protein = dna_to_protein(dna_sequence)
print(f"Final Protein Sequence: {protein}")

