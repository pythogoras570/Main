n = int(input())
word = input()
all_strings = []
strings_containing_words = []

for _ in range(n):
    current_string = input()
    all_strings.append(current_string)

    if word in current_string:
        strings_containing_words.append(current_string)

print(all_strings)
print(strings_containing_words)
