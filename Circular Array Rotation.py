n,k,q = map(int, input().split())
l = list(map(int,input().split()))
temparray = []
rem = k%n
#print(r)
temp = n-rem
#print(temp)
for k in range(0,q):
    i = int(input())
    if temp+i>=n:
        temparray.append(l[(temp+i)-n])
    else:
        temparray.append(l[temp+i])
for s in temparray:
    print(s)