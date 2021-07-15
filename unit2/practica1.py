import sys



# def alternatingSums(input):
print("Starting program...")
##FIRST WAY##
def  alternatingSums(par1):
    Team1 = []
    Team2 = []
    for i in  range (0, len(par1)):
        if (i%2 != 0):
            Team1.append(par1[i])
        elif(i%2 == 0):
            Team2.append(par1[i])

    suma1 = sum(Team1)
    suma2 = sum(Team2)
    result = [suma2, suma1]  
    return result

##SECOND WAY USING LIST COMP##
def alternatingSums2(input):
    return [sum([input[iterador] for iterador in range (0, len(input)) if iterador%2!=0]), sum([input[iterador] for iterador in range (0, len(input)) if iterador%2 ==0])]
    
if __name__ == "__main__":
    a = [50,60,60,45,70]
    output = alternatingSums(a) 
    print(output)
    ##PRINT OF LIST COMP METHOD##
    print(alternatingSums2([50,60,60,45,70]))
    
    