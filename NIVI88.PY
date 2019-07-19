#N
    
k11,l=map(int,input().split())
t=[]
m=[]
lcm=1
r=max(k11,l)
for i in range(1,r):
    if(k11%i==0 and l%i==0):
        t.append(i)
        k11=k11//i
        l=l//i
m.append(k11)
m.append(l)
for u in t:
    lcm=lcm*u
for r in m:
    lcm=lcm*r
print(lcm)
