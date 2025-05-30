class std:
    __a=10
    b=20
    def __f1(self):
        print("in private")
    def f2(self):
        s1.__f1()
        print(s1.__a)
        print("in public")

s1=std()
print(s1.a)
print(s1.b)
s1.__f1()
s1.f2()

"""
20
in private
10
in public

"""