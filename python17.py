n22=int(input())
sum=0
t=n22
while t>0:
  digit=t%10
  sum+=digit**3
  t//=10
if n22==sum:
  print("yes")
else:
  print("no")
