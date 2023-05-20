stay = int(input())
room = input()
review = input()

single = 18
apartment = 25
papartment = 35
discount = 0
cost = 0

if room == 'apartment':
    if stay < 10:
        apartment *= 0.70
    elif 10 < stay < 15:
        apartment *= 0.65
    elif stay > 15:
        apartment *= 0.50
    cost = apartment * (stay - 1)
elif room == 'president apartment':
    if stay < 10:
        papartment *= 0.90
    elif 10 < stay < 15:
        papartment *= 0.85
    elif stay > 15:
        papartment *= 0.80
    cost = papartment * (stay - 1)
else:
    cost = single * (stay - 1)

if review == 'positive':
    discount = 1.25
elif review == 'negative':
    discount = 0.90


total = cost * discount

print(f'{total:.2f}')
