N = int(input())
n = list(map(int, input().split()))
x = int(input())
for i in range(1,len(n)):
    if i <= N:
        print(i)
    else:
        if i <= x:
            print(i)
