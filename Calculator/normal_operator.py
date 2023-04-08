operator = input ("input your operator: ")

num1 = float(input("input the num1: "))
num2 = float(input("input the num2: "))

if operator == "+":

  result = num1 + num2
  print(round(result, 1))

elif operator == "-":
 result = num1 - num2

 print(round(result, 1))

elif operator == "*":

   result = num1 * num2
   print(round(result, 3))

elif operator == "/":
       result = num1/num2
       print(round(result, 3))

else:
    print(f"{operator} is invalid")



