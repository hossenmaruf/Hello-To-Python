foods = []
prices = []
total = 0

while True:
    food = input("Enter your food to buy (n to quit): ")
    if food.lower() == "n":
        break
    else:
        price = float(input(f"Enter the price of that food {food}: $"))
        foods.append(food)
        prices.append(price)

        print("--- YOUR CART ---")

        for food in foods:
            print(food, end=" ")

for price in prices:
         total += price

print(f"your food total price is: ${total}")