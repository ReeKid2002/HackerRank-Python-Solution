n = int(input())
l = list(map(int,input().split()))
c = 0
le = len(l)
while le!=0:
        print(len(l))
        l.sort()
        a = l[0]
        #print(a)
        le = len(l)
        #print(l)
        for k in range(0,le):
            if l[k] == a:
                c+=1
        l.reverse()
        for i in range(0,c):
            l.pop()
        le = len(l)
        c = 0