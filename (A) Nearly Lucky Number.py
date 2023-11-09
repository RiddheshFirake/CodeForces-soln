n=int(input())
res = [int(x) for x in str(n)]
count=0
for i in res:
    if i==4 or i==7:
        count+=1
if count==4 or count==7:
    print("YES")
else:
    print("NO")