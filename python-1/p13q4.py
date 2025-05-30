def acc(st):
    l,u=0,0
    for k in st:
        if(k.isupper()):
            u+=1
        if(k.islower()):
            l+=1
    print("upper case letter",u)
    print("lower case letter",l)

st=(input("enter a string"))
acc(st)
