nylon = 1.5
paint = 14.5
thinner = 5

nylon_need = int(input())
paint_need = int(input())
thinner_need = int(input())
hours = int(input())

total_materials = (nylon * (nylon_need +2) + paint * (paint_need + (paint_need * 0.1)) + (thinner * thinner_need) + 0.40)
total_work = total_materials * 0.3
total = total_materials + total_work * hours
print(total)