import sys

def listElementsSum(input):
    add = 0
    for i in range (0, len(input[0])): ##filas
        #print(f" i:{i},{edificio[i]}")
        for j in range(0,len(input)):
           # print(f"edificio[{j}][{i}]: {edificio[j][i]}")
            if (input[j][i] == 0):
                break
            add += input[j][i]
             
    return add


if __name__ == "__main__":
    print("Practica 2_CodeBlocks")
    edificio = [ [0,1,1,2], ##edificio[0]
                [0,5,0,0], ##edificio[1][1] , elemento de la fila 1, columna 1 que sera 5
                [2,0,3,3]]
    # print(listElementsSum(edificio))

    print(listElementsSum(edificio))





    # for i in range (0, len(edificio[0])): ##de cero a lo largo de la lista edificio
    #    #print(f" i:{i},{edificio[i]}") ##imprime el index y la lista que se encuentra en dicho index
    #     ##FOR ANIDADO##
    #     # for j in range (0, 3):
    #     #     print("j:",j,",i:",i)
    #     for j in range(0,len(edificio)):
    #         print(f"edificio[{j}][{i}]: {edificio[j][i]} "   ) ##acceder el elemento de un array rectangular, [i] fila [j] columna
