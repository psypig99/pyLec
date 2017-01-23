import requests
from bs4 import BeautifulSoup
import operator

def start(url):
    word_list = []
    source_code = requests.get(url).text
    soup = BeautifulSoup(source_code, "lxml")
    p_tag = soup.findAll("p", {"class":"tt-post-title"})

    for title_text in p_tag:
        content = title_text.text
        words = content.lower().split()
        for each_word in words:
            print(each_word)
            word_list.append(each_word)

start("http://creativeworkds.tistory.com")