def IsPointInCircle (x, y, xc, yc, r):
    centerX = xc - xc
    centerY = yc - yc
    pointX = x - xc
    pointY = y - yc
    return -r <= x <= r and -r <= y <= r

x = float(input())
y = float(input())
xc = float(input())
yc = float(input())
r = float(input())


if IsPointInCircle(x, y, xc, yc, r):
    print("YES")
else:
    print("NO")
