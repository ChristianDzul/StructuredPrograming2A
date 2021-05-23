##Start##

print ("Welcome to the market factory")

##Defining variables##
bank_account = 1500
product = 0
price = 0


##Now it goes the process##
product = input("Insert the name of the product\n") 
price = int( input("What is the cost of the product?\n"))
product = price

if (product <= bank_account):
    print("the purchase has been completed successfully")
    
else:    
     print("the order has been rejected")

##End##    