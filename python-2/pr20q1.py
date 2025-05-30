class p19:
    #x=2
    #n=3
    def  __init__(self,x,n):
        self.x=x;
        self.n=n;
p1=p19(2,3)
print(p1.x," ^ " , p1.n)
print(pow(p1.n,p1.x))
