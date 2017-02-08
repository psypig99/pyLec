from html.parser import HTMLParser
from urllib import parse

class LinkFinder(HTMLParser):
    def __init__(self, base_url, page_url):
        super().__init__()
        self.base_url = base_url
        self.page_url = page_url
        self.links = set()

    def handle_starttag(self, tag, attrs):
        if tag == "a":
            for(attribute, value) in attrs:
                if attribute == "href":
                    url = parse.urljoin()

    def handle_endtag(self, tag):
        print(tag)

    def error(self, message):
        pass

finder = LinkFinder()
finder.feed("<html><head><title> TITLE TEST </title></head>"
            "<body><h1> Parse Test</h1><a href='www.naver.com'/></body></html>")