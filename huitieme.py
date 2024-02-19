#coding:utf-8

#on va maintenant apprendre à gerer une erreur

"""
try: 
    instruction(s)
except:
    instruction(s)
"""

"""age = input("entrer votre age : ")

try:
    age = int(age)  # si l'utilisateur ne fait pas de betise
    print("vous etes {} ans".format(age))
     
except:
    print(" {} n'est pas un entier".format(age)) """   # si l'utilisateur fait de betise
    

# mampiasa else indray eto nefa mitovy ianyny zavatra avoakany
"""ages = input("quel age avez votre petite amie : ")

try:
    ages = int(ages)

except:
    print("{} n'est un entier !".format(ages))

else:
    print("votre petite amie a {} ans".format(ages))"""
    

# ampiasa an'ilay finally indray izao izay midika hoe excecutena foana ninoninona zavatra mitranga ny ao amin'ilay instruction finally

"""taona = input("firy taona ianao : ")

try:
    taona = int(taona)
except:
    print("{} dia tsy tarehimarika".format(taona))
else:
    print("{} taona ianao ".format(taona))
finally:
    print("VOTRE PROGRAMME EST FINI...")"""
    
#---------- EXERCICE KELY ARY EH ------------------------
nombre1 = 45

nombre2 = input("entrer un nombre à diviser : ")

"""
try:
    nombre2 = int(nombre2)
except:
     print("{} ne peut pas un diviseur ".format(nombre2))
else :
    if nombre2 == 0 : print("impossible de diviser un nombre avec {}".format(nombre2))
    else :print("resultat = {}".format(nombre1 / nombre2))
finally:
    print("PROGRAMME TERMINER...")
    
"""

#  ou bien 

try :
    nombre2 = int(nombre2)
    print("resultat = {}".format(nombre1 / nombre2))  # !!! tsaratsara kokoa raha tonga de apetraka eto ilay zavatra ho traitena
except ZeroDivisionError :
    print("on ne peut pas diviser un nombre par zero")
except ValueError :
    print("on ne peut pas diviser un nombre par des caractaires")
else :
    print("c'est un nombre exacte , bravo :)")
finally :
    print("PROGRAMME TERMINER...")
    
# ampiasa an'ilay resaka insertion indray izao

try :
    age = input("entrer votre age : ")
    age= int(age) 
    
    assert age < 18    # fampiasana an'ilay assert!!!
except AssertionError: 
    print("age est superieur a 18")  #mamoaka erreur satria maherin'ny 18
except : 
    print("erreur introuvable ninanemaniny")
else :
    print("age est inferieur a 18")  #ny inferieur à 18 iany no raisina fa rehefa tsy izay dia mamoaka erreur
    
m = input("entrer le nom de votre future petite amie : ")

try:
    assert m == "Mirana"
except AssertionError:
    print("ce n'est pas son nom vous etes tromper oupss")
except :
    print("erreur introuvable")
else : 
    print("c'est bien elle ma future epouse")
finally :
    print("MERCI POUR VOTRE PARTICIPATION...")