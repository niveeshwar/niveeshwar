l1=int(input())
k23=[]
for i in range(0,l1):
   k23.append(input())
l2=len(k23[0])
s=""
for i in range(0,l2):
   c=k23[0][i]
   f=0
   for j in range(0,l1):
        if(c!=k23[j][i]):
           f=1
   if(f==0):
     s=s+c
   else:
     break
print(s)
