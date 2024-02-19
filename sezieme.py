#coding: utf-8

"""
    on va parler maintenant de la dictionnaire
        pour declarer un variable de type dictionnaire on doit ecrire le syntaxe suivant
            dictionnaire = {<cle> : <valeur>}
        
        acceder a une valeur:
            dictionnaire[<cle>]
        
        modifier et ajouter un valeur:
            dictionnaire[<cle>] = <valeur>

        supression :
            del dictionnaire[<cle>]
            dictionnaire.pop([<le>])
        
        copie de dictionnaire :
            dico = dictionnaire.copy()
"""

dictionnaire = {"nom":"Tsaroana",1:True}

print(type(dictionnaire))

# pour acceder a un element en dictionnaire il faut ecrire le syntaxe suivant

print(dictionnaire["nom"])
print(dictionnaire[1])

# pour ajouter un element dans un dico alors on doit ecrire

dictionnaire["classe"] = "je suis en 3 eme annee de liçance"

print(dictionnaire["classe"])

# on peut aussi faire de la modification

dictionnaire["nom"] = "Jazz"

print(dictionnaire["nom"])

cle = input("entrer un cle qui peut etre dans le dico: ")

if cle in dictionnaire:
    print("Yaya...")
else:
    print("NoNo...")
    
# afaka atao iany koa ny mrecuperer ny key anle zavatra

for cle in dictionnaire.keys():
    print(cle)
    
#afaka atao iany koa ny mrecuperer ny valeur ao anatinle cle

for valeur in dictionnaire.values():
    print(valeur)
    
# afaka atao iany koa ny manao ennumeration

for cl,val in dictionnaire.items():
    print("{} : {}".format(cl,val))
    
# on peut faire un affectation d'un dictionnaire

dico = dictionnaire
    
#afaka manao copie iany koa ny dictionnaire

dico = dictionnaire.copy() # on a maintenant deux dictionnaire indepandente dans notre programme

print("pour le variable dictionnaire : ",dictionnaire)
print("pour le variable dico : ",dico)

dico["slama"] = "Salama Tompoko oh!"

print("pour le variable dictionnaire : ",dictionnaire)
print("pour le variable dico : ",dico)

#afaka atao iany koa ny mamorona dictionnaire amin'ny alalan'ny fonction nommée

def functionDico(**parametre):
    print(parametre)

functionDico( p="anarako", a="Taonako")

print(functionDico)