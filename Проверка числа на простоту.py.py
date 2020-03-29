def IsPrime(n):
    import math
    origin = math.sqrt(n)
    if n == 3:
        return "YES"
    elif n == 5:
        return "YES"
    elif n == 7:
        return "YES"
    elif n % 2 == 0:
        return "NO"
    elif n % 3 == 0:
        return "NO"
    elif n % 5 == 0:
        return "NO"
    elif n % 7 == 0:
        return "NO"
    elif n % origin == 0:
        return "NO"
    else :
        return "YES"
    
N = int(input())        
func = IsPrime (N)
print (func)
