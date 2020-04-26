n = int(input())
N = list(map(int, input().split(maxsplit=n)))
N.sort()
print(*N)
