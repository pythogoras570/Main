number_of_pages = int(input())
pages_per_h = int(input())
number_of_days = int(input())

hours_per_day = int(number_of_pages / pages_per_h) / number_of_days

print(hours_per_day)