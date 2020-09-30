n = int(input())
d = []
l = []
k = []
for i in range(0,n):
    key , value = input().split()
    d.append(str(key))
    d.append(str(value))
for i in range(0,n):
    k[i] = str(input())
    if k[i]==d[i]:
        reply = str(d[i]+"="+d[i+1])
        l.append(reply)
    else:
        l.append("Not Found")
for j in l:
    print(j)
