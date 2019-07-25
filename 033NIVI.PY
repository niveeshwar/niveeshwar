#N
n11=input()
f=0
for x in range(0,len(n11)-1):
  for j in range(x+1,len(n11)):
    if n11[x]<n11[j]:
      f=1
      print(n11[j:])
      break
  if f==1:
    break
  else:
      print(n11)
