
n = int(input())

people_total = 0
g1 = 0
g2 = 0
g3 = 0
g4 = 0
g5 = 0

for i in range(n):
    people = int(input())
    people_total += people
    if 0 < people <= 5:
        g1 += people
    elif people <= 12:
        g2 += people
    elif people <= 25:
        g3 += people
    elif people <= 40:
        g4 += people
    else:
        g5 += people


total = g1 + g2 + g3 + g4 + g5

p1 = g1 / total * 100
p2 = g2 / total * 100
p3 = g3 / total * 100
p4 = g4 / total * 100
p5 = g5 / total * 100


print(f'{p1:.2f}%')
print(f'{p2:.2f}%')
print(f'{p3:.2f}%')
print(f'{p4:.2f}%')
print(f'{p5:.2f}%')
