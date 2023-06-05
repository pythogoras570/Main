def tribonacci_seq(num):
    num -= 3
    sequence = '1 1 2'
    tribonacci1 = 1
    tribonacci2 = 1
    tribonacci3 = 2
    tribonacci4 = 0
    for n in range(num):
        tribonacci4 = tribonacci1 + tribonacci2 + tribonacci3
        tribonacci1 = tribonacci2
        tribonacci2 = tribonacci3
        tribonacci3 = tribonacci4
        sequence += ' ' + str(tribonacci4)
    return sequence


number = int(input())
print(tribonacci_seq(number))