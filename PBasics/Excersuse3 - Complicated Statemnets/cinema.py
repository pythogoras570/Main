movie_type = input()
r = int(input())
c = int(input())

pro = 12.00
nor = 7.50
dis = 5.00
profit = 0

if movie_type == 'Premiere':
    profit = (r * c) * pro
elif movie_type == 'Normal':
    profit = (r * c) * nor
elif movie_type == 'Discount':
    profit = (r * c) * dis

print(f'{profit:.2f}')