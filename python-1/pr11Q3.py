s={10,20,30,40}
s1={50,40,70,80}
a=s&s1 #s1.intersection(s2)
print("intersection=  ",a)
b=s|s1  #s1.union(s2)
print("union=  ",b)
s3=s-s1  #s1.difference(s2)
print("difference=  ",s3)
c=s^s1   # s1.symmatric_difference(s2)
print("symatric difference=  ",c)
print(s.difference(s1))
s1.clear()
print("clear set=  ",s1)

"""
intersection=   {40}
union=   {70, 40, 10, 80, 50, 20, 30}
difference=   {10, 20, 30}
symatric difference=   {70, 10, 80, 50, 20, 30}
{10, 20, 30}
clear set=   set()


"""
