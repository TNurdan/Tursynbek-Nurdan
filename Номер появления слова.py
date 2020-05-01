N = open("input.txt")
M = N.read().split()
V = dict()

for word in M:
    if word in V:
        V[word] = V[word] + 1
    else:
        V[word] = 0
    print(V[word])
