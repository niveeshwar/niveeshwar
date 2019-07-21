size23=int(input())
arr=input().rstrip()
arr=list(map(int,arr.split(" ")))
final=[1]*size23
for i in range(1,size23-1):
	if arr[i]>arr[i-1]:
		final[i]=final[i-1]+1
if arr[0]>arr[1]:
	final[0]=final[1]+1
if arr[size23-1]>arr[size23-2]:
	final[size23-1]=final[size23-2]+1
print(sum(final))
