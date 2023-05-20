chicken = 10.35
fish = 12.40
vegan = 8.15
delivery = 2.50

chicken_menu = int(input())
fish_menu = int(input())
vegan_menu = int(input())

desert = (chicken_menu * chicken + fish_menu * fish + vegan_menu * vegan) * 0.2
total = (chicken_menu * chicken + fish_menu * fish + vegan_menu * vegan)

print(total+desert+delivery)