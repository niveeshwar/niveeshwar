#N
v11=input()
l1=len(v11)
z=[]
for x in range(0,l1,2):
    z.append(v11[x:x+2][::-1])
print(''.join(z))
