budget = float(input())
extras = int(input())
costumes_cost_person = float(input())

decor = budget * 0.1
total_costumes = extras * costumes_cost_person

if extras > 150:
    total_costumes *= 0.9

if budget >= (decor + total_costumes):
    diff = budget - (decor + total_costumes)
    print(f"Action!")
    print(f"Wingard starts filming with {diff:.2f} leva left.")
else:
    diff = abs(budget - (decor + total_costumes))
    print(f"Not enough money!")
    print(f"Wingard needs {diff:.2f} leva more.")
