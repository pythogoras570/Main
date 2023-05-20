product = input()
day = input()
qty = float(input())
price = 0

if day in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']:
    if product == 'banana':
        price = qty * 2.50
    elif product == 'apple':
        price = qty * 1.20
    elif product == 'orange':
        price = qty * 0.85
    elif product == 'grapefruit':
        price = qty * 1.45
    elif product == 'kiwi':
        price = qty * 2.70
    elif product == 'pineapple':
        price = qty * 5.50
    elif product == 'grapes':
        price = qty * 3.85
    print(f'{price:.2f}')
elif day in ['Saturday', 'Sunday']:
    if product == 'banana':
        price = qty * 2.70
    elif product == 'apple':
        price = qty * 1.25
    elif product == 'orange':
        price = qty * 0.90
    elif product == 'grapefruit':
        price = qty * 1.60
    elif product == 'kiwi':
        price = qty * 3.00
    elif product == 'pineapple':
        price = qty * 5.60
    elif product == 'grapes':
        price = qty * 4.20
    print(f'{price:.2f}')
else:
    print('error')
