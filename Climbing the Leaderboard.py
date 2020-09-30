n = int(input())
score = list(map(int,input().split()))
m = int(input())
alice = list(map(int,input().split()))
score = list(dict.fromkeys(score))
dub = len(score)
score.sort()
#print(score)

rank = []
co = 0
pos = 0
for i in range(0,len(alice)):
        score.append(alice[i])
        score.sort()
        #print(score)
        for j in range(0,len(score)):
            if alice[i]==score[j]:
                co+=1
                pos = j
        if co>1:
            rank.append(dub-pos+1)
        else:
            rank.append(dub-pos+1)
        score.remove(alice[i])
for q in rank:
    print(q)
