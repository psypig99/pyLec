class Archer():
    def move(self):
        print("I am moving")

class Item():
    def eat_item(self):
        print("Now I am leveling up")

class LevelupArcher(Archer, Item):
    pass


lvarc = LevelupArcher()
lvarc.move()
lvarc.eat_item()