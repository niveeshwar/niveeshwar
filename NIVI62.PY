#N
z11=input()
flag=0
for i in z11:
    if i!='0' and i!='1':
        print("no")
        flag=1
        break
if flag==0:
    print("yes")
