class Hero:
    def __init__(self):
        self.coins = []


    def get_money(self):

        golds = 0
        for coin in self.coins:
            if coin.metal == "gold":
                golds += coin.value
            elif coin.metal == "silver":
                golds+= coin.value/100
            elif coin.metal == "bronze":
                golds+= coin.value/10000


        g = int(golds//1)
        s = int(golds%1*100)
        b = int(golds%1*100%1*100)

        to_return = []
        if g>0:
            to_return.append(f"{g} золотых")
        if s>0:
            to_return.append(f"{s} серебрянных")
        if b > 0:
            to_return.append(f"{b} бронзовых")
        return ", ".join(to_return)


class Coin:


    def __init__(self, value, metal):
        self.metal = metal
        self.value = value


hero = Hero()

coins = [Coin(5, "gold"), Coin(30, "silver"), Coin(15, "bronze"), Coin(8, "gold")]

hero.coins = coins
print(hero.get_money())