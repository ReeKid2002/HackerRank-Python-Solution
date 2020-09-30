n = input()
l = list(map(int,input().split()))
maxx = int(l[0])
minn = int(l[0])
m = 0
o = 0
for i in l:
    if maxx>i:
        maxx=i
        m+=1
    if minn<i:
        minn=i
        o+=1
print(o,m)