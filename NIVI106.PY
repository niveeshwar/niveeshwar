#N
n11,k22=map(int,input().split())
intg=input().split()
a=[]
for i in intg:
  if (int(i)%2!=0):
    a.append(i)
print(a[k22-1])
