al = list(map(int,input().split()))
bo = list(map(int,input().split()))
sa = 0
sb = 0
for i in range(0,3):
    if al[i]>bo[i]:
        sa+=1
    elif al[i]<bo[i]:
        sb+=1
    else:
        sa+=0
        sb+=0
print(sa,sb,sep=" ")