n=int(input("enter number= "))
sumn=0
rem=0

while(n>0):
    rem=int(n%10)
    sumn=sumn+rem
    n=int(n/10)
print(sumn)
