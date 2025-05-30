class degree:
    def getdegree(self):
        print("i got a degree")
class undergraduate(degree):
    def getdegree(self):
        print("i am a undergraduate")
class post(undergraduate):
    def getdegree(self):
        print("i am postgraduate")

d=degree()
d.getdegree()
d1=undergraduate()
d1.getdegree()
d2=post()
d2.getdegree() 

'''class cal:
    def area(self,l,b):
        print(l*b)
    def area(self,s):
        print(4*s)
c=cal()
c.area(10,20)
c1=cal(2)
i got a degree
i am a undergraduate
i am postgraduate
'''