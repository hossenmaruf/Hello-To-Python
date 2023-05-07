# concession stand program

menu = {"pizza": 2.00,
        "popcorn": 4.8,
        "chips": 2.8,
        "soda": 2.4}

cart = []
total = 0

print("------ MENU _____")


for key, value in menu.items():
    print(f"{key:10} : ${value:.2f}")

print("------ ")

while True:
    food = input("SELECT your item(q to quit): ").lower()
    if food == "q" :
        break
    elif menu.get(food) is not None:
        cart.append(food)

print("------YOUR ORDER IS ----- ")

for food in cart:
    total += menu.get(food)
    print(food, end=" ")

print()
print(f"Total is: ${total:.2f}")
