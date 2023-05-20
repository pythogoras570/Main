from math import ceil
series_name = str(input())
series_lenght = int(input())
break_lenght = int(input())

lunch_lenght = break_lenght * 0.125
rest_lenght = break_lenght * 0.25
total_left = break_lenght - (lunch_lenght + rest_lenght)

if series_lenght <= total_left:
    remaining = total_left - series_lenght
    print(f"You have enough time to watch {series_name} and left with {ceil(remaining)  } minutes free time.")
else:
    remaining = abs(total_left - series_lenght)
    print(f"You don't have enough time to watch {series_name}, you need {ceil(remaining)} more minutes.")
