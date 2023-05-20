
# input
fav_book = input()
cur_book = input()

check = 0
is_found = False

# logic
while cur_book != 'No More Books':
    if cur_book == fav_book:
        is_found = True
        print(f'You checked {check} books and found it.')
        break

    check += 1
    cur_book = input()

if not is_found:
    print("The book you search is not here!")
    print(f"You checked {check} books.")
