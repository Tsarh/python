"""
    Les chaines de caractère on va utiliser le methode " help(type_de_variable) "
    str.upper(), str.lower(), str.capitalize(), str.title(),
    str.center(<nombre_d'espace",<une_chane>), str.index(), str.find()
    str.replace(<ancienne>,<nouveau>,<occurence>)
"""

# help(str)

ch1 = "tsaroana ny aina fandresena"
print(ch1)

ch1 = ch1.upper()
print(ch1)

ch1 = ch1.title()
print(ch1)

ch1 = ch1.lower()
print(ch1)

ch1 = ch1.center(50,"-")
print(ch1)

ch2 = "Tsaroana Ny Aina Fandresena"
ma_chaine = input("entrer la chaine à rechercher : ")
print(ch2.find(ma_chaine))
try:
    ch2.index(ma_chaine)
except:
    print("je ne le trouve pas desolé...")
else:
    print("l'index de cette chaine c'est : {}".format(ch2.index(ma_chaine)))
    
chaine = "Bonne journée"
chaine = chaine.replace("journée","après midi")
print(chaine)