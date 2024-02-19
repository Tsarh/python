#coding:utf-8

#on va parler les methodes en python

# class Humain :
    
#     lieu_habitation = "Terre"
    
#     def __init__(self,nom,age):
#         self.nom = nom
#         self.age = age
    
#     # def parler(self,message):  #ito izany no antsohina hoe methode satria fonction ao anaty classe
#     #     print("{} a dit : {}".format(self.nom,message))
    
#     parler = lambda self,message : print("{} a dit : {}".format(self.nom,message)) #self = methode standard
    
#     def changer_planete(cls,nouvelle_planete) : #cls = methode de classe
#         Humain.lieu_habitation = nouvelle_planete
    
#     changer_planete = classmethod(changer_planete)
    
#     def definition() : # pas besoin de la mot clé self ou cls
#         print("je suis une methode independant de la classe Humain")
    
#     difinition = staticmethod(definition)

# print("lancement du programme...")

# h1 = Humain("Tsaroana",19)
# print("{} un jeune homme de {} ans".format(h1.nom,h1.age))
# h1.parler("salama eh") #fomba fanaovana appel anle fonction ao amin'ilay classe humain (methode)

# print("habiter à planete {}".format(Humain.lieu_habitation))
# Humain.changer_planete("Mars")
# print("j'ai changé de planete et maitenant je suis au planete {}".format(Humain.lieu_habitation))

# Humain.definition()

class Mofo :
    vita = "Malagasy"
    tia = "Tsaroana"
    def __init__(self,anarana,tsirony) :
        self.anarana = anarana
        self.tsirony = tsirony
    
    def anarana_tanana(self,tanana) :
        print("ny {} dia avy tao {}".format(self.anarana,tanana))
    
    def mpakafia(cls) :
        print("i {} dia tia Mofo vita malagasy".format(Mofo.tia))
    
    mpakafia = classmethod(mpakafia)
    
    def firenena(F_anarana) :
        print("vita teto {}".format(F_anarana))
    
    firenena = staticmethod(firenena)

print("manomboka ny programa...")
m1 = Mofo("Mofogasy","Mamy")
print("{} dia manana tsiro {} izay vita {}".format(m1.anarana,m1.tsirony,Mofo.vita))
m1.anarana_tanana("Antananarivo")

Mofo.tia = "Fandresena"
Mofo.mpakafia()

Mofo.firenena("Madagasikara")