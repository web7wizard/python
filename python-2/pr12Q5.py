d={"a":1,"b":2,"c":13,"d":4,"e":50,"f":20,"g":1001}

"""m=sorted(d.values())
for i in range (1,4):
    print(m[len(m)-i])"""

    #or
m=sorted(d.values(),reverse=True)
for i in range (0,3):
    print(m[i])
