#N
m11,n11=map(int,input().split())
space=input()
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=[]
for i in range(len(b)):
  a.append(b[i])
  c.append(max(a))
print(*c,sep=' ')
