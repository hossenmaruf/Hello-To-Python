sum_odd_digit = 0
sum_even_digit = 0
total = 0

#step1

card_number = input("Enter your credit card Number: ")
card_number = card_number.replace("-", "")
card_number = card_number.replace(" ", "")
card_number = card_number[::-1]

#Step2

for x in card_number[::2]:
    sum_odd_digit += int(x)

#step3

for x in card_number[1::2]:
    x = int(x) * 2
    if x>=10:
        sum_even_digit += (1 + (x % 10))
    else:
        sum_even_digit += x

#FinalStep

total = sum_even_digit + sum_odd_digit
if total % 10 == 0:
    print("Credit card is valid")
else:
    print("your credit is invalid")



