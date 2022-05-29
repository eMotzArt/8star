from random import randint



class Cube:
    def __init__(self, edges):
        self.edges = edges
        self.history = []

    def dice_throw(self):
        result = randint(1, self.edges)
        self.history.append(result)
        return result

    def get_history(self):
        return tuple(self.history)

my_cube = Cube(10)
print(my_cube.dice_throw())
print(my_cube.dice_throw())
print(my_cube.dice_throw())
print(my_cube.dice_throw())
print(my_cube.dice_throw())

print(my_cube.get_history())