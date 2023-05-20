
n = int(input())
price_wash = float(input())
price_toy = int(input())

odd = 0
even = 0
money = 0
money_multi = 10

for i in range(1, n + 1, 2):
    odd += 1
for i in range(2, n + 1, 2):
    even += 1
    money += money_multi
    money_multi += 10

price_toy *= odd
money += price_toy
money -= even

if price_wash < money:
    print(f'Yes! {abs(price_wash - money):.2f}')
else:
    print(f'No! {abs(price_wash - money):.2f}')
    