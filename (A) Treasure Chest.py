t=int(input())
for i in range(t):
    x,y,k=input().split()
    x=int(x)
    y=int(y)
    k=int(k)
    a=0
    b=0
    if y>x and (y-x)<=k:
        print(y)
    elif y>x and (y-x)>=k:
        a=x+k
        a+=(y-a)*2
        print(a)
    elif x>y :
        print(x)
    elif x==y:
        print(x)