import math

def main():

    first_odometer = float(input('Enter the first odometer reading (miles): '))
    second_odometer = float(input('Enter the second odometer reading (miles): '))
    fuel_amount = float(input('Enter the amount of fuel used (gallons):'))
    miles_per_gallon = (second_odometer - first_odometer)/fuel_amount
    lp100k = 235.215/miles_per_gallon

    print(f'{miles_per_gallon:.2f} per gallon, {lp100k:.2f} liters per 100 kilometers')

def miles_per_gallon(first_odometer,second_odometer,fuel_amount):
    mpg = abs(second_odometer - first_odometer) / fuel_amount
    return mpg

def lp100k(mpg):
    lp100k = 235.215/mpg
    return lp100k

main()