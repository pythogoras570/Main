import sys

n = int(input())

sum_numbers = 0
max_number = -sys.maxsize

for i in range(n):
    current_number = int(input())
    sum_numbers += current_number
    if current_number > max_number:
        max_number = current_number

sum_numbers -= max_number

if max_number == sum_numbers:
    print('Yes')
    print(f'Sum = {max_number}')
else:
    print('No')
    print(f'Diff = {abs(sum_numbers - max_number)}')

