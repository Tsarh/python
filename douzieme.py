"""
    functions tres utils pour l'heritage :
    
        isinstance(<objet>, <classe>) : verifie qu'un objet est de la classe renseignée
        
        issubclass(<classe_fille>, <classe_màre>) : vérifie qu'une classe est fille d'une autre
"""


class Vehicul:
    def __init__ (self,nom_vehicul,qualite_essence):
        self.nom = nom_vehicul
        self.qualite = qualite_essence
    
    def se_deplace(self):
        print("le vehicul {} se deplace...".format(self.nom))

class Voiture(Vehicul):
    def __init__ (self,nom,essence,puissance):
        Vehicul.__init__(self,nom,essence)
        self.puissance = puissance
        
class Avion(Vehicul):
    def __init__(self, nom, qualite,puissance):
        Vehicul.__init__(self,nom, qualite)
        self.puissance = puissance

voiture1 = Vehicul("Toyota",120)
print(voiture1.nom,", ",voiture1.qualite)

voiture2 = Voiture("Mazda",125,1000)
voiture2.se_deplace()
print(voiture2.puissance)

av1 = Avion("Aire Madagascar",800,5000)
av1.se_deplace()
print(av1.puissance)

print(isinstance(voiture1,Vehicul)) # doit retourner true
print(issubclass(Voiture,Vehicul)) # doit retourner true
print(issubclass(Avion,Voiture))  # doit retourner false