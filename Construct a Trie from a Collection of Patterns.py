patterns = []
while True:
    s = input().strip()
    if not s:
        break
    patterns.append(s)

edges = [[]]
for pattern in patterns:
    current_node = 0
    for symbol in pattern:
        current_node_edges = [edge[0] for edge in edges[current_node]]
        if symbol in current_node_edges:
            current_node = edges[current_node][current_node_edges.index(symbol)][1]
        else:
            edges.append([])
            edges[current_node].append([symbol, len(edges) - 1])
            current_node = len(edges) - 1

with open('output_Construct a Trie from a Collection of Patterns.txt', 'w') as f:
    for i in range(len(edges)):
        for edge in edges[i]:
            f.write(str(i) + '->' + str(edge[1]) + ':' + edge[0] + '\n')