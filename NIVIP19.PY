#N

A11=int(input())

B11=[]

for i in range (2,A11+1):

	if(A11%i)==0:
  
		B11.append(i)
    
		A11=A11//i
    
k1=sorted(B11)

print(*k1)
