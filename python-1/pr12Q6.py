dic1={'google':1,'facebook':2,'microsoft':3}
dic2={'gfg':1,'microsoft':2,'youtube':3}
dic1.update(dic2)
for key , values in dic1.items():
    print(key,values)

"""
google 1
facebook 2
microsoft 2
gfg 1
youtube 3
"""
