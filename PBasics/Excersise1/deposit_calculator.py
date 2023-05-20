
deposit_amount = float(input())
deposit_time = int(input())
yearly_interest = float(input())
total_amount = deposit_amount + (deposit_time * ((deposit_amount * yearly_interest/100) / 12))

print(f"Total at the end of the year {total_amount}")