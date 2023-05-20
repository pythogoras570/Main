trip_price = float(input())
puzzle_qty = int(input())
doll_qty = int(input())
teddy_qty = int(input())
minion_qty = int(input())
truck_qty = int(input())

total_price = (puzzle_qty * 2.60) + (doll_qty * 3) + (teddy_qty * 4.10) + (minion_qty * 8.20) + (truck_qty * 2)
total_qty = puzzle_qty + doll_qty + teddy_qty + minion_qty + truck_qty

if total_qty >= 50:
    total_price *= 0.75

total_price *= 0.9

if total_price >= trip_price:
    remaining = total_price - trip_price
    print(f"Yes! {remaining:.2f} lv left.")
else:
    remaining = abs(total_price - trip_price)
    print(f"Not enough money! {remaining:.2f} lv needed.")