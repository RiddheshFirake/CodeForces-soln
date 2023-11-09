
n = int(input())
for i in range(n):
    s = input()
    x = len(s)
    if x > 10:
        print(f"{s[0]}{x - 2}{s[-1]}")
    else:
        print(s)