xaat123 = int(input())
taat = int(xaat123/2)
raat = []
for i in range(xaat123, taat, -1):
    j = str(i)
    if i + sum([int(kaat) for kaat in j]) == xaat123:
        print(1)
        print(i)
        break
else:
    print(0) 
