from PIL import Image
"""
주석처리된 코드의 경우에는 에러가 발생함
호출하는 부분에서 뭔가 다른 것으로 여겨짐
rawImage = Image.open("../537.jpg")

area = (20, 20, 60, 60)
cropImage = rawImage.crop(area)

print(rawImage.size)
print(cropImage.size)

paste_area = (10, 10, 40, 40)

rawImage.paste(cropImage, paste_area)
rawImage.show()
"""

steve = Image.open("../steve.jpg")
apple = Image.open("../apple.png")

print(apple.size)

paste_area = (0, 0, 259, 194)

steve.paste(apple, paste_area)
steve.show()
