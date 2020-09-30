a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = list(map(int,input().split()))
m = []
n = []
lb = len(b)
lc = len(c)
num = lb+lc
co = 0
for i in range(0,lb):
    for k in range(b[lb-1],c[0]+1):
        if k%b[i]==0:
            m.append(k)
for j in range(0,lc):
    for k in range(b[lb-1],c[0]+1):
        if c[j]%k==0:
            m.append(k)
print(m)
for l in m:
    co = m.count(l)
    if co==num:
        n.append(l)
    co = 0
print(n)
print(len(n)//num)