p=int(input())
temp=p
rev=0
while(p>0):
  digit=p%10
  rev=rev*10+digit
  p=p//10
if(temp==rev):
  print("yes")
else:
  print("no")
