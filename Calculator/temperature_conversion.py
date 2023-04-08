unit = input("Is this celsius or fahrenheit (C/F) : " )
temp = float(input("Enter the temperature : "))

if unit == "C" :
    temp = round((9 * temp) / 5  + 32, 3)
    print(f"temperature is {temp} Fahrenheit ")


elif unit == "F":
     temp = round((temp -32) * 5 / 9 , 2)
     print(f"temperature is {temp} celsius ")

else:
   print("invalid unit of temperature")