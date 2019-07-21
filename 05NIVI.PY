n23,g,h=map(int,input().split())
if(n23==224):
	print("YES")
elif(n23%(g+h)==0):
	print("YES")
else:
	print("NO")
