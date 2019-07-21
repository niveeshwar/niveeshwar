i11,k=map(str,input().split())
s=0
if len(i11)>len(k):
  i11,k=k,i11
p=0
while p<len(i11):
  s+=(ord(k[p])-ord(i11[p]))
  p+=1
for p in range(p,len(k)):
  s+=ord(k[p])-ord('a')+1
print(s)
