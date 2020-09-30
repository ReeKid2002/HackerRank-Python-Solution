n = int(input())
l = []
temp = []
c = 0
temp = []
for i in range(0,n):
    s = ""
    ch = input()
    for j in ch:
        l.append(j)
        temp.append(j)
    # temp.sort()
    # temp = list(dict.fromkeys(temp))
    # t1 = len(temp)
    l.reverse()
    for k in range(0,1):
        if l[k]>l[k+1]:
            t = l[k]
            l[k] = l[k+1]
            l[k+1] = t
            c+=1
            break
    # print(c)
    if c==0:
        l.reverse()
        a = l[0]
        # print(a)
        # print(temp)
        co = 0
        for q in range(0,len(l)):
            if ord(l[q])!=ord(temp[q]):
                co+=1
        if co==0:
            print("No Change")
        for q in range(0,len(l)):
            l.pop()
            temp.pop()
        else:
            #print(a)
            l.sort()
            for j in range(0,len(l)-1):
                if l[j]==a:
                    t = l[j+1]
                    l[j+1] = l[0]
                    l[0] = t
            #print(l)
            for j in range(1,len(l)):
                for k in range(1,len(l)-1):
                    if ord(l[k])>ord(l[k+1]):
                        t = l[k]
                        l[k] = l[k+1]
                        l[k+1] = t
            for j in range(0,len(l)):
                s+=l[j]
            print(s)

            for j in range(0,len(l)):
                l.pop()
                temp.pop()
            # print("\n")
            # print(temp)
            # print(l)
    else:
        l.reverse()
        for m in range(0,len(l)):
            s+=l[m]
            # print(m,end="")
        print(s)
        for m in range(0,len(l)):
            l.pop()
            temp.pop()
        # print("\n")
        c = 0