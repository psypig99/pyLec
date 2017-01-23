class Person():

    def __init__(self):
        print("I have Two Arms")
        print("I have tow legs")

    def swim(self):
        print("I'm trying to move my arms and legs to survive")

lucy = Person()
lucy.swim()



class Archer:

    def __init__(self, amount):
        self.energy = amount

    def get_energy(self):
        print(self.energy)


chris = Archer(10)
ellena = Archer(20)

chris.get_energy()
ellena.get_energy()
