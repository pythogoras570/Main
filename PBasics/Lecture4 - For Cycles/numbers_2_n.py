n = int(input())
result = 1

for i in range(0, n + 1):
    if i != 0:
        result = result * 2
    if i % 2 == 0:
        print(result)