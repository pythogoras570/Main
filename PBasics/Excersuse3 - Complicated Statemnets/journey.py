budget = float(input())
season = input()

cost = 0
destination = ''
accomodation = ''

if budget <= 100:
    destination = 'Bulgaria'
    if season == 'summer':
        cost = 0.3
        accomodation = 'Camp'
    elif season == 'winter':
        cost = 0.7
        accomodation = 'Hotel'
elif 100 < budget <= 1000:
    destination = 'Balkans'
    if season == 'summer':
        cost = 0.4
        accomodation = 'Camp'
    elif season == 'winter':
        cost = 0.8
        accomodation = 'Hotel'
elif budget > 1000:
    destination = 'Europe'
    cost = 0.9
    accomodation = 'Hotel'

total_cost = budget * cost

if destination == 'Bulgaria' or 'Balkans' or 'Europe':
    print(f'Somewhere in {destination}')
    print(f'{accomodation} - {total_cost:.2f}')
