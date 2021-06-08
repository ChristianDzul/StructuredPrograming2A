import sys


lista = ["red", "black", "white", "gray", "green"]

#List Comprehension
lista2 = [i for i in range(1,101) if i%2==0]

listaEvenOdd = [i for i in range(1,101) if i%2==0],[i for i in range(1,101) if i%2!=0]

print(listaEvenOdd)

if __name__ == "__main__":

    print(f' programName: { sys.argv[0]}\n')
    print(lista, len(lista)) #Size of a list
    #Manual
    # print(lista[0])cd 
    # print(lista[1])
    # print(lista[2])
    ##...
    ##...
    ##...
    index = 0
    while(index < 4):
        print(f'index:{index}, value: {lista[index]}')
        index = index + 1
    print("--------")

    for index in range(0, len(lista)):
        print(f'index:{index}, value: {lista[index]}')