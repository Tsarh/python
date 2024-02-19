#coding:utf-8

#on va maintenant parler de l'objet

class Humain:
    
    humain_creer = 0
    
    def __init__(self,c_prenom,c_age):  #constructeur
        print('on a cree un humain')
        #declaration des variables dans une classe
        self.prenom = c_prenom
        self.age = c_age
        Humain.humain_creer += 1
        
print("on n'est pas dans la classe humain mais en bas on y est")

h1 = Humain("Tsaroana",19)  #appele d'une classe
#affichage des variables dans la programme principale
print("Nom => {} et age => {}".format(h1.prenom,h1.age))
print("humain créer est {}".format(Humain.humain_creer))

h2 = Humain("Fandresena",40)
print("ages => {} et nom => {}".format(h2.age,h2.prenom))
print("humain créer est {}".format(Humain.humain_creer))