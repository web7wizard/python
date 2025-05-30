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
