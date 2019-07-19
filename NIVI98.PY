#N
s22=int(input())
d=list(map(int,input().split()))
for i in range(s22-1):
    if(d[i]>d[i+1]):
        print(i)
