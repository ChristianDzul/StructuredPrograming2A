import sys


lista = ["red", "black", "white", "gray", "green"] ##or lista = list() el cual es el constructor
   
#List Comprehension, que se creara una lista de un numero hasta llegar el 100
lista2 = [i for i in range(1,101) if i%2==0] ## if es la condicion y la pega en i y solo alojara los valores que cumplan dicha condicion
print(lista2)

#lista compuesta
listaEvenOdd = [i for i in range(1,101) if i%2==0],[i for i in range(1,101) if i%2!=0] ##listas con numeros pares e impares, una por una
print(listaEvenOdd)

if __name__ == "__main__":

    print(f' programName: { sys.argv[0]}\n')
    print(lista, len(lista)) #Size of a list, lo que indica el numero de elementos guardadas en la lista o su tamaño
    #Manual-Print each element of the list
    # print(lista[0]) 
    # print(lista[1])
    # print(lista[2])
    ##...
    ##...
    ##...

    ##Automatic way
    index = 0  ##iterador
    while(index < len(lista)): ##o tambien puedo ingresar el valor fijo
        print(f'index:{index}, value: {lista[index]}') ## para imprimir el valor del index y el dato que se encuentra en esa posicion
        index = index + 1 ## para imprimir cada valor de la lista y le agreags 1 para que pegue al siguiente
    print("------------------")

    ##Other way to do it
    for index in range(0, len(lista)):
        print(f'index:{index}, value: {lista[index]}')