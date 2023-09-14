expression = input()

stack = []

for index in range(len(expression)):
    if expression[index] == '(':
        stack.append(expression[index])
    elif expression[index] == ')':
        start_index = stack.pop()
        print(expression[start_index:index+1])