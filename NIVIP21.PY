x11,y11=list(map(int,input().split()))
i,j=list(map(int,input().split()))
k,l=list(map(int,input().split()))
if (x11==i==k) or (y11==j==l) or (x11==y11) or (i==j) or (k==l) :
    print("yes")
else:
    print("no")
