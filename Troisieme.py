#coding:utf-8

"""
      on va parler maitenant des operateurs en langage python comme : + , - , * , / , % ou biem (modulo)
"""

a = input("entrer a : ");
a = int(a);

b = input("entrer b : ");
b = int(b);

division = a / b;
division = int(division);
print("{} / {} = {}\n".format(a,b,division));

modulo = a % b;
print("{} % {} = {}\n".format(a,b,modulo));

multiplication = a * b;
print("{} * {} = {}\n".format(a,b,multiplication));

addition = a + b;
print("{} + {} = {}\n".format(a,b,addition));

soustraction = a - b;
print("{} - {} = {}\n".format(a,b,soustraction))

"""
    ----->   tsy afaka mampiasa anle incrementation ++ sy decrementation -- ihany koa
    afaka mampiasa an'ireto ihany koa ohatry ny amin'ny JS sy PHP , C ,JAVA :   += , -= , *= , /= , %=
"""