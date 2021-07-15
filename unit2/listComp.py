import sys


if __name__ =="__main__":
    print("List Comprehension...")
    ##FORMA DE LLENAR UNA LISTA## primera forma
    lista = []
    for iterador in range(1,101):
        if iterador%2 == 0:   ##una condicion donde solo se impriman de 0 a 101 pero que sean solo multiplos de 2
            lista.append(iterador) ##append añade los datos crado por la list comp a la variable de lista
    print(lista)

    ##List Comp hecho de otra forma##

    listComp = [iterador for iterador in range (1, 100) if iterador %2 == 0] ##i for i in range (x,y)
    print(listComp)