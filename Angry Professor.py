n = int(input())
i = 0
c = 0
ans = []
while i!=n:
    a,b = map(int,input().split())
    l = list(map(int,input().split()))
    for j in l:
        if j<=0:
            c+=1
    if c>=b:
        ans.append('NO')
    else:
        ans.append("YES")
    for k in range(0,len(l)):
        l.pop()
    c = 0
    i+=1
for d in ans:
    print(d)