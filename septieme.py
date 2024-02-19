#coding:utf-8

# on va parler maitenant de la modularité en python
# mais d'abord focalisons nous sur la fonction lambda 
# une fonction lambda consiste à executer une et une seule instruction dans une fonctio c-à-d qu'il n'y a qu'une seule ligne de code à exectuter 

#le hoe "lambda" dia midika fa tsy manana nom ilay fonction

# fonction tsy misy parametre aloha izy eto
salama = lambda:print("salama eh")

# rehefa iantso anazy anle fonction lambda dia tsy maintsy affectena ao anatina variable iray aloha ilay fonction lambda
salama();

# fonction ampiana parametre amin'izay ary aloha eh 
# tsy mila parenthese ny parametre fonction lambda rehefa ampiana parametre 
addition = lambda a,b: a+b;
print(addition(8,2))


# eto isika vo tena hihiditra amle resaka module na ko hoe bibliotheque amin'ny langage python
import math

racine = math.sqrt(25)
racine = int(racine)

puissance = math.pow(5,2)
puissance = int(puissance)

print(racine)
print(puissance)

# mba hialana anle anoratra math isaky ny mihetsika dia nampiana ity sintaxe ity

from math import *
racine1 = sqrt(9);
racine1 = int(racine1)

print(racine1) 

#ampiasa module izay namboariko zah fa mila fantatra ko aloha hoe ny module dia fichier ah !!!!

import mesModules.module

mesModules.module.dire_salama("Tsaroana","salama daholo ianareo ao eeeeeeh!");
mesModules.module.dire_salama();

from mesModules.module import *

dire_salama("Jazz","keza keza eh")

# afaka renommena ihany koa ilay anarana lava be eo amle chemain

import mesModules.module as modls

modls.dire_salama()