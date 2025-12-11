import sys
from pathlib import Path

# Add the src directory to the Python path
sys.path.append(str(Path(__file__).parent.parent / "src"))

import pytest
from src.analysis import codon_freq_analysis

TEST_FASTA = Path(__file__).parent / "test_data.fasta"

def test_codon_freq_analysis():
    # Create a temporary FASTA file for testing
    with open(TEST_FASTA, "w") as f:
        f.write(">seq1\nATGCGTACGTAG\n>seq2\nATGCGTACG")

    # Run the analysis for non unique codon count
    result = codon_freq_analysis(TEST_FASTA)

    # Check results
    assert result["ATG"] == 2 / 7
    assert result["CGT"] == 2 / 7
    assert result["TAG"] == 1 / 7
    
    # Run the analysis for non unique codon count
    result = codon_freq_analysis(TEST_FASTA, unique=True)

    # Check results
    assert result["ATG"] == 2 / 4
    assert result["CGT"] == 2 / 4
    assert result["TAG"] == 1 / 4

    # Clean up
    TEST_FASTA.unlink()