N = int(input())
n = set(range(1, N + 1))
m = input()

while m != "HELP":
    m = set(map(int, m.split()))
    if input() == "YES":
        n &= m
    else:
        n -= m
    m = input()

print(*sorted(n))
