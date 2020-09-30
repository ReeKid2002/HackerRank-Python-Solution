t = int(input())
a = []
b = []
n = 1
m = 0
sum = 0
for i in range(0,t):
    a = list(map(int,input().split()))
    n = a[0]//a[1]
    m = n
    sum+=n
    while(m>=a[2]):
        sum+=1
        m-=a[2]
        m+=1
    a.pop()
    a.pop()
    a.pop()
    b.append(sum)
    sum = 0
for j in b:
    print(j)
