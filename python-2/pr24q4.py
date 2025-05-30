class A:
    def ashow(self):
        print("i am grandfather from A class")
class B(A):
    def bshow(self):
        print("i am father from B class")
class C(B):
    def cshow(self):
        print("i am grandfather from A class")

c1=C();
c1.ashow()
c1.bshow()
c1.cshow()

"""

i am grandfather from A class
i am father from B class
i am grandfather from A class

"""

