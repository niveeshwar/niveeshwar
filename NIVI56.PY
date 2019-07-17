#N
q1=input()
count1=0
for j1 in q1:
  if (j1.isdigit() or j1.isalpha()):
    count1+=1
if count1!=0:
  print("Yes")
else:
  print("No")
