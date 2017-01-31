from PIL import Image

baby = Image.open("../baby.jpg")
print(baby.size)
baby.show()

square_baby = baby.resize((500,500))
square_baby.show()

flip_baby = baby.transpose(Image.FLIP_LEFT_RIGHT)
flip_baby.show()

spin_baby = baby.transpose(Image.ROTATE_90)
spin_baby.show()