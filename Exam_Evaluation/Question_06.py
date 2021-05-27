##Start##
print ("Welcome to the area calculator")

##Variables##
length = 0
width = 0
area_square = 0
area_rectangle = 0
##Getting the values##
length = int( input("Insert a value for the lenght \n"))
width = int( input("Insert a value for the width \n"))
##Process##
if (length == width):
    area_square = length * width
    print ("The figure is a square with an area of:", area_square)
else:
    area_rectangle = length * width
    print ("The figure is a rectangle with an area of:", area_rectangle)
