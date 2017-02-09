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