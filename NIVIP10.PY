ap1,bp1=list(map(str,input().split()))
count=0
for i in range(0,len(ap1)):
    if(ap1[i]!=bp1[i]):
        count+=1
if(count==1):
    print('yes')
else:
    print('no')
