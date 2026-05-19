# projet_GPI_AF (master training project)

### Project Description

This bioinformatics project aims to analyze the 3D structure of an RNA molecule from a PDB file in order to:

- reconstruct an object-based representation of RNA
- detect hydrogen bonds between nucleotide bases
- identify base pairs involved in secondary structure formation
- generate the RNA primary sequence
- produce a dot-bracket representation of secondary structure

---

### General Pipeline

The program follows these steps:

1. Reading the PDB file
2. Parsing atomic data and reconstructing RNA objects (Atom → Nucleotide → RNA)
3. Detection of hydrogen bonds based on atomic interaction rules
4. Strict validation of base pairs (all expected hydrogen bonds must be present)
5. Generation of RNA secondary structure (dot-bracket format)
6. Extraction of the RNA nucleotide sequence

---

### Biological Modeling 

Base pairing interactions are defined according to:

- Watson-Crick pairs:
  - A–U
  - G–C
- Wobble pair:
  - G–U

Each base pair is considered valid **only if all expected hydrogen bonds are detected**.

A maximum distance threshold of **3 Å** is used to validate atomic interactions.


j'ai dans un premier temps préconfiguré mon bashr pour définir le chemin jusqu'à mon répertoire de travail 

---

### What each file does:

- projet_1.py → Main script (runs the program)
- model.py → Defines the data structures (classes)
- utils.py → Input/output and computation functions
- init.py → Turns the RNA/ folder into a Python package
- 8D28.pdb → Biological dataset (RNA structural data)

---
## Environment setup

This project requires Python 3.

No external dependencies are required.

### 1. Clone the repository
```bash
git clone <your-repo-url>
cd projet_GPI_AF
```

### 2. Set working directory
A working directory path was configured in the `.bashrc` file to simplify access to the project during development.

This allows easier execution of scripts without manually specifying full file paths.

---
## How to run the project

Run the main script with a PDB file as argument, for example : 

```python projet_1.py 8D28.pdb ```