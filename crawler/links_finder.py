from html.parser import HTMLParser
from urllib import parse
from crawler.analyze import analyze


class LinksFinder(HTMLParser):
    """Extract links and text from a webpage"""

    def __init__(self, base_url, page_url):
        super().__init__()
        self.base_url = base_url
        self.page_url = page_url
        self.links = set()
        self.data = ''
        self.datatags = False

    def handle_starttag(self, tag, attrs):
        """Extract links"""
        if tag == 'a':
            for (attribute, value) in attrs:
                if attribute == 'href':
                    url = parse.urljoin(self.base_url, value)
                    self.links.add(url)
        if tag != 'script' and tag != 'style' and tag != 'head':
            self.datatags = True
        else:
            self.datatags = False

    def handle_data(self, data):
        """Extract text"""
        if self.datatags == True:
            self.data += data

    def page_links(self):
        """Return found links and text"""
        content = {
            "url": self.page_url,
            "data": analyze(self.data)
        }
        return self.links, content

    def error(self, message):
        pass
