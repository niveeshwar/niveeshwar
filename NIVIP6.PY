#N
m11,p11=map(str,input().split())
for i in range(len(m11)):
    if(m11.count(m11[i])==p11.count(p11[i])):
        print("yes")
        break
    else:
        print("no")
        break
