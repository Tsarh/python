# on va parler maintenant de la liste

Maliste = ["note","eleve",15,True,"tsara"]

print(Maliste)

liste = ["Tsaroana"] * 10 # on va entrer des Chaines Tsaroana dix fois  

print(liste)

# afaka manamboatra list iray izay nombre croissant ohatra

nombreListe = range(5)  # liste entre 0 à 4 nombre
# mba angalana ny valeur rehetra aoo amin'io tableau vo noforonina io dia mampiasa  boucle while na for

# i = 0

# while i<len(nombreListe):
#     print(nombreListe[i])
#     i += 1

for valeur in nombreListe:
    print(valeur)
    
#le syntaxe necessaire pour faire une affichage qu'on veut capturer dans un tableau

print(Maliste[4:])

#on peut modifier les valeur dans un tableau comme bon nous semble

liste[2:] = ["Ny aina"] * 8
print(liste[:])

# ireo methode ilaina mba anaovana insertion ao amin'ny tableau iray

tabvide = []
print(tabvide)
tabvide.append("Jazz")
print(tabvide)

#raha efa misy valeur indray ilay tableau fa tiana antsofoana valeur ao amin'ilay valeur anle tableau

tab = ["anarana","fanampiny","taona"]
print(tab[:])
tab.insert(1, "sokajy")
print(tab[:])

# raha anao resaka supression indray dia mampiasa mot clé "del"

del tab[2]
print(tab[:])

#afaka mampiasa ny methode remove iany koa ah

tab.remove("taona")
print(tab[:])

# afaka manao trie iany koa ny famiasana ny methode sort fa tokony tsy maintsy hitovy daholo ilay type ny zavatra ao 
# anatinle tableau rehefa mampiasa an'io methode io si non mamoaka erreur

tab.sort()
print(tab[:])

#afaka atao iany koa ny manisa ny nombre ny valeur tiana ho fantatra @ alalan'ny methode count

compter = ["naruto","songoku","lufy","naruto","tanjiro"]
print(compter[:])
print("le nombre de naruto : ",compter.count("naruto"))

# afaka atao ny mampifandray ny tableau anakiroa

tab1 = ["Tsara","ny"]
tab2 = ["Tompo","Andriamanitsika","Amen!"]

print(tab1[:])
print(tab2[:])

tab1.extend(tab2)

print(tab1[:])