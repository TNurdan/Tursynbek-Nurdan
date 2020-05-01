N = int(input())
M = dict()

for i in range(N):
    a = input().split()
    M[a[0]] = a[1]
    M[a[1]] = a[0]

print(M[input()])
