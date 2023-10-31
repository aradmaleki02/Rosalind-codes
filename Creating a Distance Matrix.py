strings = []
while True:
    s = input()
    if not s:
        break
    if s[0] == '>':
        strings.append('')
    else:
        strings[-1] += s

n = len(strings)
distance = [[0] * n for i in range(n)]
for i in range(n):
    for j in range(n):
        for k in range(len(strings[i])):
            if strings[i][k] != strings[j][k]:
                distance[i][j] += 1 / len(strings[i])

for i in range(n):
    for j in range(n):
        print(f'{distance[i][j]:.5f}', end=' ')
    print()