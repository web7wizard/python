l1=[10,20,40,"jiya",'j',60]
l2=[10,70,'j',2,60]
common=list(set (l1) & set(l2))
print("common data =  ",common)


#or

commo=[x for x in l1 if x in l2]
print("common data=  ",commo)


"""
common data =   ['j', 10, 60]
common data=   [10, 'j', 60]
"""
