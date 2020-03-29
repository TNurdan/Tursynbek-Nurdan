a=input()
n=0
for i in range(0,len(a)):
    if a[i]=="f":
        n+=1
        if n==2:
            print(i)        
if n==1:
        print('-1')
elif "f" not in a:
    print('-2')