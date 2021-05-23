##Start##

print ("Welcome to the payment service")

##Defining variables##
price_hour = 240
min_hour = 40
bon = 1.5
hours_worked = 0
final_salary = 0

##Now it goes the process##

hours_worked = int( input("Enter the hours you worked during the week \n"))
 
if (hours_worked <= min_hour):
    final_salary = hours_worked * price_hour
    print("Congrats, you earned:", final_salary)
    
else:    
    hours_extra = hours_worked - min_hour
    final_salary = (price_hour * min_hour) + (hours_extra) * (price_hour * bon)
    print ("you earned:", final_salary)

##End##    