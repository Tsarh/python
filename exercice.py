#coding:utf-8

a = input("entrer un nombre : ")
a = int(a);

if 1 <= a <= 10:

    def factoriel(a) :
        init = 2
        fact = 1
        while init <= a :
            fact = init * fact
            init +=1;
        return fact

    def fibonachi(b) :
        u1=1;
        init = 1;
        inn = 1
        fib = 0;
        while inn <= b :
            fib = init + inn
            init = fib
            inn += 1
        return fib


    print("le factoriel de {} est : {}".format(a,factoriel(a)))
    print("la suite de fibonachi de {} est : {}".format(a,fibonachi(a)))

else : print("valeur trop charger")