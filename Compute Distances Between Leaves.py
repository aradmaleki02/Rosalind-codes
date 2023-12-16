#floyd warshall

n_leaves = int(input())
n_nodes = n_leaves
graph = dict(dict())
while True:
    inp = input()
    if inp == "":
        break
    inp = inp.replace("->", ":")
    inp = inp.strip().split(":")
    from_node = int(inp[0])
    to_node = int(inp[1])
    weight = int(inp[2])
    n_nodes = max(n_nodes, from_node, to_node)
    if from_node not in graph.keys():
        graph[from_node] = dict()
    graph[from_node][to_node] = weight


def is_leaf(node):
    return node not in graph.keys()


dis = [[float("inf") for i in range(n_nodes + 1)] for j in range(n_nodes + 1)]
for i in range(n_nodes + 1):
    dis[i][i] = 0
for k in graph.keys():
    for i in graph[k].keys():
        dis[k][i] = graph[k][i]

for k in range(n_nodes + 1):
    for i in range(n_nodes + 1):
        for j in range(n_nodes + 1):
            dis[i][j] = min(dis[i][j], dis[i][k] + dis[k][j])

for i in range(n_leaves):
    for j in range(n_leaves):
        print(int(dis[i][j]), end=" ")
    print()