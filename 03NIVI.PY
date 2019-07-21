s11,b=input().split()
d=abs(len(s11)-len(b))
for j in range(len(s11)):
    if len(b)==1 and s11[j] in s11:
        break
    if s11[j]!=b[j]:
        d+=1
print(d)
