class sup():
    def __init__(self):
        print("i am constructor")
    def __del__(self):
        print("i am destructor")


s1=sup()
del s1

