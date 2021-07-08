import sys

##Variables##
my_int = 0
my_str = ""
my_float = 0.0
my_bool = True ##False
my_list = [] ##list ()


if __name__ == "__main__":

        ##First way to put variables##
       
        # my_int = int(sys.argv[1] )
        # my_str = str (sys.argv[2] )
        # my_float = sys.argv[3]
        # my_bool = sys.argv[4] ##False
        # my_list = sys.argv ##List ()ç

#-----------Second way to define variables but using sys.argv but u will put it manually------##
        my_int = int(sys.argv[1] )
        my_str = str (sys.argv[2] )
        my_float = sys.argv[3]
        my_bool = sys.argv[4] ##False
        my_list = sys.argv ##List ()

        print(my_int, my_str, my_float, my_bool, my_list) ##here i can do process like sum, multiply and so on.
        ##print(my_int * 2, my_str*2 , my_float, my_bool, my_list)
        ##print(sys.argv) manda a llamr argv de la biblioteca sys en donde se guarda cada dato que se ingresa