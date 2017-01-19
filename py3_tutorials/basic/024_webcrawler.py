import requests
from bs4 import BeautifulSoup

def spider(max_pages):
    page=1
    while page < max_pages:
        url = "http://createiveworks.tistory.com/"+str(page)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, "lxml")

    print(soup)

spider(10)