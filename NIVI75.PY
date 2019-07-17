z11=input()
n2=len(z11)
if n2%2!=0:
    z11=z11[:int(n2/2)]+'*'+z11[int(n2/2)+1:n2]
else:
    z11=z11[:int(n2/2)-1]+'**'+z11[int(n2/2)+1:n2]
print(z11)
