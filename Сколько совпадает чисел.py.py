a = int(input())
b = int(input())
c = int(input())
if a == b == c :
    print ('3')
elif a == b != c or c == b != a or a == c != b:
    print ('2')
else :
    print('0')
