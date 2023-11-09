c,u=input().split()
a=int(c)
t=int(u)
while t>0:
    m=a%10
    if m!=0:
        a-=1
    else:
        a=a//10
    t-=1
print(a)