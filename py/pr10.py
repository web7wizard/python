d1={1:'jiya',2:'jk'}
print(d1)
print("add new employee")
d1.update({3:"jj"})
print(d1)
del d1[2]
print(d1)

flag=0
print("lets search for an emp give id and name")
idn=int(input("enter id=  "))
name=input("enter name=  ")
if name in d1.values():
    print("found")
    flag=1

if(flag==0):
    print("not found lets add")
    d1.update({idn:name})
print(d1)    
