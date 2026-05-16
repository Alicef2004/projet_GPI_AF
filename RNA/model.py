class Atom:

    def __init__(self, name, x, y, z):
        self.name = name
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

    def distance(self, other):
        return ((self.x - other.x)**2 +
                (self.y - other.y)**2 +
                (self.z - other.z)**2) ** 0.5


class Nucleotide:

    def __init__(self, base, number):
        self.base = base
        self.number = number
        self.atoms = []

    def add_atom(self, atom):
        self.atoms.append(atom)


class RNA:

    def __init__(self):
        self.nucleotides = []

    def add_nucleotide(self, nt):
        self.nucleotides.append(nt)

    def get_sequence(self):
        seq = ""
        for nt in self.nucleotides:
            seq += nt.base
        return seq