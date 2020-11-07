# @authors: Eric Truong, Erina Lara
# BMI calculator
# November 6, 2020

# converts a person's height to meters, given feet and inches
def height_to_meters(ft,inches):
    INCH_PER_FEET = 12
    CM_PER_INCH = 2.54
    M_PER_CM = 0.01
    totalInches = (ft*INCH_PER_FEET) + inches
    totalcm = totalInches * CM_PER_INCH
    totalm = totalcm * M_PER_CM
    return totalm


# converts a persons weight in pounds to kilograms
def pounds_to_kg(lbs):
    KG_PER_POUND = 0.453
    totalkg = lbs * KG_PER_POUND
    return totalkg

# calculates bmi using kg and meters
def calculate_bmi(kg, meters):
    return kg / (meters**2)

# gets user's height
def getUserHeight():
    height = [0,0]
    height[0] = input("Enter feet: ")
    height[1] = input("Enter inches: ")
    return height

# gets user's weight
def getUserWeight():
    weight = input("Enter weight in pounds")
    return weight

# prints menu
def printMenu():






def main():
    choice = 0
    while (choice != 3):




