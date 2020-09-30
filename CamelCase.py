s = str(input())
u = 0
for i in range(0,len(s)):
    if(s[i]>='A' and s[i]<='Z'):
        u+=1
print(u+1)