text = input()
forbidden = ['a', 'o', 'u', 'e', 'i']
text_list = [char for char in text if char.lower() not in forbidden]

print(''.join(text_list))