month = input()
number_of_stays = int(input())

studio_price = 0
apartment_price = 0

if month == 'May' or month == 'October':
    studio_price = 50
    apartment_price = 65
    if 7 > number_of_stays < 14:
        studio_price *= 0.95
    elif number_of_stays > 14:
        studio_price *= 0.70
elif month == 'June' or month == 'September':
    studio_price = 75.20
    apartment_price = 68.70
    if number_of_stays > 15:
        studio_price *= 0.80
elif month == 'July' or month == 'August':
    studio_price = 76
    apartment_price = 77

if number_of_stays > 14:
    apartment_price *= 0.90

a_price = apartment_price * number_of_stays
s_price = studio_price * number_of_stays


print(f'Apartment: {a_price:.2f} lv.')
print(f'Studio: {s_price:.2f} lv.')
