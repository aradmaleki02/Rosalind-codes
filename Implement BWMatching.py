# Getting number of occurrences of each pattern in the Genome given BWT(Genome)

text = input()
patterns = input().split()
first_column = sorted(text)
last_to_first = []
is_matched = [False] * len(text)
for i in range(len(text)):
    for j in range(len(text)):
        if text[i] == first_column[j] and not is_matched[j]:
            last_to_first.append(j)
            is_matched[j] = True
            break


def count_occurrences(pattern, first_column, last_column, last_to_first):
    top = 0
    bottom = len(last_column) - 1
    while top <= bottom:
        if pattern:
            symbol = pattern[-1]
            pattern = pattern[:-1]
            if symbol in last_column[top:bottom + 1]:
                top_index = top + last_column[top:bottom + 1].index(symbol)
                bottom_index = bottom - last_column[top:bottom + 1][::-1].index(symbol)
                top = last_to_first[top_index]
                bottom = last_to_first[bottom_index]
            else:
                return 0
        else:
            return bottom - top + 1


for pattern in patterns:
    print(count_occurrences(pattern, first_column, text, last_to_first), end=' ')