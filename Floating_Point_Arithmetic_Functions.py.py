#Write a program that takes in how many miles a person has driven. Then call a function that calculates (and returns) how many kilometers they drove. (Hint: 1 mile = 1.60934 kilometers)

def calculations (driver_miles):
    #calculations
    #1 mile = 1.60934 kilometers
    kil_driver_miles = (driver_miles * 1.60934)
    return kil_driver_miles

def main ():
    driver_miles = float(input("How many miles have you driven? "))
    total_kil = calculations(driver_miles)
    print (f"You have driven {total_kil} kilometers") 

#call the main fucntion to start program
main ()
