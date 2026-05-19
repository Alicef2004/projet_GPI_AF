#!/usr/bin/env python3  
# Indique que le script doit être exécuté avec Python 3 

import sys  # Module pour récupérer les arguments passés en ligne de commande
import RNA.utils  # Import de ton module utilitaire contenant les fonctions du projet

# Vérifie que l'utilisateur a bien fourni un fichier en argument
if len(sys.argv) != 2:

    print("Usage : python main.py file.pdb")  # Message d'aide si mauvaise utilisation
    exit()  # Arrête le programme si l'argument est incorrect


pdb_file = sys.argv[1] # Récupère le nom du fichier PDB passé en argument
rna = RNA.utils.parse_pdb(pdb_file)  # Convertit le fichier PDB en objet RNA (Atom → Nucleotide → RNA)
pairs = RNA.utils.find_base_pairs(rna) # Détecte toutes les paires de bases via les liaisons hydrogène
dbn = RNA.utils.generate_dot_bracket(rna, pairs)  # Transforme les paires en format dot-bracket

# Affichage
print("Sequence and Dot-bracket :") 
print(rna.get_sequence())
print(dbn)

