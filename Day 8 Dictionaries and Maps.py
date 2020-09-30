n = int(input())
name = []
phn = []
temp = []
flag = 0
for i in range(0,n):
    na, ph = map(str,input().split())
    name.append(na)
    phn.append(ph)
for j in range(0,n):
    nam = input()
    for k in range(0,n):
        if nam == name[k]:
            t = (name[k]+"="+phn[k])
            temp.append(t)
            break
        else:
            flag+=1
    if(flag==n):
        t = "Not found"
        temp.append(t)
for i in temp:
    print(i)