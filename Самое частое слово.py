d = {}

N = open("input.txt")
word = N.read().split()

for i in word:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

M = 0
i = ''
for key, value in d.items():
    if value > M:
        M = value
        i = key
    elif value == M:
        if key < i:
            i = key

print(i)
