#N
array_size=input()

array=list(map(int,input().split()))

s12=1

for i in array:

    if array.count(i)==s12:
    
        print(i)
        
        break;
        
    else:
    
        continue;
