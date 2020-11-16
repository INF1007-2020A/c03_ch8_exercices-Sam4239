#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Exercice 1
#def compare_files(fname1, fname2):
    #with open(fname1, "r") as f, open(fname2, "r") as p:
        #c = f.read(1)
        #k = p.read(1)
        #while c != '' and k != '':
            #if c != k:
                #position =f.tell()
                #print(f"La difference est a la position {position} entre {c} et {k}")
                #break
            #c = f.read(1)
            #k = p.read(1)
#Exercice 5
def nombres(fname) : 
    with open(fname, mode = "r") as f:
        donnees = f.read()

    liste_nombres = []
    mots = donnees.split()
    for mot in mots:
        if mot.isdigit():
            liste_nombres.append(mot)
    liste_nombres.sort(key = lambda x: int(x))
    print(liste_nombres)

    #Alternative
    #liste_nombres = sorted([int(mot) for mot in donnees.split() if mot isdigit()])
    #print(liste_nombre)


# Exercice quelque chose
import os
filename = "chemin du document"
with open(filename, mode = "r") as file:
    mots = file.read().split()
    mots.sort(key=lambda x: len(x), reverse=True)
    print(mots)




if __name__ == '__main__':
    # Exercice 1
    #compare_files(fname1 ="exemple.txt", fname2 = "exemple2.txt")
    #Exercice 5
    nombres(fname="exemple.txt")
    pass
