hours = int(input())
minutes = int(input())

minutes += 15

if minutes > 59:
    minutes -= 60
    hours += 1
if hours > 23:
    hours = 0
    print(f"{hours}:{minutes:02d}")
else:
    print(f"{hours}:{minutes:02d}")
