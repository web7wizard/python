import pandas as pd
l1=[100,200,300,400,500]
ser=pd.DataFrame(l1)
print(ser)
print("--------------------------------------------")
d1={1:10,2:20,3:30}
p=pd.DataFrame(d1.items())
print(p)

"""
     0
0  100
1  200
2  300
3  400
4  500
--------------------------------------------
   0   1
0  1  10
1  2  20
2  3  30

"""