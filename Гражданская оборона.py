n = int(input())
nlist = list(map(int, input().split()))
m = int(input())
mlist = list(map(int, input().split()))
c = []
c1 = []
for i in range(n):
    camp = (nlist[i], i + 1)
    c.append(camp)
    c.sort()
    c1 = c.copy()
b = []
for j in range(m):
    bomb = (mlist[j], j + 1)
    b.append(bomb)
b.sort()
for k in range(n):
    g = 0
    h = m // 2
    f = m
    a = c[k][1] - 1
    x = 10 ** 10
    if c[k][0] < b[0][0]:
        c1[a] = b[0][1]
    elif c[k][0] > b[m - 1][0]:
        c1[a] = b[m - 1][1]
    else:
        while g < f and h != 0 and h != m - 1:
            if b[h - 1][0] <= c[k][0] <= b[h][0]:
                break
            elif c[k][0] > b[h][0]:
                g = h + 1
            else:
                f = h - 1
            z = h
            h = ((g + f) // 2)
        if g < f:
            if abs(b[h - 1][0] - c[k][0]) > abs(b[h][0] - c[k][0]):
                c1[a] = b[h][1]
            else:
                c1[a] = b[h - 1][1]
        elif c[k][0] < b[0][0]:
            c1[a] = b[0][1]
        elif c[k][0] > b[m - 1][0]:
            c1[a] = b[m - 1][1]
        else:
            c1[a] = b[z + 1][1]
print(*c1)
