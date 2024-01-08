def numb_func():
    numbers_list =[]
    for number in numbers:
        numbers_list.append(round(float(number)))
    return numbers_list


numbers = input().split()

print(numb_func())