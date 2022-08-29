from random import choice
def food(eats):
    return choice(eats)
print("we are eating:")
print(food(["pizza", "burgers", "sushi", "chinese"]))
