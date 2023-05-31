n = int(input())
even = []
odd = []
negative = []
positive = []

for _ in range(n):
    lines = int(input())
    if lines == 0:
        even.append(lines)
        positive.append(lines)
    if lines % 2 == 0:
        even.append(lines)
    if lines % 2 != 0:
        odd.append(lines)
    if lines < 0:
        negative.append(lines)
    if lines > 0:
        positive.append(lines)

command = input()

if command == "even":
    print(even)
if command == 'odd':
    print(odd)
if command == 'negative':
    print(negative)
if command == 'positive':
    print(positive)
