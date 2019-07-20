#N
n23,k,p=map(str,input().split())
n23=list(n23)
k=list(k)
p=int(p)
count=0
for i in range(0,len(n23)):
        if(n23[i]!=k[i]):
            count=count+1
if(count==p):
    print("yes")
else:
    print("no")
