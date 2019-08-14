N23 = int(input())
sM = [ int(x) for x in input().split()]
N23 = len(sM)
sc = 0
for i in range(0,N23-2) :
    for j in range(i+1, N23-1):
        for k in range(j+1, N23):
            if sM[i] > sM[j] > sM[k] :
                sc += 1
print(sc)
