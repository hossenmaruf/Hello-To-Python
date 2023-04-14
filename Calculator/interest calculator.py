principle = 0
rate = 0
time = 0
total = 0

while True:
   principle = float(input("Enter the principle amount: "))

   if principle < 0:
       print("principle can not be less than zero")
   else:
       break

while True:
   rate = float(input("Enter the rate: "))

   if rate < 0:
       print("rate can not be less than zero")
   else:
       break

while True:
    time = int(input("Enter the Time: "))

    if time < 0:
        print("Time can not be less than zero")
    else:
        break

total = principle * pow((1 + rate / 100), time)

print(f"Balance after {time} year/s: ${total : .2f}")