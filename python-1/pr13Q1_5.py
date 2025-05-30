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
