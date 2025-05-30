from functools import reduce
def multiply(x,y):
    return x*y

numbers=[1,2,3,4,5]
result=reduce(multiply,numbers)
print(result)



numbers=[1,2,3,4,5]
squared=list(map(lambda x:x**2,numbers))
print(squared)


def even_check(num):
    if num % 2==0:
        return True
    else:
        return False
numbers=[1,2,3,4,5,6,7,8,9,10]
even_numbers=filter(even_check,numbers)
print(list(even_numbers))

"""
output

120
[1, 4, 9, 16, 25]
[2, 4, 6, 8, 10]
"""
