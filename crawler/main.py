import threading
from queue import Queue
from crawler.spider import Spider
from crawler.domain import *
from crawler.general import *
import requests


NUMBER_OF_THREADS = 8
queue = Queue()


def create_workers():
    """Create threads"""
    for _ in range(NUMBER_OF_THREADS):
        t = threading.Thread(target=work)
        t.daemon = True
        t.start()


def work():
    """Make threads work like a Spider class"""
    while True:
        url = queue.get()
        Spider.crawl_page(threading.current_thread().name, url)
        queue.task_done()


def create_jobs(QUEUE_FILE):
    """Make more jobs for threads from links in queue"""
    for link in file_to_set(QUEUE_FILE):
        queue.put(link)
    queue.join()
    crawl(QUEUE_FILE)


def crawl(QUEUE_FILE):
    """Check the items in queue and make jobs for threads"""
    queued_links = file_to_set(QUEUE_FILE)
    if len(queued_links) > 0:
        print(str(len(queued_links)) + ' links in the queue')
        create_jobs(QUEUE_FILE)


def get_data_from_domain(HOMEPAGE):
    """Run the crawler"""
    DOMAIN_NAME = get_domain_name(HOMEPAGE)
    PROJECT_NAME = get_project_name(HOMEPAGE)
    QUEUE_FILE = 'directories/' + PROJECT_NAME + '/queue.txt'
    CRAWLED_FILE = 'directories/' + PROJECT_NAME + '/crawled.txt'

    try:
        r = requests.get(HOMEPAGE)

    except Exception as e:
        print(str(e))
        return str(e)

    Spider(PROJECT_NAME, HOMEPAGE, DOMAIN_NAME)
    create_workers()
    crawl(QUEUE_FILE)
