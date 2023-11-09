n=int(input())
s=0
i=0
while s < n:
    if (n-s)<=4:
        break
    else:
        s = 5+s
        i+=1
diff=n-s
if diff==0:
    print(i)
elif diff>0 and diff<=4:
    print(i+1)