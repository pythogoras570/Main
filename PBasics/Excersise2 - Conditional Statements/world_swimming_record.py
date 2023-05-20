from math import floor

record = float(input())
distance = float(input())
time_1_m = float(input())

time_total = distance * time_1_m
slowing_down = floor(distance / 15) * 12.5

time_total_slowed = time_total + slowing_down

if time_total_slowed < record:
    print(f"Yes, he succeeded! The new world record is {time_total_slowed:.02f} seconds.")
else:
    print(f"No, he failed! He was {(time_total_slowed - record):.02f} seconds slower.")
