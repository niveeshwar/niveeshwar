a23=int(input())
li=list(map(str,input().split()[:a23]))
li.sort()
li.sort(key=len)
for i in li:
        print(i,end=" ")
