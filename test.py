#!/usr/bin/env python3

"""formation d'une classe orienté objet, les fonctions de la classe sont appelées des méthodes, permet d'organiser les données de magnière plus simple 

class Protein : # une classe est un type d'objet 
    def __init__(self, name): # init et self sont une convention ; il faut toujours les mettrer
        self.nom = name
    
protein1 = Protein('hemoglobin') # protein1 est une instance de la classe Protein
protein2 = Protein('cytochrom C')
protein1.nom = 'Hgb' # nous montre qu'on peut changer les données même lorsqu'elles sont déjà définit


print(protein1.nom)
print(protein2.nom)

class Protein :
    def __init__(self,name):
        self.folded = True # on part du principe que toutes les proteines sont d'abord repliées
        self.name = name
        
    
    def unfold(self):
        self.folded = False

    def fold(self):
        self.folded = True

class FoldableProtein(Protein):
    def fold(self) :
        print(self.name + 'is not foldable')

prot1 = Protein('hgb')
prot2 = Protein('cytochrome C')
prot3 = FoldableProtein('ovalbumin')

proteome = [prot1,prot2,prot3]

print('before')
for prot in proteome :
    print (prot.name + ' is folded:' , prot.folded)

for prot in proteome :
    prot.unfold()

print('after')
for prot in proteome:
    print (prot.name + ' is folded: ',prot.folded)

for prot in proteome :
    prot.fold()

print('after')
for prot in proteome:
    print (prot.name + ' is folded ?',prot.folded)

for prot in proteome:
    print('Protein '+ prot.name + 'is a Protein ',isinstance(prot,Protein))
    print('Protein '+ prot.name + 'is a FoldableProtein ',isinstance(prot,FoldableProtein)) """ 

# lire le contenu d' un fichier 
lines =[]
with open('8D28.pdb','r') as file:
    for i in range(1000):
        lines.append(file.readline())

for line in lines :
    if line[:4] =='ATOM' : # récupération des lignes qui commencent pas ATOM
        print(line)

# on le décompose en 3  partis
# un petit script executables qui importe les modules qu'on a créé précédemment : 
# module modèle (description de l'ARN en classe/objects/methodes ...)
# module utilitaire : fonction de lecture de PDB, produit le résultat final (chaine de caractères DBN)












