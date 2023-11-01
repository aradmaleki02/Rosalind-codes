input()
s1 = ""
while True:
    s = input()
    if s[0] == '>':
        break
    s1 += s
s2 = ""
while True:
    s = input()
    if not s:
        break
    s2 += s
n = len(s1)
m = len(s2)
d = [[0] * (m + 1) for i in range(n + 1)]
parent = [[0] * (m + 1) for i in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, m + 1):
        d[i][j] = min(d[i - 1][j] + 1, d[i][j - 1] + 1, d[i - 1][j - 1] + (s1[i - 1] != s2[j - 1]))
        if d[i][j] == d[i - 1][j] + 1:
            parent[i][j] = 'up'
        elif d[i][j] == d[i][j - 1] + 1:
            parent[i][j] = 'left'
        else:
            parent[i][j] = 'diag'

print(d[n][m])
ans1 = ""
ans2 = ""
while n > 0 or m > 0:
    if parent[n][m] == 'up':
        ans1 += s1[n - 1]
        ans2 += '-'
        n -= 1
    elif parent[n][m] == 'left':
        ans1 += '-'
        ans2 += s2[m - 1]
        m -= 1
    else:
        ans1 += s1[n - 1]
        ans2 += s2[m - 1]
        n -= 1
        m -= 1

print(ans1[::-1])
print(ans2[::-1])
