w=int(input())
num=w//2
flag=0
num1=num-1
num2=num+1
num3=num-2
num4=num+2
if w == 2:
    print("NO")
    flag=1
if num+num==w and num%2==0:
    print("YES")
    flag=1
if (num1+num2)==w and num1%2==0 and num2%2==0 and flag == 0:
    print("YES")
    flag=1
if (num3+num4)==w and num3%2==0 and num4%2==0 and flag == 0:
    print("YES")
elif flag==0:
    print("NO")