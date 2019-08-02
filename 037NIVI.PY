
n123 = int(input())
L = [ int(x) for x in input().split()]
n1 = len(L)
if n123==1 :
    print(1)
   
cnt = 0
for i in range(1,n123-1) :
    if ((L[i] > L[i-1]) and (L[i] > L[i+1])) or ((L[i] < L[i-1]) and (L[i] < L[i+1])):
        cnt += 1
print(cnt)
