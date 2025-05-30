def myfunc(text ,num):
    while num>0:
        print(text)
        num=num-1
myfunc('hello',4)

print("-----------------------------------")

num=1
def func():
    num=3
    print(num)
func()
print(num)

"""
hello
hello
hello
hello
-----------------------------------
3
1
"""
print("-----------------------------------")
def prime(n):
    i=1
    flag=0
    for i in range(2,n):
        if(n%i==0):
            flag=1
            print("not prime")
            break
    if(flag==0):
        print("prime")
prime(9)

print("-----------------------------------")

def fact(num):
    fact=1
    i=1
    while(i<=num):
        fact=fact*i
        i=i+1
    print("factorial=  ",fact)
fact(5)

