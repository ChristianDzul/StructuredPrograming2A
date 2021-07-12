import sys
import random as rd ##There is a function in random called randint



myList = list()
otherlist =[] ##otherList[10] = {}; 
myInt=3

def isAnyUpper (str):
        for element in str:
                if element.isupper():
                        return True
        return False

if __name__ =="__main__":
    print("DataStructures!")
    print(type(myList)) ##te arroja el tipo de valor guardad en la varibale
    print(type(otherlist))
    print(type(myInt))
    myList.append ("Data1") ##agrega datos a mylist
    myList.append ("Data2")
    myList.append ("Data3")
    myList.append ("Data4")
    myList.append ("Data5")


    for index in range(0, len(myList)):
            print(f'Mylist[{index}]:',myList[index],",Current Index:", index) ##asi asignas lo que se guarda en index y no un elemnto en particular

    for iteracion in range(0, 11):
            otherlist.append(rd.randint(0,100))
    print(otherlist)

    myList.extend(otherlist)
    print(myList)

   # myList.pop() ##elimina datos en la lista  y libera memoria
    myList.reverse() #da la vuelta a la lista
    print(myList)

    newlist =myList[0::5] ##slicing, solo selecciono lo que quiero clonar, donde 0 es el inicio y el 5 es el final, y el dos indica saltos de 2 en 2, si eliminas el dato medio ya no abrá limite [0::2]
    print(newlist)

    usersAdmin =["Luis","Rafa","Jose","Fernando","Ricardo"]
    print(usersAdmin)
    print(usersAdmin[0].lower()) ##te cambia el valor del index 0 a minuscula, en este caso luis esta en 0
    
   ## usersAdmin[0] = usersAdmin[0].lower() ##agregas el valor modifica a la lista

    for usuario in usersAdmin:                   ## para imprimir each name con su tipo, en este caso string
            print(usuario, type(usuario))


    for element in range(0,len(usersAdmin)): ##longitud que dure x variable
            if (isAnyUpper(usersAdmin[element])):
                print(f'usersAdmin[{element}] modificated')
                usersAdmin[element] = usersAdmin[element].lower()  ##modifica usersadmin por elemento y lo convierte en lower al momento de igualar. Recordar que element contiene los datos previos asignados con "range"
                

    print(usersAdmin) ##aqui nos muestra el resultado

         


    sensor = "$GPGGA,134658.00,5106.9792,N,11402.3003,W,2,09,1.0,1048.47,M,16.27,M,08,AAAA*60"
        
        ###Slicing
    strVariable = "ThisIsAnApple"
    newString  =  strVariable[::-1]
    print(   f'strVariable[{1}]: {strVariable[1]}' )
    print(   f'newString: {newString}' )
        ##OTRA COSA##
    listaSensor =   sensor.split(   ","  )
    hr = listaSensor[1][:2]
    min =  listaSensor[1][2:4]
    sec = listaSensor[1][4:6]
     # print(f'hr: {hr}, min: {min}, sec: {sec}')
    listaSensor[1] = f'hr: {hr}, min: {min}, sec: {sec}'
    print(listaSensor)
    
    sensorFixed  = ",".join(listaSensor)
    print(sensorFixed)



    
    
