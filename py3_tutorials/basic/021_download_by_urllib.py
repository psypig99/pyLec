import random
import urllib.request

def download_web_imgaes(url):
    name = random.randrange(1, 1001)
    full_name = str(name) + ".jpg"
    urllib.request.urlretrieve(url, full_name)

download_web_imgaes("이미지 url 주소가 들어감")