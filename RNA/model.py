# DEFINITION DE LA CLASSE ATOME 

class Atom: 

    def __init__(self, name, x, y, z): # on stock le nom et les coordonées x,y et z 
        self.name = name
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

# Cette fonction calcule la distance 3D entre deux atomes basée sur le théorème de Pythagore, pour cela on met les valeurs au carré (on évite également les valeurs négatives)
    def distance(self, other): 
        return ((self.x - other.x)**2 + (self.y - other.y)**2 + (self.z - other.z)**2) ** 0.5
# on additionne les différences entre les deux atomes sur l'axe x, y et z. On les met au carré et on fait la racine carré 

# DEFINITION DE LA CLASSE NUCLEOTIDE

class Nucleotide:

    def __init__(self, base, number): # on stock le nom de la base (AUCG) et son numéro qu'on retrouve dans le fihier PDB
        self.base = base
        self.number = number
        self.atoms = [] # création d'une liste vide où on va mettre tous les atomes

    def add_atom(self, atom): # méthode qui permet d’ajouter un atome au nucléotide
        self.atoms.append(atom)  # on ajoute l’objet Atom dans la liste des atomes

# DEFINITION DE LA CLASSE RNA 

class RNA:

    def __init__(self):
        self.nucleotides = [] # on initialise une liste vide qui contiendra tous les nucléotides de l’ARN

    def add_nucleotide(self, nt):  # Méthode pour ajouter un nucléotide à la molécule
        self.nucleotides.append(nt)  # on ajoute le nucléotide nt dans la liste

    def get_sequence(self):  # Méthode qui reconstruit la séquence primaire de l’ARN
        seq = ""  # on initialise une chaîne de caratères vide pour construire la séquence
        
        for nt in self.nucleotides:  # on parcourt tous les nucléotides dans l’ordre
            seq = seq + nt.base  # Ajoute la base (A, U, G ou C) à la séquence
        
        return seq  # Retourne la séquence complète sous forme de chaîne de caractères