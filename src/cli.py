import argparse
import logging
import yaml
from pathlib import Path
from src.analysis import codon_freq_analysis

# Load configuration
CONFIG_PATH = Path(__file__).parent.parent / "config.yaml"

def load_config():
    with open(CONFIG_PATH, "r") as file:
        return yaml.safe_load(file)

config = load_config()
logging.basicConfig(
    level=config['logging']['level'],
    format=config['logging']['format']
)
logger = logging.getLogger(__name__)

def main():
    logger.info("Starting AGAT CLI")
    parser = argparse.ArgumentParser(description="AGAT: Genome Analysis Toolkit")
    subparsers = parser.add_subparsers(dest="command")

    # Example subcommand
    analyze_parser = subparsers.add_parser("analyze", help="Analyze sequences")
    analyze_parser.add_argument("--input", required=True, help="Input file")

    args = parser.parse_args()
    if args.command == "analyze":
        analyze_sequences(args.input)

def analyze_sequences(input_file):
    logger.info("Performing sequence analysis")
    codon_frequencies = codon_freq_analysis(input_file)
    for codon, freq in codon_frequencies.items():
        print(f"{codon}: {freq:.4f}")

if __name__ == "__main__":
    main()