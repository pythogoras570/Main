budget = int(input())
season = input()
fisherman_count = int(input())

rent = 0

if season == 'Spring':
    rent = 3000
elif season == 'Summer' or season == 'Autumn':
    rent = 4200
elif season == 'Winter':
    rent = 2600

if 6 >= fisherman_count:
    rent *= 0.90
elif 7 <= fisherman_count <= 11:
    rent *= 0.85
elif 12 < fisherman_count:
    rent *= 0.75

if fisherman_count % 2 == 0 and season != 'Autumn':
    rent *= 0.95

remaining = abs(rent - budget)

if budget < rent:
    print(f"Not enough money! You need {remaining:.2f} leva.")
else:
    print(f"Yes! You have {remaining:.2f} leva left.")
