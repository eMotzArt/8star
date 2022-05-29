import math



class Hero():

    def __init__(self, name):
        self.name = name
        self.experience = 0
        self.health = 100
        self.level = 1

        self.to_lvl_up = 15


    def add_experience(self, points):
        '''Добавляет опыт, расчитывает уровень, поднимает хелсы'''

        #прибавляем опыт
        self.experience += points

        new_level, self.to_lvl_up = self.check_lvl()



        if new_level>self.level:
            self.grow_health(new_level)
        self.level = new_level


        print(f"У меня {self.experience} Очков. Это {new_level} уровень. Следующая ступень {self.to_lvl_up} очков")

    def grow_health(self, new_level):
        for lvl in range(self.level, new_level):
            self.health+=self.health*0.5
            self.health=math.ceil(self.health/10)*10
            print(f"Мои хелсы стали {self.health}")


    def check_lvl(self, **kwargs):
        #берем нынешний опыт
        exp=self.experience

        #если нет аргументов (а это только при первичном вызове функции) берем из self'а данные уровня и следующего повышения
        if not kwargs:
            next = self.to_lvl_up
            lvl=self.level

        else:
            next = kwargs['next']
            lvl = kwargs['lvl']

        #если опыт больше, чем нужно для повышения
        if exp >= next:
            lvl += 1
            next *= 2
            return self.check_lvl(next=next, lvl=lvl)
        else:
            return lvl, next










my_hero = Hero('Ivan')
while True:
    points = int(input())
    my_hero.add_experience(points)


