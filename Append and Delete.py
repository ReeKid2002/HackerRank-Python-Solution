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
#print(co)
#print(pos)
if sl==tl:
    #print("1")
    print("Yes")
elif len(tl)<len(sl) and len(tl)==co:
    #print("2")
    for b in range(0,len(sl)-co):
        cou+=1
        sl.pop()
    if cou<=k:
        print("Yes")
    else:
        print("No")
elif len(sl)<len(tl) and len(sl)==co:
    pos = len(sl)
    #print("3")
    for w in range(pos,len(t)):
        cou+=1
        sl.append(tl[w])
    #print(sl)
    if cou<=k:
        print("Yes")
    else:
        print("No")
elif co == 0 and pos ==0:
    if k>=len(tl):
        print("Yes")
    else:
        print("No")
else:
    #print("4")
    for b in range(0,len(sl)-co):
        cou+=1
        sl.pop()
    #print(sl)
    for c in range(pos,len(t)):
        cou+=1
        sl.append(tl[c])
    #print(cou)
    if cou==k:
        print("Yes")
    else:
        print("No")