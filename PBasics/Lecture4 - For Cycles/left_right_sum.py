
n = int(input())
left = 0
right = 0

for i in range(n):
    user_input = int(input())
    left += user_input

for i in range(n):
    user_input = int(input())
    right += user_input

if left == right:
    print(f'Yes, sum = {left}')
else:
    diff = abs(left - right)
    print(f'No, diff = {diff}')