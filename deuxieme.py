#coding:utf-8

"""
   on va parler des variables en python
   fonction tene miasa amin'ny variable str.format() , type() , printf() , input()
"""

# pour un entier
var_entier = 4

# pour le type float ou nombre flottant
var_float = 645.54

#pour les chaines de caractaire
var_string = "salama eh 882"

#pour le boolean
var_boolean = True

print(var_string,"\n")

#manolo anle %d ao amin'ny langage C

texte = "nom : {} , age : {}"

print(texte.format("Tsaroana",19)) #ou bien
print("salama {} ah efa amin'ny {} zao raha ande amin'izay eh ".format("Fandresena",5))

#solona scanf any anaty langage C indray

nom = input("entrer votre nom : ");  
print("mon nom c'est ",nom)

# on peut aussi faire caster les variable comme : float() , int() , bool() , str()

age = input("entrer votrer age : ") #raha nombre no retour anle input dia par defaut izy de type string fa mila castena raha te ahazo nombre entier na flottant
age = int(age)
print("je suis {} ans".format(age))