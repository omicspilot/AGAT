import sys
from pathlib import Path

# Add the src directory to the Python path
sys.path.append(str(Path(__file__).parent.parent / "src"))

import pytest
from src.analysis import codon_freq_analysis

TEST_FASTA = Path(__file__).parent / "test_data.fasta"
DNA_SEQ1="ATGCCCCCCTACACCGTGGTGTACTTCCCCGTGAGAGGCAGATGCGCCGCCCTGAGAATGCTGCTGGCCGACCAGGGCCAGAGCTGGAAGGAGGAGGTGGTGACCGTGGAGACCTGGCAGGAGGGCAGCCTGAAGGCCAGCTGCCTGTACGGCCAGCTGCCCAAGTTCCAGGACGGCGACCTGACCCTGTACCAGAGCAACACCATCCTGAGACACCTGGGCAGAACCCTGGGCCTGTACGGCAAGGACCAGCAGGAGGCCGCCCTGGTGGACATGGTGAACGACGGCGTGGAGGACCTGAGATGCAAGTACATCAGCCTGATCTACACCAACTACGAGGCCGGCAAGGACGACTACGTGAAGGCCCTGCCCGGCCAGCTGAAGCCCTTCGAGACCCTGCTGAGCCAGAACCAGGGCGGCAAGACCTTCATCGTGGGCGACCAGATCAGCTTCGCCGACTACAACCTGCTGGACCTGCTGCTGATCCACGAGGTGCTGGCCCCCGGCTGCCTGGACGCCTTCCCCCTGCTGAGCGCCTACGTGGGCAGACTGAGCGCCAGACCCAAGCTGAAGGCCTTCCTGGCCAGCCCCGAGTACGTGAACCTGCCCATCAACGGCAACGGCAAGCAGTAG\n"

def test_codon_freq_analysis():
    # Create a temporary FASTA file for testing
    with open(TEST_FASTA, "w") as f:
        f.write(f">seq1\n{DNA_SEQ1}")

    num_codons_dna_seq1 = round(len(DNA_SEQ1) / 3)
    num_unique_codons = len(set(DNA_SEQ1[i:i+3] for i in range(0, len(DNA_SEQ1) - 2, 3)))
    print(num_codons_dna_seq1, num_unique_codons)
    # Run the analysis for non unique codon count
    res, res_unique = codon_freq_analysis(TEST_FASTA)
    print(res["ATG"])
    print(res["CTG"])
    print(res["TAG"])

    # Check results
    assert res["ATG"] == 3 / num_codons_dna_seq1
    assert "CGT" not in res
    assert res["TAG"] == 1 / num_codons_dna_seq1
    # unique counters
    assert res_unique["ATG"] == 3 / num_unique_codons
    assert res_unique["TAG"] == 1 / num_unique_codons

    # Clean up
    TEST_FASTA.unlink()