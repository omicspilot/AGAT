
### Objective
Build a comprehensive command-line tool for genome analysis that demonstrates advanced Python and bioinformatics integration.

### You'll Learn & Use
**Advanced Python:**
- Generators and iterators for large files
- Context managers (`with` statements)
- Decorators for logging and timing
- Type hints and modern Python (3.10+)
- Dataclasses for clean data structures
- Pathlib for file handling
- Argparse for CLI interfaces

**Bioinformatics Tools:**
- BioPython (SeqIO, SeqRecord, Seq)
- Pysam (BAM/SAM manipulation)
- PyVCF or cyvcf2 (variant files)

**Data Science:**
- NumPy for efficient computations
- Pandas for tabular data
- Matplotlib/Seaborn for visualization

### Features to Implement
1. **Multi-format sequence reader** (FASTA, GenBank, EMBL)
   - Lazy loading for huge files
   - Statistics calculation (GC content, length distributions, N50)
   
2. **Advanced sequence analysis**
   - Codon usage analysis and visualization
   - ORF prediction with multiple frames
   - Repeat sequence detection
   - K-mer counting and frequency analysis
   
3. **Visualization suite**
   - GC content sliding window plots
   - Codon usage heatmaps
   - Sequence composition bar charts
   - Coverage plots for alignments

4. **Export functionality**
   - JSON/CSV reports
   - HTML interactive reports
   - PDF summary documents

### Technical Requirements
- Clean OOP design with classes
- Comprehensive docstrings
- Unit tests (pytest)
- CLI with multiple subcommands
- Configuration file support (YAML/JSON)
- Logging at different levels
- Progress bars for long operations (tqdm)

### Biological Context
*When analyzing genomes, understanding composition patterns helps identify:*
- GC-rich vs AT-rich regions (related to gene density, recombination)
- Codon usage bias (expression levels, organism-specific preferences)
- Repetitive elements (transposons, tandem repeats)
- Coding vs non-coding regions

### Deliverables
- GitHub repository with complete code
- README with installation and usage
- Example datasets and outputs
- Test suite with >80% coverage
- Documentation (Sphinx or mkdocs)
