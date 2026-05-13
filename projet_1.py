#!/usr/bin/env python3

import sys
import RNA.utils as utils 

if len(sys.argv) !=2 : # vecteur d'argument ; permet de convertir tout ce qu'il y a sur la ligne de commande en chaine de caractères
    print('error : incorrect number of argument')
    print('>' + sys.argv[0] + 'file.pdb')
    exit()

pdb_name = sys.argv[1]
"""RNA = utils.parsePDB(pdb_name)
utils.generate_dot_bracket(RNA)"""

with open (pdb_name , 'r') as file :
    line = file.readline()
    while line[0:6].strip() != 'TER':
        if line [0:6].strip()=='ATOM':
            name_atom = line[12:16].strip()
            x= line[30:38].strip()
            y= line[38:46].strip()
            z= line[46:54].strip()
            print(name_atom, x, y, z)
        line = file.readline()





