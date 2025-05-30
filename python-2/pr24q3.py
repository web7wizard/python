class area:
    def cal(self,l,b):
       return(self.l*self.b)

class peri:
    def show(self,l,b):
        return(2*self.l+2*self.b)

class rect(area,peri):
    def display(self):
        self.l = int(input("enter a the len=  "))
        self.b = int(input("enter the bre  =  "))
        print(self.cal(self.l,self.b))
        print(self.show(self.l,self.b))

r=rect()
r.display()

"""
enter a the len=  2
enter the bre  =  3
6
10

"""