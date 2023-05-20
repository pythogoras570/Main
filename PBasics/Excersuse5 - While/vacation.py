
trip_cost = float(input())
current_amount = float(input())

days = 0
days_spending = 0

while True:
    action = input()
    daily_amount = float(input())
    days += 1

    if action == 'spend':
        current_amount -= daily_amount
        if current_amount < 0:
            current_amount = 0
        days_spending += 1
        if days_spending == 5:
            print(f"You can't save the money.")
            print(f'{days}')
            break

    if action == 'save':
        current_amount += daily_amount
        days_spending = 0
        if trip_cost <= current_amount:
            print(f'You saved the money for {days} days.')
            break
