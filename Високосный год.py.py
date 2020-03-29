A = int(input())
if A % 4 == 0 and A % 100 != 0 :
    print ('Yes')
elif A % 400 == 0 :
    print ('Yes')
elif A % 100 == 0:
    print ('NO')

