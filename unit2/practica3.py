import sys

###Practica###

def palin (string):
    string2=string.lower()
    string3=string2.replace(" ","")
    newstring=string3[::-1]
    if newstring==string3:
       return True
    else:
       return False

if __name__ == "__main__":
    a="Anita lava la tina"


    if palin(a)==True:
        print(a, "es palindrome")
    else:
       print(a, "no es palindrome") 