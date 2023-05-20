budget = float(input())
gpu = int(input())
cpu = int(input())
ram = int(input())

gpu_price = gpu * 250
cpu_price = cpu * (gpu_price * 0.35)
ram_price = ram * (gpu_price * 0.1)

price_total = gpu_price + cpu_price + ram_price

if cpu < gpu:
    price_total *= 0.85

if budget >= price_total:
    diff = budget - price_total
    print(f"You have {diff:.02f} leva left!")

elif budget < price_total:
    diff = abs(budget - price_total)
    print(f"Not enough money! You need {diff:.02f} leva more!")