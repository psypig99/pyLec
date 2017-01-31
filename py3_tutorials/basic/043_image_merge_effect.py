from PIL import Image

cat = Image.open("../cat.jpg")
print(cat.mode)

r,g,b = cat.split()

new_img = Image.merge("RGB", (r,g,b))
new_img.show()
transform_img = Image.merge("RGB", (g,r,b))
transform_img.show()