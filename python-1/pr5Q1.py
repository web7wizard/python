n=int(input("enter a val"))
original=n
rem=0
rev=0

while(n>0):
    rem=int(n%10)
    rev=(rev*10)+rem
    n=int(n/10)
if(original==rev):
    print("pali")
else:
    print("not")
