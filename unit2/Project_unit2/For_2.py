import sys

lista=[]
lista2=[]
lista3=[]
lista4=[]

def Sucession (lista):
    for number in range(2,6):
        lista.append(number)
    for number2 in range(3,7):
        lista2.append(number2)
    for number3 in range(4,8):
        lista3.append(number3)
    for number4 in range(5,9):
        lista4.append(number4)
    
    lista.extend(lista2+lista3+lista4)
    print(lista)

if __name__ == "__main__":
    print("Starting Program!!!")
    print("Finding sucession...")
    print("The result is:")
    Sucession(lista)