class Teller:
    def __init__(self):
        self.shots = 1
        self.has_shot = 0


    def ask(self, topic):
        if self.has_shot>0:
            return "Ты исчерпал свои попытки, странник. Уходи!"
        if topic == "дорога":
            self.has_shot += 1
            return "Отправляйся на север, держись самого края леса, найдешь пещеру, пройдешь внутри, от нее 2-3 лиги до городка"

        elif topic == "виверна":
            self.has_shot += 1
            return "Победить виверну можно только магическим оружием. Спроси в городке сотрудников гильдии магического метода"

        elif topic == "дракон":
            self.has_shot += 1
            return "За сломанной горой в скалах живет дракон. С ним вообще никогда проблем не было"





teller = Teller()
print(teller.ask("дорога"))
print(teller.ask("виверна"))
print(teller.ask("дракон"))