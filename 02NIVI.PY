from itertools import combinations
s11,u=map(int,input().split())
l1=len(str(s11))
l2=list(combinations(str(s11),l1-u))
l2=sorted(l2)
print(*l2[0],sep='')
