n = int(input())
ans = []
for i in range(0,n):
    l = list(map(int,input().split()))
    if l[0]>l[2]:
        a = l[0]-l[2]
    else:
        a = l[2]-l[0]
    if l[1]>l[2]:
        b = l[1]-l[2]
    else:
        b = l[2]-l[1]
    if a>b:
        ans.append("Cat B")
    elif a<b:
        ans.append("Cat A")
    else:
        ans.append("Mouse C")
for j in ans:
    print(j)