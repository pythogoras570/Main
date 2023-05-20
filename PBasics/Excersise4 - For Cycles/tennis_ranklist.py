
n = int(input())
starting_points = int(input())

points = 0
wins = 0

for i in range(n):
    place = input()
    if place == 'W':
        wins += 1
        points += 2000
    elif place == 'F':
        points += 1200
    elif place == 'SF':
        points += 720

starting_points += points

print(f'Final points: {starting_points}')
print(f'Average points: {points // n}')
print(f'{wins / n * 100 :.2f}%')
