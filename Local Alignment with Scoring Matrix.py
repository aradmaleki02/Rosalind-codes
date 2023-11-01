PAM250 = '''   A  C  D  E  F  G  H  I  K  L  M  N  P  Q  R  S  T  V  W  Y
            A  2 -2  0  0 -3  1 -1 -1 -1 -2 -1  0  1  0 -2  1  1  0 -6 -3
            C -2 12 -5 -5 -4 -3 -3 -2 -5 -6 -5 -4 -3 -5 -4  0 -2 -2 -8  0
            D  0 -5  4  3 -6  1  1 -2  0 -4 -3  2 -1  2 -1  0  0 -2 -7 -4
            E  0 -5  3  4 -5  0  1 -2  0 -3 -2  1 -1  2 -1  0  0 -2 -7 -4
            F -3 -4 -6 -5  9 -5 -2  1 -5  2  0 -3 -5 -5 -4 -3 -3 -1  0  7
            G  1 -3  1  0 -5  5 -2 -3 -2 -4 -3  0  0 -1 -3  1  0 -1 -7 -5
            H -1 -3  1  1 -2 -2  6 -2  0 -2 -2  2  0  3  2 -1 -1 -2 -3  0
            I -1 -2 -2 -2  1 -3 -2  5 -2  2  2 -2 -2 -2 -2 -1  0  4 -5 -1
            K -1 -5  0  0 -5 -2  0 -2  5 -3  0  1 -1  1  3  0  0 -2 -3 -4
            L -2 -6 -4 -3  2 -4 -2  2 -3  6  4 -3 -3 -2 -3 -3 -2  2 -2 -1
            M -1 -5 -3 -2  0 -3 -2  2  0  4  6 -2 -2 -1  0 -2 -1  2 -4 -2
            N  0 -4  2  1 -3  0  2 -2  1 -3 -2  2  0  1  0  1  0 -2 -4 -2
            P  1 -3 -1 -1 -5  0  0 -2 -1 -3 -2  0  6  0  0  1  0 -1 -6 -5
            Q  0 -5  2  2 -5 -1  3 -2  1 -2 -1  1  0  4  1 -1 -1 -2 -5 -4
            R -2 -4 -1 -1 -4 -3  2 -2  3 -3  0  0  0  1  6  0 -1 -2  2 -4
            S  1  0  0  0 -3  1 -1 -1  0 -3 -2  1  1 -1  0  2  1 -1 -2 -3
            T  1 -2  0  0 -3  0 -1  0  0 -2 -1  0  0 -1 -1  1  3  0 -5 -3
            V  0 -2 -2 -2 -1 -1 -2  4 -2  2  2 -2 -1 -2 -2 -1  0  4 -6 -2
            W -6 -8 -7 -7  0 -7 -3 -5 -3 -2 -4 -4 -6 -5  2 -2 -5 -6 17  0
            Y -3  0 -4 -4  7 -5  0 -1 -4 -1 -2 -2 -5 -4 -4 -3 -3 -2  0 10'''

scoring_matrix = {}
for i, line in enumerate(PAM250.splitlines()):
    line = line.strip()
    if i == 0:
        keys = line.split()
    else:
        values = line.split()
        scoring_matrix[values[0]] = {keys[j]: int(values[j + 1]) for j in range(len(keys))}

input()
string1 = ""
string2 = ""
while True:
    s = input()
    if s[0] == '>':
        break
    string1 += s
while True:
    s = input()
    if not s:
        break
    string2 += s

n = len(string1)
m = len(string2)
distance = [[0 for i in range(n + 1)] for j in range(m + 1)]
backtrack = [['zero' for i in range(n + 1)] for j in range(m + 1)]

for i in range(1, m + 1):
    for j in range(1, n + 1):
        distance[i][j] = max(distance[i - 1][j] - 5, distance[i][j - 1] - 5, distance[i - 1][j - 1] + scoring_matrix[string2[i - 1]][string1[j - 1]], 0)
        if distance[i][j] == distance[i - 1][j] - 5:
            backtrack[i][j] = 'up'
        elif distance[i][j] == distance[i][j - 1] - 5:
            backtrack[i][j] = 'left'
        elif distance[i][j] == distance[i - 1][j - 1] + scoring_matrix[string2[i - 1]][string1[j - 1]]:
            backtrack[i][j] = 'diag'
        else:
            backtrack[i][j] = 'zero'

max_score = 0
for i in range(0, m + 1):
    for j in range(0, n + 1):
        # We might want to exclude i = 0 and j = 0 as we want the strings to be non-empty (doesn't matter in Rosalind)
        if distance[i][j] > max_score:
            max_score = distance[i][j]
            max_i = i
            max_j = j


align1 = ""
align2 = ""
while backtrack[max_i][max_j] != 'zero':
    if backtrack[max_i][max_j] == 'up':
        align1 += '-'
        align2 += string2[max_i - 1]
        max_i -= 1
    elif backtrack[max_i][max_j] == 'left':
        align1 += string1[max_j - 1]
        align2 += '-'
        max_j -= 1
    else:
        align1 += string1[max_j - 1]
        align2 += string2[max_i - 1]
        max_i -= 1
        max_j -= 1

print(max_score)
print(align1[::-1].replace('-', ''))
print(align2[::-1].replace('-', ''))
