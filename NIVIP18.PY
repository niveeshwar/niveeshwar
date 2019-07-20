#N
l=int(input())

b12=sorted("kabali")

c=0

for i in range(l):

    s=input("")
    
    a=sorted(s)
    
    if(b12==a):
    
        c=c+1
        
print(c)
