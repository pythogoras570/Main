ftype = input()
fqty = int(input())
budget = int(input())

price = 0
discount = 0
left = 0

if ftype == "Roses":
    price = 5
    if fqty > 80:
        discount += 0.1
elif ftype == "Dahlias":
    price = 3.80
    if fqty > 90:
        discount += 0.15
elif ftype == "Tulips":
    price = 2.80
    if fqty > 80:
        discount += 0.15
elif ftype == "Narcissus":
    price = 3
    if fqty < 120:
        discount -= 0.15
elif ftype == "Gladiolus":
    price = 2.50
    if fqty < 80:
        discount -= 0.2

total_price = price * fqty * (1 - discount)
left = abs(total_price - budget)

if budget < total_price:
    print(f"Not enough money, you need {left:.2f} leva more.")
else:
    print(f"Hey, you have a great garden with {fqty} {ftype} and {left:.2f} leva left.")
