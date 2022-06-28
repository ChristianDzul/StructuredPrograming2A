from cmath import cos, pi, sin, sqrt
import string
import sys
import array 
import math

#Position Analysis
    ##Variables##
link1 = 0
link2 = 0
link3 = 0
link4 = 0
grades1 = 0
w2 = 0
Rpa = 0
d3 = 0

if __name__ == "__main__":
    print ("Initializing program...")

    link1 = int(input("Enter the value for link d: \n"))
    link2 = int(input("Enter the value for link a: \n"))
    link3 = int(input("Enter the value for link b: \n"))
    link4 = int(input("Enter the value for link c: \n"))
    grades1 = int(input("Insert the value of the angular speed: \n"))
    w2 = int(input("Insert the value of the angular velocity: \n"))
    Rpa = int(input("Insert the value of Rpa: \n"))
    d3 = int(input("Insert the value of d3: \n"))
    angle2 = (grades1*math.pi)/180
    print ("///////////////////////////////////////////")
    # ///////////
    print ("Now, let's calculate K1")
    k1 = link1/link2
    print ("K1 is:", k1)
    # ///////////
    print ("Now, let's calculate K2")
    k2 = link1/link4
    print ("K2 is:", k2)
    # ///////////
    print ("Now, let's calculate K3")
    k3 = (link2**2 -link3**2 + link4**2 + link1**2)/(2*link2*link4)
    print ("K3 is:", k3)
    # ///////////
    print ("Now, let's calculate K4")
    k4 = link1/link3
    print ("K4 is:", k4)
    # ///////////
    print ("Now, let's calculate K5")
    k5 = (link4**2 -link1**2 - link2**2 - link3**2)/(2*link2*link3)
    print ("K5 is:", k5)

    print ("///////////////////////////////////////////")
    print ("Now we must calculate the constants...")
    A = (math.cos(angle2)-k1-(k2*math.cos(angle2))+k3)
    print ("So A is:", A)
    #######################
    B = -2*math.sin(angle2)
    print ("So B is:", B)
    #######################
    C = k1-(k2+1)*math.cos(angle2) +k3
    print ("So C is:", C)
    #######################
    D = math.cos(angle2) -k1+(k4*math.cos(angle2))+k5
    print ("So D is:", D)
    #######################
    E = -2*math.sin(angle2)
    print ("So E is:", E)
    ######################
    F = k1 + (k4-1)*math.cos(angle2)+k5
    print ("So F is:", F)
    ######################

    print ("///////////////////////////////////////////")
    print ("Now we must calculate the angles for the opened configuration...")
    ang31 = 2*math.atan((-E-math.sqrt(E**2 -4*D*F))/(2*D))
    O31 = (ang31*180)/math.pi

    if O31<0 and O31>-90:
        O31 = 360+O31
        print ("So angle 031 is:", O31)
    elif O31<-90 and O31>-180:
        O31 = 360+O31
        print ("So angle 031 is:", O31)
        
    elif O31<-180 and O31>-270:
        O31 = 360+O31
        print ("So angle 031 is:", O31)
        
    elif O31<-270 and O31>-360:
        O31 = 360+O31
        print ("So angle 031 is:", O31)
    else:
        print ("So angle 031 is:", O31)

    
    ######################
    ang41 = 2*math.atan((-B-math.sqrt(B**2 -4*A*C))/(2*A))
    O41 = (ang41*180)/math.pi

    if O41<0 and O41>-90:
        O41 = 360+O41
        print ("So angle 041 is:", O41)
    elif O41<-90 and O41>-180:
        O41 = 360+O41
        print ("So angle 042 is:", O41)
        
    elif O41<-180 and O41>-270:
        O41 = 360+O41
        print ("So angle 041 is:", O41)
        
    elif O41<-270 and O41>-360:
        O41 = 360+O41
        print ("So angle 041 is:", O41)
    else:
        print ("So angle 041 is:", O41)
    # print ("So angle 041 is:", O41)
    ######################
    print ("///////////////////////////////////////////")
    print ("Now we must calculate the angles for the closed configuration...")
    ang32 = 2*math.atan((-E+math.sqrt(E**2 -4*D*F))/(2*D))
    O32 = (ang32*180)/math.pi
    
    ###################################
    if O32<0 and O32>-90:
        O32 = 360+O32
        print ("So angle 032 is:", O32)
    elif O32<-90 and O32>-180:
        O32 = 360+O32
        print ("So angle 032 is:", O32)
        
    elif O32<-180 and O32>-270:
        O32 = 360+O32
        print ("So angle 032 is:", O32)   
    elif O32<-270 and O32>-360:
        O32 = 360+O32
        print ("So angle 032 is:", O32)
    else:
        print ("So angle 032 is:", O32)    
   
    ######################
    ang42 = 2*math.atan((-B+math.sqrt(B**2 -4*A*C))/(2*A))
    O42 = ((ang42*180)/math.pi)
    
    if O42<0 and O42>-90:
        O42 = 360+O42
        print ("So angle 042 is:", O42)
    elif O42<-90 and O42>-180:
        O42 = 360+O42
        print ("So angle 042 is:", O42)
        
    elif O42<-180 and O42>-270:
        O42 = 360+O42
        print ("So angle 042 is:", O42)
        
    elif O42<-270 and O42>-360:
        O42 = 360+O42
        print ("So angle 042 is:", O42)
    else:
        print ("So angle 042 is:", O42)
    print ("///////////////////////////////////////////")
    ################Velocity Analysis#################
    ###Opened###
    #Angular velocity##
    print ("Now we must calculate the angular velocity for the opened configuration.")
    w31 = ((link2*w2)/link3)*((math.sin((O41-grades1)*math.pi/180))/((math.sin((O31-O41)*math.pi/180))))
    print ("W31 is:", w31)
    w41 = ((link2*w2)/link4)*((math.sin((grades1-O31)*math.pi/180))/((math.sin((O41-O31)*math.pi/180))))
    print ("W41 is:", w41)
    print ("///////////////////////////////////////////")
    ##Velocity of points A and B
    print ("Now we must calculate velocity in points A and B.")
    ##Other variables##
    P1 = link2*w2*(-math.sin(angle2))
    P2 = link2*w2*(math.cos(angle2))
    P3= link4*w41*(-math.sin(O41*math.pi/180))
    P4= link4*w41*(math.cos(O41*math.pi/180))
    ########################
    vA = link2*w2*(complex(-math.sin(angle2))+ complex(0,math.cos(angle2)))
    print ("vA is:", vA)
    vB = link4*w41*(complex(-math.sin(O41*math.pi/180))+ complex(0,math.cos(O41*math.pi/180)))
    print ("vB is:", vB)
    print ("///////////////////////////////////////////")
    print ("Now we must calculate magnitud of vA and vB.")
    mvA = math.sqrt ((P1)**2 +(P2)**2)
    print ("Magnitud of vA is:", mvA)
    mvB = math.sqrt ((P3)**2 +(P4)**2)
    print ("Magnitud of vB is:", mvB)

#END
