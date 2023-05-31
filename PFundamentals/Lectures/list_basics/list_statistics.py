n_lines = int(input())
positive_list = []
negative_list = []

for numbers in range(n_lines):
    new_number = int(input())
    if new_number >= 0:
        positive_list.append(new_number)
    else:
        negative_list.append(new_number)

print(f'{positive_list} \n {negative_list}')
print(f"Count of positives: {len(positive_list)}")
print(f"Sum of negatives: {sum(negative_list)}")
