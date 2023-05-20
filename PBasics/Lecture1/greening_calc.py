price_per_sq_m = float(7.61)
sq_m = float(input())

total_price = price_per_sq_m * sq_m
discount = 0.18 * total_price
final_price = total_price - discount

print(f"The final price is: {final_price} lv.")
print(f"The discount is: {discount} lv.")