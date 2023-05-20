pen_packs_price = float(5.80)
marker_packs_price = float(7.20)
detergent_liters_price = float(1.20)
pen_packs = int(input())
marker_packs = int(input())
detergent_liters = int(input())
discount = int(input())/100

total_amount = ((pen_packs * pen_packs_price) + (marker_packs * marker_packs_price) + (detergent_liters * detergent_liters_price))
discounted_amount = total_amount * discount
total_discounted = total_amount - discounted_amount

print(total_discounted)