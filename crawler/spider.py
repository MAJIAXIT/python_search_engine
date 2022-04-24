from crawler.domain import get_domain_name
from crawler.links_finder import LinksFinder
from crawler.general import *
import requests


class Spider:
    """Variables for all spiders"""
    project_name = ''
    base_url = ''
    domain_name = ''
    queue_file = ''
    crawled_file = ''
    queue = set()
    crawled = set()

    def __init__(self, project_name, base_url, domain_name):
        """First spider creates the files"""
        Spider.project_name = project_name
        Spider.base_url = base_url
        Spider.domain_name = domain_name
        Spider.queue_file = 'directories/' + Spider.project_name + '/queue.txt'
        Spider.crawled_file = 'directories/' + Spider.project_name + '/crawled.txt'
        Spider.data_file = 'directories/' + Spider.project_name + '/data.txt'
        self.boot()
        self.crawl_page('First spider', Spider.base_url)

    @staticmethod
    def boot():
        """Creates the directory and data files on first run"""
        create_directory_for_url(Spider.project_name)
        create_data_files(Spider.project_name, Spider.base_url)
        Spider.queue = file_to_set(Spider.queue_file)
        Spider.crawled = file_to_set(Spider.crawled_file)

    @staticmethod
    def crawl_page(spider_name, page_url):
        """Fills queue with formated links, update other files and write the message"""
        if page_url not in Spider.crawled:
            print(spider_name + ' now crawling ' + page_url)
            print('Queue ' + str(len(Spider.queue)) +
                  ' | Crawled ' + str(len(Spider.crawled)), end='\r')
            links = Spider.gather_links(page_url)
            if len(links) > 0:
                Spider.add_links_to_queue(links)
            Spider.queue.remove(page_url)
            Spider.crawled.add(page_url)
            Spider.update_files()

    @staticmethod
    def gather_links(page_url):
        """Gets the html and links from file and format it"""
        links = set()
        try:
            r = requests.get(url=page_url)
            content_type = r.headers.get('content-type')
            if 'html' in content_type:
                finder = LinksFinder(Spider.base_url, page_url)
                finder.feed(r.text)
                content = finder.page_links()[1]
                append_to_file(Spider.data_file, content)
                links = finder.page_links()[0]
        except Exception as e:
            print(str(e))

        return links

    @staticmethod
    def add_links_to_queue(links):
        """Add the new links to the spider queue set"""
        for link in links:
            if (link in Spider.queue) or (link in Spider.crawled):
                continue
            if Spider.domain_name != get_domain_name(link):
                continue
            Spider.queue.add(link)

    @staticmethod
    def update_files():
        """Add the spider data to queue and crawled files"""
        set_to_file(Spider.queue, Spider.queue_file)
        set_to_file(Spider.crawled, Spider.crawled_file)
