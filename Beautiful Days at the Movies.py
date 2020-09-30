def reversenum(y):
    su = 0
    i = 0
    t = int(y)
    while t!=0:
        i+=1
        t//=10
    while y!=0:
        rem = int(y%10)
        su = int((10**(i-1))*rem + su)
        i-=1
        y/=10
    return su
a, b, c =map(int,input().split())
cou = 0
temp = 0
for i in range(a,b+1):
    temp = int(i-reversenum(i))
    if (temp/c).is_integer():
        cou+=1
    temp =0
print(cou)