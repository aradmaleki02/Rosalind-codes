# getting inverse burrows wheeler transform
transform = input().strip()
sorted = sorted(transform)
match = [0] * len(transform)
matched = [False] * len(transform)
for i in range(len(sorted)):
    for j in range(len(transform)):
        if sorted[i] == transform[j] and not matched[j]:
            match[i] = j
            matched[j] = True
            break

text = ''
index = 0
while len(text) < len(transform):
    text += sorted[index]
    index = match[index]

print(text[1:] + '$')