#coding: utf-8
"""
(!) on ne peut pas modifier les valeur d'un tuple
    on va maintenant parler de la tuple
        pour declarer un tuple en puthon il faut ecrire le syntaxe suivant :
            ma_tuple = () "ça c'est pour un tuple vide"
            ma_tuple = 17, "pour ça c'est pour une seule valeur dans un tuple"
            ma_tuple = (17,) "pour ça c'est pour une seule valeur dans un tuple"
            ma_tuple = (17,12,52) "pour ça c'est pour plusieur valeurs dans un tuple"
"""

ma_tuple = ("Tsaroana",19) #ny tuple dia valeur tsy afaka ovaina intsony izany ho ohatry ny liste en constant izany
print(ma_tuple[1])

# afaka anaovana affectation multiple ny tuple

(nombre1,nombre2) = (19,20)
print("nombre 1 : {}".format(nombre1))
print("nombre 2 : {}".format(nombre2))

# rehefa atao amina resaka affectation multyple ilay tuple dia afaka manao changement du valeur izany hoe

nombre1 = 52
print("nombre 1 a changé: {}".format(nombre1))

# on peut faire aussi :

def posistion_my_position():
    X = 12
    Y = 20
    
    return X,Y

coordeX = 0
coordeY = 0

print("coordoner de X et Y = ({}/{})".format(coordeX,coordeY))

coordeX,coordeY = posistion_my_position()

print("changement du tuple de la coordoner de x et y = ({}/{})".format(coordeX,coordeY))

#dans ce cas là c'est un affectation multiple alors on peut modifier la valeur de coordeX et coordeY

coordeX = 50

print("changement du tuple de la coordoner de x et y = ({}/{})".format(coordeX,coordeY))