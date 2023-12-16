n = int(input())
leaf = int(input())

dis = [[] for _ in range(n)]
for i in range(n):
    dis[i] = list(map(int, input().split()))

ans = float('inf')
for i in range(n):
    for j in range(n):
        if leaf in (i, j):
            continue
        ans = min(ans, 0.5 * (-dis[i][j] + dis[i][leaf] + dis[leaf][j]))

print(int(ans))