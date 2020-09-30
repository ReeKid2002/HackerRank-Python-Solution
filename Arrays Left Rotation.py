n , s= map(int,input().split())
a = list(map(int,input().split()))
j = int(s%n)
print(j)
i = 0
while i!=j:
    for j in range(0,n-1):
        temp = int(a[j])
        a[j] = a[j+1]
        a[j+1] = temp
    i+=1
for k in range(0,n):
    print(a[k],end=" ")