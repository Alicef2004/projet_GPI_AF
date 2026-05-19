from RNA.model import Atom, Nucleotide, RNA


# 1. REGLES DE LIAISONS HYDROGÈNE (Watson-Crick + wobble)
# création d'un dictionnaire appelé BASE_PAIRS qui prend en clé le nom des deux BA qui sont liées et les valeurs correspondent aux atomes qui sont impliqués dans les liaisons hydrogènes

BASE_PAIRS = {
    ("C", "G"): [("N4", "O6"), ("N3", "N1"), ("O2", "N2")],
    ("G", "C"): [("O6", "N4"), ("N1", "N3"), ("N2", "O2")],

    ("A", "U"): [("N6", "O4"), ("N1", "N3")],
    ("U", "A"): [("O4", "N6"), ("N3", "N1")],

    ("G", "U"): [("O6", "N3"), ("N1", "O2")],
    ("U", "G"): [("N3", "O6"), ("O2", "N1")]
}

# 2. PARSING DU PDB

def parse_pdb(pdb_file): # cette fonction transforme un fichier PDB en objet RNA

    rna = RNA()  # Création de l'instance de classe vide (il contindra tous les nucléotides)

    current_number = None # il stocke le numéro du nucléotide en cours de lecture
    current_nt = None # Stocke l’objet nucléotide courant

    with open(pdb_file, "r") as file: # ouverture du fichier pdb_file 
        for line in file: # Parcours ligne par ligne du fichier

            if line.startswith("TER"):  # Fin de chaîne biologique
                break  # On arrête complètement le parsing

            if line.startswith("ATOM"): # quand la ligne commence par ATOM on récupère :
                atom_name = line[12:16].strip() # le nom de l'atome (ex : N6)
                base = line[17:20].strip() # le nom de la BA (ex : C)
                nt_number = int(line[22:26].strip()) # le numéro du nucléotide dans la séquence de l'ARN

                x = float(line[30:38].strip()) # la position x de l'atome
                y = float(line[38:46].strip()) # la position y de l'atome
                z = float(line[46:54].strip()) # la position z de l'atome
                atom = Atom(atom_name, x, y, z) # on transfert la position de l'atome et son nom dans l'instance de classe atom

                if nt_number != current_number: # Si on change de nucléotide :
                    current_nt = Nucleotide(base, nt_number) # on créé un nouveau nucléotide
                    rna.add_nucleotide(current_nt) # on ajoute un nucléotide à l’objet RNA
                    current_number = nt_number # on met à jour le nucléotide courant

                current_nt.add_atom(atom) # on ajoute l’atome au nucléotide actuel

    return rna # Nous retourne la structure RNA complète


# 3. DISTANCE EUCLIDIENNE 
# Cette fonction calcule la distance 3D entre deux atomes basée sur le théorème de Pythagore, pour cela on met les valeurs au carré (on évite également les valeurs négatives)

def distance(a1, a2): # on choisit deux atomes 
    return ((a1.x - a2.x) ** 2 + (a1.y - a2.y) ** 2 + (a1.z - a2.z) ** 2) ** 0.5
# on additionne les différences entre les deux atomes sur l'axe x, y et z. On les met au carré et on fait la racine carré 

# 4. TEST LIAISON HYDROGÈNE
# Cette fonction vérifie s’il existe toutes les liaisons hydrogènes entre deux nucléotides

def has_hbond(nt1, nt2):  

    possible_paire_bases = (nt1.base, nt2.base)  # Crée la paire de bases 

    if possible_paire_bases not in BASE_PAIRS:  # Vérifie si cette paire est biologiquement autorisée
        return False  # Si non → pas de liaison possible

    required_bonds = BASE_PAIRS[possible_paire_bases]  # Liste des liaisons hydrogène attendues pour cette paire
    found_bonds = 0  # Compteur du nombre de liaisons correctement détectées

    for a1, a2 in required_bonds:  # Parcourt chaque liaison attendue 
        bond_found = False  # Indique si cette liaison spécifique a été trouvée

        for atom1 in nt1.atoms:  # Parcourt tous les atomes du premier nucléotide
            if atom1.name != a1:  # Ignore les atomes qui ne correspondent pas au donneur attendu
                continue  # Passe à l’atome suivant

            for atom2 in nt2.atoms:  # Parcourt tous les atomes du second nucléotide
                if atom2.name != a2:  # Ignore les atomes qui ne correspondent pas à l’accepteur attendu
                    continue  # Passe à l’atome suivant

                # Vérifie si les deux atomes sont suffisamment proches pour former une liaison H
                if distance(atom1, atom2) <= 3.0:

                    bond_found = True  # La liaison spécifique est validée
                    break  # On arrête la boucle sur atom2 (inutile de continuer)

            if bond_found:  # Si la liaison a été trouvée
                break  # On arrête la boucle sur atom1 aussi

        if bond_found:  # Si cette liaison attendue est bien présente
            found_bonds += 1  # On incrémente le compteur de liaisons valides

    # Vérifie que toutes les liaisons attendues sont présentes
    return found_bonds == len(required_bonds)  # True si complet, sinon False

# 5. DETECTION DES PAIRES DE BASES

def find_base_pairs(rna):  # Détecte toutes les paires de bases valides dans l’ARN

    pairs = []  # Liste des paires 
    nts = rna.nucleotides  # raccourci pour accéder à la liste des nucléotides de l’ARN

    for i in range(len(nts)):  # Parcourt chaque nucléotide comme premier élément de la paire
        for j in range(i + 1, len(nts)):  # Parcourt les suivants pour éviter doublons et auto-paires
            # Vérifie si les deux nucléotides forment une paire complète de liaisons hydrogène
            if has_hbond(nts[i], nts[j]):
                pairs.append((i, j))  # Ajoute la paire validée

    return pairs  # Retourne toutes les paires détectées

# 6. DOT-BRACKET
# Cette fonction transforme les paires de bases en notation structure secondaire

def generate_dot_bracket(rna, pairs):  # rna = objet RNA, pairs = liste des paires (i, j)
    n = len(rna.nucleotides)  # Nombre total de nucléotides dans l’ARN
    db = ["."] * n  # Initialise une structure remplie de "." (non apparié)

    for i, j in pairs:  # Parcourt toutes les paires de bases détectées
        db[i] = "("  # Marque le début de la paire avec une parenthèse ouvrante
        db[j] = ")"  # Marque la fin de la paire avec une parenthèse fermante

    return "".join(db)  # Convertit la liste en chaîne de caractères finale

# 7. EXTRACTION DE LA SEQUENCE RNA
# Cette fonction reconstruit la séquence nucléotidique à partir de l’objet RNA

def get_sequence(rna):  # rna est un objet contenant une liste de nucléotides
    seq = ""  # initialise une chaîne vide qui va contenir la séquence

    for nt in rna.nucleotides:  # parcourt tous les nucléotides dans l’ordre
        seq += nt.base  # ajoute la base (A, U, G ou C) à la séquence

    return seq  # retourne la séquence complète sous forme de chaîne de caractères