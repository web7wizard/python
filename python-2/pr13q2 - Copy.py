def primef(n):
    flag=0
    for i in range(2,n):
        if(n%i==0):
            print("not a prime")
            flag=1
            break
    if(flag==0):
        print("prime")

n=int(input("enter a number"))
primef(n)
