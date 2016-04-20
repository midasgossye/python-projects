#ISA calculator
#Midas Gossye (c) 2016
import math as mt
h_m = 0
again = 1
T_strato = 216.650
p_strato = 22632.1
Rho_strato = 0.363918
while again == 1:
    print "ISA calculator (c) 2016 Midas Gossye"
    print " "
    print "What do you want to do?"
    print " "
    print "\t 1) Enter an altitude in meters"
    print "\t 2) Enter an altitude in feet"
    print "\t 3) Enter an altitude in FL (Flight Level)"
    print "\t 4) Calculate an altitude in meters"
    print "\t 5) Calculate an altitude in feet"
    print "\t 6) Calculate an altitude in FL (Flight Level)"

    print " "
    choice = int(raw_input("Your choice: "))
    if choice == 1:
        h_m = float(raw_input("Geopotential altitude h in meters= "))

    elif choice == 2:
        h_ft = float(raw_input("Geopotential alt. h in feet= "))
        h_m = h_ft * 0.3048

    elif choice == 3:
        h_ft = float(raw_input("Geopotential alt. h in FL (Flight Level)= "))*100
        h_m = h_ft * 0.3048

    elif (choice > 3) & (choice < 7):
        p_pa = float(raw_input("Pressure in Pa at unknown altitude= "))


    else:
        print "Invalid selection, sorry"
        quit()

    if (h_m < 11000) & (choice < 4):

        T = 288.15 - 0.0065*h_m
        p = 101325 * ((T/288.15)**(-9.80665/(-0.0065*287)))
        Rho = 1.225*((T/288.15)**((-9.80665/(-0.0065*287))-1))

    elif (h_m < 20000) & (choice < 4):
        T = T_strato
        p = p_strato*mt.exp((-9.80665/(287*T))*(h_m-11000))
        Rho = Rho_strato*mt.exp((-9.81/(287*T))*(h_m-11000))

    elif p_pa > p_strato:

        h_m = ((288.15*((p_pa/101325)**(-((-0.0065*287)/9.80665))))-288.15)/(-0.0065)
        h_ft = h_m * 3.2808399
        h_FL = int(round(h_ft/100))

    elif p_pa > 5475:

        h_m = (mt.log(p_pa/p_strato) * ((-287*T_strato)/9.80665)) + 11000
        h_ft = h_m * 3.2808399
        h_FL = int(round(h_ft/100))

    else:
        print "Not able to calculate this high, sorry..."
        quit()

    print " "
    print "=============DATA============="

    if choice < 4:
        print "T= ", T,"K"
        print "p= ", p,"Pa"
        print "Rho= ", Rho,"kg/m^3"

    elif choice == 4:
        print "Altitude in meters h= ",h_m,"m"

    elif choice == 5:
        print "Altitude in feet h=",h_ft,"ft"

    elif choice == 6:
        print "Altitude in FL: FL",h_FL
    print "=============================="
    print " "
    dummy=raw_input("Press enter to quit or 1 to restart: ")
    if dummy == '1':
        again = 1
        print "=============================="
        print " "
    else:
        again = 0

    
