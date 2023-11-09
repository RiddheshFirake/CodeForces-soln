s=str(input())
up=0
low=0
for t in s:
    if t.isupper()==True:
        up+=1
    elif t.islower()==True:
        low+=1
if up>low:
    a=s.upper()
    print(a)
else:
    b=s.lower()
    print(b)