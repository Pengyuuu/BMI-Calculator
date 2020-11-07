# @authors: Eric Truong, Erina Lara
# BMI calculator
# November 6, 2020

# converts a person's height to meters, given feet and inches
def height_to_meters(height):
    INCH_PER_FEET = 12
    CM_PER_INCH = 2.54
    M_PER_CM = 0.01
    totalInches = (height[0]*INCH_PER_FEET) + height[1]
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
    print("Main menu: \n1. Calculate BMI \n2. Log Weight \n3. Quit")

# main
def main():

    choice = 0
    while (choice != 3):
        printMenu()

        if choice == 1:
            height = getUserHeight()
            weight = getUserWeight()
            meters = height_to_meters(height)
            kilograms = pounds_to_kg(weight)
            bmi = calculate_bmi(kilograms, meters)
            print("Your BMI is: ", bmi)

        elif choice == 2:
            pass

    print("Goodbye!")





