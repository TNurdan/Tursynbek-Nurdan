a=input()
n=0
for i in range(0,len(a)):
    if a[i]=="f":
     print(i)
     if n>=2:
         print(i,i)
else:
 print()
