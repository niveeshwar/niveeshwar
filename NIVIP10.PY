#N
k11,n21=list(map(str,input().split()))
count=0
for i in range(0,len(k11)):
    if(k11[i]!=n12[i]):
        count+=1
if(count==1):
    print('yes')
else:
    print('no')
