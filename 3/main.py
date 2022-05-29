import math
class Dragon:

    def __init__(self, color, hp):
        self.color = color
        self.hp = hp
        self.is_alive = True

    def get_health(self):
        return f"У меня есть {self.hp} HP"

    def closest_degree(self):
        current_degree = 1
        while True:
            result = 2**current_degree
            if result> self.hp:
                return result
            current_degree+=1


    def get_damage(self, value):

        #простое решение
        log = math.log(value, 2)
        #сложное

        if log % 1 == 0:
            self.hp = self.closest_degree()
            print(f"Я исцелился до {self.hp}")
            return
        #если дробная часть == 0



        #магия
        if self.hp - value > 0:
            self.hp -= value
        else:
            self.hp = 0
            self.die()
        print(f"Мои хелсы равны {self.hp}")


    def bite(self):
        if not self.is_alive:
            print("Не могу делать кусь, я ведь умир")
            return
        self.hp+=10
        print("Кусь на 10")

    def die(self):
        self.is_alive = False
        print("Я умир, и не могу делать кусь")

dragon = Dragon("black", 500)
dragon.get_damage(1)
dragon.get_damage(4)
