#N
i1=input()
b1=str(input())
p=('a','e','i','o','u')
for i1 in b1:
    if i1 in p:
        b1=b1.replace(i,"")
print(b1[::-1])
