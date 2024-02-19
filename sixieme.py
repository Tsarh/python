#coding:utf-8
"""
    on va entrer maintenant la declaration et l'appel d'un fonction en langage python
"""

def dire_bonjour():
    print("salama eh :) !")

#on va appeler maintenant la fonction dire_bonjour

dire_bonjour()

#deuxieme exemple prenant un dialogue

def dialogue(nom_personne,message_personne):
    print("{} : {}".format(nom_personne,message_personne))

dialogue("Tsaroana","salama eeeeh :) ")
dialogue("Jazz","salama less inona ny kajy mande any eh")
dialogue("Tsaroana","maina be less ity fa nareo zao no tsy hita mihintsy le tsy hita hoe makaiza")
dialogue("Jazz","nga less ita fa mbola variana miady amin'ny fiainana ah")

#afaka declarena par defaut ilay parametre ao amle fonction raha ohatra ka sendra tsy tiana ampiana parametre rehefa rappel anle fonction

def parametre_par_defaut(nom="Tsaroana",age=19):
    print("mon nom c'est {} et j'ai {} ans".format(nom,age));

parametre_par_defaut();
parametre_par_defaut("Jazz",20);

#afaka atao ihany koa ny tsy definir parametre amin'ny voalohany fa mila mampiasa an'ireto syntaxeireto fotsiny

def materiel(*liste_materiel):    # ilay signe * eto dia tsy misy hifandraisany amin'ny pointeur mihintsy ah !!!!
    for liste in liste_materiel :
        print(liste)

materiel("bouclier","armure en or","soins","flèche","possion magique")
materiel("guitareaaah")

imp = input("entrer votre nom : ")

for nom in imp :
    print(nom);

# ny zavatra ita teo ambony aloha dia mitovy amin'ny procedure amin'ny pascal ihany aloha izany hoe tsy misy valeur de retour
# fa ilay zavatra ataonle fonction fotsiny no ataon'ilay programme rehefa antsohina ilay izy

#  ^-------------------------------------------------------------------------------------------------------------------------^

# hiditra amin'ny fontion misy valeur de retour amin'izay isika izao ah !!!!

def addition(a,b):
    somme = a + b;
    return somme;

print(addition(20,58))

def puissance(a,n):
    init = 2;
    puiss = a;
    while init <= n : 
        puiss = puiss * a
        init += 1
    return puiss;

print(puissance(5,8));
