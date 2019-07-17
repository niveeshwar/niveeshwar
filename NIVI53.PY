#N
NI=0
Num = int(input(""))
PA= 0
while(Num > 0):
    NI= Num % 10
    PA = PA+NI
    Num = Num //10
print(PA)
