#coding: utf-8

import pickle

"""
    mode d'ouverture : r  (lecture seul)
                       w  (écriture avec remplacement)
                       a  (écriture avec ajout en fin de fichier)
                       x  (lecture et écriture)
                       r+ (lecture/ecriture dans un même fichier)
                       
    Lecture          : read(), readline(), realdlines()
    Ecriture         : write()
"""

#----------------------- POUR LA LECTURE -----------------------------------------------------

fic = open("./fichier.txt","r"); #manokatra anle fichier

print(fic.read());

# afaka atao iany koa ny mampiasa ny methode readline() mba ahafahana maka ny zavatra ao anatinle fichier ho ligne par ligne

# fichier = open("./fichier.txt","r")
# f = fichier.readline()

# print(f)
# f = fichier.readline()

# print(f)

fic.close(); # rehefa nosokafana dia tsy maintsy akatona ilay fichier (!)

# (!!!) afaka soratana amin'ny fomba hafa iany koa io syntae io

with open("./fichier.txt","r") as fics:
    F = fics.read()
    print(F)
    # Pas besoin de close (tsy mila akatona rehefa ohatr'izao ilay syntsaxe anoratana azy)

#---------------------------- POUR LA L'ECTURE ----------------------------------------------------

with open("./fichier.txt","w") as ecriture:
    print(ecriture.write("Tsaroana\n"))
    print(ecriture.write("19 ans\n"))
    print(ecriture.write("Jazz\n"))
    
#--------------------------- avadika binaire amin'izay fa tsy atao soratra normal intsony----------

class Player:
    def __init__ (self,nom,level):
        self.nom = nom
        self.level = level
    
    def izaAho(self):
        print("{} ({})".format(self.nom,self.level))
        
# p1 = Player("Tsaroana",19) # (!!!) TSY ILAINA INTSONY REHEFA VITA NY SAUVEGARDER ANY
# p1.izaAho()

# with open("data.data","wb") as ficB:  (!!!) HO ANLE FISAUVEGARDENA AZY FOTSINY INY
#     record = pickle.Pickler(ficB)
#     record.dump(p1) # (faire une copie de l'objet) (!!!) besoin d'un objet à stocker

with open("data.data","rb") as readB:
    get_record = pickle.Unpickler(readB)
    player_one = get_record.load()

player_one.izaAho()
    
 # IO ZAVATRA IO DIA TENA ILAINA MBA I-SAUVEGARDERNA NY OBJET IRAY 
 
 #--------------------amaky anle zavatra n-sauvegardena amin'izay ary eh fa ataontsika eo ambony iany ny modificationany--------------------------