anyat23=(input())
catat=0
for i in range(0,len(anyat23)):
    surat=(anyat23[:i]+anyat23[i+1:])
    if(int(surat) % 8==0):
        catat=1
        break
if(catat==1):
    print("yes")
else:
    print("no")
