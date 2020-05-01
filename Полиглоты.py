N = int(input())
n = dict()

for i in range(0, N):
    m = int(input())
    for j in range(0, m):
        l = input()
        if l in n:
            n[l] = n[l] + 1
        else:
            n[l] = 0

lan = list()
for l in n:
    if n[l] == N - 1:
        lan.append(l)

print(len(lan))
for l in lan:
    print(l)

print(len(n))
for i in n:
    print(i)
