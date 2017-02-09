from urllib.request import urlopen
from web_crawler.link_finder import LinkFinder
from web_crawler.general import *

class Spider:
    # Define Class variables (shared among all instances)
    project_name = ""
    base_url = ""
    domain_name = ""
    queue_file = ""
    crawled_file = ""
    queue = set()
    crawled = set()

    # Initialize Spider Class
    def __init__(self, project_name, base_url, domain_name):
        Spider.project_name = project_name
        Spider.base_url = base_url
        Spider.domain_name = domain_name
        Spider.queue_file = Spider.project_name+"/queue.txt"
        Spider.crawled_file = Spider.project_name+"/crawled.txt"
        self.boot()
        self.crawl_page("First Spider", Spider.base_url)

    @staticmethod
    def boot():
        create_project_dir(Spider.project_name)
        create_data_files(Spider.project_name, Spider.base_url)
        Spider.queue = file_to_set(Spider.queue_file)
        Spider.crawled = file_to_set(Spider.crawled_file)

    @staticmethod
    def crawl_page(thread_name, page_url):
        if page_url not in Spider.crawled:
            print(thread_name + " now crawling " + page_url)
            print("Queue " + str(len(Spider.queue)) + " | Crawled " + str(len(Spider.crawled)))
            Spider.add_links_to_queue(Spider.gather_links(page_url))
            Spider.queue.remove(page_url)
            Spider.crawled.add(page_url)
            Spider.update_files()

    @staticmethod
    def gather_links(page_url):
        html_string = ""
        print(page_url)
        try:

            response = urlopen(page_url)
            print(response)
            if response.getheader("Content-Type") == "text/html; charset=utf-8":
                html_bytes = response.read()
                html_string = html_bytes.decode("utf-8")
            finder = LinkFinder(Spider.base_url, page_url)
            finder.feed(html_string)
        except:
            print("Error : cannot crawl page")
            return set()
        return finder.page_links()

    @staticmethod
    def add_links_to_queue(links):
        for url in links:
            if url in Spider.queue:
                continue
            if url in Spider.crawled:
                continue

            # To avoid crawling the entire tistory.com
            if Spider.domain_name not in url:
                continue

            Spider.queue.add(url)

    @staticmethod
    def update_files():
        set_to_file(Spider.queue, Spider.queue_file)
        set_to_file(Spider.crawled, Spider.crawled_file)