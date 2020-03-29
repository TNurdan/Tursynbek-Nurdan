def sum(a, b):
    if a and b >= 0:
        if b == 0:
            return a
        else:
            return sum(a+1, b-1)
a = int(input())
b = int(input())
print(sum(a, b))
