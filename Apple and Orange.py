s,t = map(int,input().split())
a,b = map(int,input().split())
n,m = map(int,input().split())
ap = list(map(int,input().split()))
ora = list(map(int,input().split()))
no = 0
na = 0
for i in range(0,len(ap)):
    ap[i]=ap[i]+a
for j in range(0,len(ora)):
    ora[j]=ora[j]+b
for l in ap:
    if l>=s and l<=t:
        na+=1
for k in ora:
    if k >= s and k <= t:
        no+=1
print(na)
print(no)