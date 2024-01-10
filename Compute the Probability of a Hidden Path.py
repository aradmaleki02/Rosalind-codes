path = input()

input()
input()
input()

states = input().split()
n = len(states)

transition = dict()
for i in range(n):
    transition[states[i]] = dict()
    transitions = input().split()
    for j in range(n):
        transition[transitions[0]][states[j]] = float(transitions[j + 1])

ans = 1.0 / n
current = path[0]
for i in range(1, len(path)):
    ans *= transition[current][path[i]]
    current = path[i]
print(ans)