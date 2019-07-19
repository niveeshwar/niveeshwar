#N
S11,S22=map(int,input().split())
C1=list(map(int,input().split()))
for j in range (0,S22):
    C1=[C1[-1]]+C1[:-1]
print(*C1,end='')
