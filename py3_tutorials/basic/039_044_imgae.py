"""
필로우(Pillow)
용도 : 간단한 이미지 처리
장점 : 필로우는 PIL보다 더 사용하기 쉬우면서도, 최소한의 변경만으로 PIL과의 코드 호환성 확보에 목표를 두고 있다
"""

from PIL import Image

"""
040_Crop_Image
img = Image.open("../537.jpg")
print(img.size)
print(img.format)
area = (20, 20, 200, 170)
cropped_img = img.crop(area)

img.show()
cropped_img.show()
"""

"""
041_Combine_images

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
"""
steve = Image.open("../steve.jpg")
apple = Image.open("../apple.png")

print(apple.size)

paste_area = (0, 0, 259, 194)

steve.paste(apple, paste_area)
steve.show()
"""

