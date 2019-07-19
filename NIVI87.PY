#N
pp11,mm11=map(int,input().split())
nnn=[]
tt=[]
gcd=1
for i in range(1,pp11+1):
    if(pp11%i==0):
        nnn.append(i)
for j in range(1,mm11+1):
    if(mm11%j==0):
        tt.append(j)
for y in nnn:
    if y in tt:
        gcd=gcd*y
print(gcd)
