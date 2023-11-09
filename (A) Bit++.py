a=int(input())
count=0
for i in range(a):
    s=input()
    if s=="X++":
        count+=1
    if s=="++X":
        count+=1
    if s=="--X":
        count-=1
    if s=="X--":
        count-=1
print(count)