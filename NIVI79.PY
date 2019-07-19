#N
z1,z2=map(int,input().split())
p13=z1*z2
for i in range(0,p13+1):
 if(i**2==0):
  print("yes")
  break
else:
  print("no")
