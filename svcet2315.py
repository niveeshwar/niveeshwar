nivesh=int(input())
if nivesh>1:
  for i in range(2,nivesh//2):
    if(nivesh%i)==0:
          print("no")
          break
  else:
          print("yes")
   
