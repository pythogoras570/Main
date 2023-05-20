
name = input()
points = float(input())
n = int(input())
nomination = 1250.5

for i in range(n):
    jury_name = input()
    jury_points = float(input())
    points += (len(jury_name) * jury_points) / 2

    if points > nomination:
        print(f'Congratulations, {name} got a nominee for leading role with {points:.1f}!')
        break
if points <= nomination:
    print(f'Sorry, {name} you need {nomination - points:.1f} more!')