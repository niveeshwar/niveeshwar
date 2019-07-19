#N
n11,k22=map(int,input().split())
intg=list(map(int,input().split()[:k22]))
a=[]
for i in intg:
   if(i<=i+1):
     a.append(i)
print(a[k22-1]) 
