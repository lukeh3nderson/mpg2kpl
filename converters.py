"""
Converters.py 
This is a program to convert MPG to KPL. The user is asked to enter 
a number and then the number is converted and the result output to 
the command line. 

"""
# Declaring known constants 

KPM = 1.609344    # Kilometers per mile

GPL = .2641720524 # Gallons per liter 

def mpg2kpl(mpg):
    """
    Converts mpg to kpl via the formula:
    KPL = MPG * KPM * KPL 

    """
    return mpg * KPM * GPL


# ask the user to input an mpg value 
mpg = input("What is the MPG")
# convert the imput into a numeric value
mpg = float(mpg)
print(round(mpg2kpl(mpg), 2), "kpl")
