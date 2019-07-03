month=int(input())
if month%4==0 and month%100==0 or month%400==0:
    print("yes")
else:
    print("no")
