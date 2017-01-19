class Enemy:
    life = 3

    def attack(self):
        print("아프다~~")
        self.life -= 1

    def checkLife(self):
        if self.life <= 0:
            print("I am dead")
        else:
            print(str(self.life) + " life left")

enemy_1 = Enemy()
enemy_2 = Enemy()
enemy_3 = Enemy()

enemy_1.attack()
enemy_1.attack()
enemy_1.checkLife()

