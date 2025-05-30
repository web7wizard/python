d1={'a':100,'b':200,'c':300}
d2={'a':300,'b':200,'d':400}


d3={}
print(d1)
print(d2)
for i in d1:
    for k in d2:
        if(i==k):
            d3.update({i:d1[i]+d2[k]})
print(d3)

"""
{'a': 100, 'b': 200, 'c': 300}
{'a': 300, 'b': 200, 'd': 400}
{'a': 400, 'b': 400}
"""

