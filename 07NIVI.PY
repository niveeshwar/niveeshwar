farrari23=int(input())
car=0
for i in range(0,farrari23):
  if(pow(2,i)>farrari23):
    break
  car=farrari23-pow(2,i)
print(car)
