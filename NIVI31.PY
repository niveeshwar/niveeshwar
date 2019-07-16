#a
a1=list(input())
b1=" "
for i in range(len(a1)):
    if b1 in a1:
        a1.remove(b1)
print(len(a1))
