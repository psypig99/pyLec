from PIL import Image

new_york = Image.open("../new_york.png")
print(new_york.mode)

r,g,b,a = new_york.split()

new_york.show()
r.show()
g.show()
b.show()
a.show()