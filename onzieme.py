#coding: utf-8

# on va parler maintenant de la propriete izany hoe raha tian tsy ho kitikitiana ilay attribut ao anatinle objet dia mila mampiasa encapsulation
# tsy atao manana accée ao amle variable amin'ny objet izany ilay olona 

class Humain:
    def __init__(self,nom,age):
        self.nom = nom;
        self._age = age;
    
    def _getage(self):
        return self._age
    
    def _setage(self,nouvelage):
        if nouvelage < 0:
            self._age = 0
        else:
            self._age = nouvelage

    age = property(_getage,_setage)

h1 = Humain("Tsaroana",19)

print(h1.age)
h1.age = -15
print(h1.age)