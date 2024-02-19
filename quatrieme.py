"""
   les operateurs de comparaisons : == , === , != , !== , <= , >= , < , > , and , or , in ou not in
"""

mdp = "12345"
userName = "Tsaroana"

nom_utilisateur = input("entrer votre nom d'utilisateur : ")
mot_de_passe = input("entrer votre mot de passe : ")

if mdp!=mot_de_passe:
    print("mot de passe incorrecte")
else : print("mot de passe validé")

lettre = "a"

if lettre in "aeiyuo" : 
    print("c'est une voyelle");
    
age = 25 
if age == 18 :
    print("vous etes majeur")
elif age < 18 :
    print("vous etes mineur")
elif 20 <= age <= 25 :
    print("vous etes un adulte")
else :
    print("vous etes vielle")
    
"""
    age >=20 and age<=25  -->   20 <= age <= 25
""" 