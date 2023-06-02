def calculate(type, qty):
    total = 0
    if type == 'coffee':
        total = qty * 1.50
    elif type == 'coke':
        total = qty * 1.40
    elif type == 'water':
        total = qty * 1.00
    elif type == 'snacks':
        total = qty * 2.00
    return total

type = input()
qty = int(input())
print(f'{calculate(type, qty):.2f}')