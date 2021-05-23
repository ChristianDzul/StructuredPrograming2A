##Start programm##
print ("Welcome to the number machine")
##defining variables##

num = 0
prime_num= 0
result = 0 

##stablish conditions##

def prime_num (num):
     if num <= 1:
          return False
     elif num == 2:
          return True
     else:
          for i in range (2, num): #i es una varianble que puede tomar cualquier numero, y range establece un rango que ese numero puede tomar)
               if num % i == 0:  ##esta funcion de modulo "%" te da como el resultado el residuo de la division de dos numero, ejemplo 7%2 = 1 ya que 2 cabe 3 veces en 7 y te queda un 1 el cual es residuo y por tanto el resultado de modulo entre dichos numero#
                   return False    
          return True

##process usign the conditions that were stablished before##
     
num = int( input ("Please, insert any number to verify that is prime or not\n"))
result = prime_num (num)  ##igualado a la variable donde se cumplen las funciones##

if result == True:
     print ("the number is prime")
else:
     print ("the number is not prime")
