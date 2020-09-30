s = str(input())
t = str(input())
k = int(input())
sl = []
tl = []
co = 0
pos = 0
cou = 0
for i in s:
    sl.append(i)
for j in t:
    tl.append(j)
if len(sl) >= len(tl):
    for a in range(0,len(tl)):
        if sl[a] == tl[a]:
            co+=1
        else:
            pos = a
            break
else:
    for a in range(0,len(s)):
        if sl[a] == tl[a]:
            co+=1
        else:
            pos = a
            break
if k>=(len(sl)+len(tl)):
    print("Yes")
elif len(sl)==len(tl) and co==len(sl):
    print("Yes")
elif len(sl)<len(tl):
    print("No")
elif k>=((len(sl)-co)+(len(tl)-co)) and len(tl)%2==0 and k%2==0:
    print("Yes")
elif k>=((len(sl)-co)+(len(tl)-co)) and len(tl)%2!=0 and k%2!=0:
    print("Yes")
else:
    print("No")
