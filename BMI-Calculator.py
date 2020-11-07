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

def pounds_to_kg(lbs):

    KG_PER_POUND = 0.453
    totalkg = lbs * KG_PER_POUND

    return totalkg



