l = list(map(int,input().split()))
car = str(input())
lo = []
for i in range(0,len(car)):
    b = int(ord(car[i]))
    lo.append(l[b-97])
ma = max(lo)
print(ma*len(car))