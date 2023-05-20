
n = int(input())
odd = 0
even = 0

for i in range(n):
    user_input = int(input())
    if i % 2 == 0:
        odd += user_input
    else:
        even += user_input

if odd == even:
    print(f'Yes')
    print(f'Sum = {odd}')
else:
    diff = abs(odd - even)
    print(f'No')
    print(f'Diff = {diff}')
