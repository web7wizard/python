def myfun1(*argv):
    for arg in argv:
        print(arg)


        
def myfun2(**args):
    for key,value  in args.items():
        print("%s==%s"%(key,value))


print("result of *argv: ")
myfun1('hello','welcome','to','GEEKSFORGEEKS')
print("result of **args: ")
myfun2(first='greek',mid='for',last='greek')
