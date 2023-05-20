import sys

biggest = int(input())

while True:
    num = input()
    if num == 'Stop':
        break
    num = int(num)
    if biggest < num:
        biggest = num

print(biggest)
