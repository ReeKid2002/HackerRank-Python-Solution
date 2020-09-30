a = int(input())
l = list(map(int,input().split()))
b = int(input())
c = 0
sum = 0
while c!=b:
    u,v = input().split()
    for i in l:
        if i==int(u):
            sum+=int(v)
            print(sum)
            l.remove(i)
            break
    u = 0
    v = 0
    c+=1
print(sum)
