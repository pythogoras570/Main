lenght = int(input())
width = int(input())
height = int(input())
percent = float(input())

capacity = lenght * width * height
l_capacity = capacity * 0.001
water_needed = l_capacity * (1 - (percent / 100))

print(water_needed)
