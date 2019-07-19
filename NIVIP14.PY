#N

d11=int(input())

e11=str(input())

e11=list(e11)

for i in e11:

	if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
  
		e11.remove(i)
    
k=e11[::-1]

print("".join(k))
