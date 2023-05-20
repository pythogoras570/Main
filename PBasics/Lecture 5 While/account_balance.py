
balance = 0
# logic
while True:
    user_input = input()
    if user_input == 'NoMoreMoney':
        break
    user_input = float(user_input)
    if user_input < 0:
        print('Invalid operation!')
        break
    balance += user_input
    print(f'Increase: {user_input:.2f}')
# output
print(f'Total: {balance:.2f}')
