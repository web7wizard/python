def print_animals(*animals):
    for animal in animals:
        print(animal)
print_animals("lion","elephant","wolf","gorilla")

print("------------------------------------------")

def print_food(**foods):
    for food in foods.items():
        print(food)
print_food(lion="carnivore",
           elephant="herbivore",gorilla="omnivore")


print("------------------------------------------")
from functools import reduce
def mul(x,y):
    return x*y
numbers=[1,2,3,4,5] 
result=reduce(mul,numbers)
print(result)


number=[1,2,3,4,5]
sq=list(map(lambda x:x**2,number))
print(sq)

def even(num):
    if num%2==0:
        return True
    else:
        return False
nu=[1,2,3,4,5,6,7,8,9,10]
e=list(filter(even,nu))
print(e)
"""
lion
elephant
wolf
gorilla
------------------------------------------
('lion', 'carnivore')
('elephant', 'herbivore')
('gorilla', 'omnivore')
"""
