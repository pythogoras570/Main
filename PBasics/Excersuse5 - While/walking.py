
goal = 10000
steps_total = 0

while True:
    steps = input()

    if steps == 'Going home':
        steps = int(input())
        steps_total += steps
        break

    steps = int(steps)
    steps_total += steps

    if steps_total > goal:
        break

if steps_total > goal:
    print(f'Goal reached! Good job!\n{steps_total - goal} steps over the goal!')
else:
    print(f'{goal - steps_total} more steps to reach goal.')
