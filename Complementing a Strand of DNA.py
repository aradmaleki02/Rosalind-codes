complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
s = input()
print(''.join([complement[c] for c in s[::-1]]))