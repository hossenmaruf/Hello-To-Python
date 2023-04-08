weight = float(input("input your weight: "))
unit = input("kg or pound ? K or L :  ")

if unit == "K":
    weight = weight * 2.205
    unit = "Lbs."
    print(f" your weight is {round(weight ,2)} {unit}")

elif unit == "L":
        weight = weight / 2.205
        unit = "Kgs."
        print(f" your weight is {round(weight, 2)} {unit}")
else:
 print( "invalid unit" )
