N = list(map(int, input().split()))
n = {}

for i in N:
    if i in n:
        print("YES")
    else:
        n[i] = 1
        print("NO")
