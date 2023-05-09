import random
dice = []


total = 0

number_of_dic = int(input("how many dice?: "))

for die in range(number_of_dic):
    dice.append(random.randint(1, 6))


print(dice)