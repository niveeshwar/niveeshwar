#N
stt1,sss=map(int,input().split())
ssn=0
Lii=[]
for i in range(stt1):
      Lii.append(input())
for i in range(stt1):
      for j in range(sss-1):
            if(Lii[i][j]!='R' and Lii[i][j+1]!='R'):
                  ssn+=3
            elif(Lii[i][j]!='G' and Lii[i][j+1]!='G'):
                  ssn+=5
print(ssn)
