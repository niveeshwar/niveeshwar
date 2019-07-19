#N
xx1=list(input())
yy2=[]
for j in xx1:
   if j not in yy2:
      yy2.append(j)
if xx1==yy2:
   print("Yes")
else:
   print("No")
