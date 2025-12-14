import logging
from Bio import SeqIO
from collections import Counter

logger = logging.getLogger(__name__)

def codon_freq_analysis(input_file):
  """
  Perform codon usage analysis on a given FASTA file.

  Args:
      input_file (str): Path to the input FASTA file.
      unique (bool): count unique codons in total codons

  Returns:
      dict: Codon usage frequencies.
  """
  logger.info(f"Starting codon usage analysis for {input_file}")

  codon_counts = Counter()
  
  total_codons = round(len(input_file) / 3)
  total_unique_codons = len(set(input_file[i:i+3] for i in range(0, len(DNA_SEQ1) - 2, 3)))

  try:
    for record in SeqIO.parse(input_file, "fasta"):
      sequence = str(record.seq).upper()
      # Count codons in the sequence, excluding incomplete codons at the end
      for i in range(0, len(sequence) - len(sequence) % 3, 3):
        codon = sequence[i:i+3]
        codon_counts[codon] += 1

    # Calculate frequencies
    codon_frequencies = {codon: count / total_codons for codon, count in codon_counts.items()}
    codon_unique_frequencies = {codon: count / total_unique_codons for codon, count in codon_counts.items()}
    logger.info("Codon usage analysis completed successfully.")
    return codon_frequencies, codon_unique_frequencies

  except Exception as e:
    logger.error(f"Error during codon usage analysis: {e}")
    raise