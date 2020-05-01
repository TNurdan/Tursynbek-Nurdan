d = {}

N = open("input.txt")
words = N.read().split()

for i in words:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

for j in sorted(d.items(), key=lambda x: (-x[1], x[0])):
    print(j[0])
