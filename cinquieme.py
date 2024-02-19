#coding:utf-8

"""
    on va maintenant parler de la boucle comme while , for
"""

compteur = 0

while compteur < 5:
    print("salama eh")
    compteur += 1;
    
print("tsy ao anaty boucle intsony...\n")

jeu_lance = True

while jeu_lance:
    commande = input("> ")
    if commande == "again" : 
        continue
    elif commande == "quit" :
        print("")
        break #jeu_lance = False
    elif commande == "salama eh" :
        print("bonjour eh")
    else :
        print("commande introuvable")

print("maintenant on est sortie de la boucle while\n")

# ny fomba fampiasa ny boucle for aty amin'ny python dia afa tanterala mihintsy fa tsy mitovy ny any amin'ny fampiasana
# boucle any amin'ny langage de programmation hafa satria tahaky ny mitovitovy amin'ny foreach le izy

phrase = "Salama tompoko oh inona ny vaovao maresaka eh"

for mpaka in phrase:
    print(mpaka)
    if mpaka == "S" :
        print("mlay izany eh")
    

factoriel = 1;
fact = 1;
x = 3;

while factoriel <= 5 :
    fact = factoriel * fact;
    x = 3 * x;
    factoriel += 1;
    
print("factoriel de 5 est egale à {}".format(fact))
print("3 à la puissance 6 est egale à {}".format(x))