#!/usr/bin/env python3

import sys
import RNA.utils as utils 

if len(sys.argv) !=2 : # vecteur d'argument ; permet de convertir tout ce qu'il y a sur la ligne de commande en chaine de caractères
    print('error : incorrect number of argument')
    print('>' + sys.argv[0] + 'file.pdb')
    exit()

pdb_name = sys.argv[1]

RNA = utils.parsePDB(pdb_name)
print (RNA.sequence)
utils.generate_dot_bracket(RNA)


