import requests
from bs4 import BeautifulSoup
import operator

def start(url):
    word_list = []
    source_code = requests.get(url).text
    soup = BeautifulSoup(source_code, "lxml")
    p_tag = soup.findAll('p', {'class':'tt-post-title'})
    print(soup)
    for title_text in p_tag:
        content = title_text.text
        words = content.lower().split()
        print(words)
        for each_word in words:
            print(each_word)
            word_list.append(each_word)

    clean_up_list(word_list)

def clean_up_list(word_list):
    clean_word_list = []
    for word in word_list:
        symbols = "`~!@#$%^&*()-=_+[]\{}|;',./:\"<>?"
        for i in range(1, len(symbols)):
            word = word.replace(symbols[i], "")
        if len(word) > 0:
            # print(word)
            clean_word_list.append(word)

    create_dictionary(clean_word_list)

def create_dictionary(clean_word_list):
    word_count = {}
    for word in clean_word_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1


start("http://creativeworkds.tistory.com")