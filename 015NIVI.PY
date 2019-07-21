c23=int(input())
d=list(map(int,input().split(" ")))
d=[bin(i) for i in d]
d.sort(reverse=True)
d=[int(c23,2) for c23 in d]
for i in range(0,c23):
     print(d[i])
