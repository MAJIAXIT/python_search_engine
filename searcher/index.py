import math
from searcher.analyze import analyze


class Index:
    def __init__(self):
        self.index = {}
        self.pages = {}

    def index_page(self, page):
        """Makes the indexes of the page"""
        if page.id not in self.pages:
            self.pages[page.id] = page
            page.analyze()

        for token in page.data:
            if token not in self.index:
                self.index[token] = set()
            self.index[token].add(page.id)

    def page_frequency(self, token):
        """Get the count of the tokens on page"""
        return len(self.index.get(token, set()))

    def inverse_page_frequency(self, token):
        """Get the ratio of pages in index to pages with token"""
        if self.page_frequency(token) != 0:
            return math.log10(len(self.pages) / self.page_frequency(token))
        if self.page_frequency(token) == 0:
            return 1

    def _results(self, analyzed_query):
        """Get the list of pages with tokens from query"""
        return [self.index.get(token, set()) for token in analyzed_query]

    def search(self, query, search_type='and', rank=True):
        """Search the matches of tokens in query and indexes"""
        if search_type not in ('and', 'or'):
            search_type = 'and'

        analyzed_query = analyze(query)
        results = self._results(analyzed_query)
        if search_type == 'and':
            pages = [self.pages[page_id]
                     for page_id in set.intersection(*results)]
        if search_type == 'or':
            pages = [self.pages[page_id]
                     for page_id in set.union(*results)]

        if rank:
            return self.rank(analyzed_query, pages)
        return pages

    def rank(self, analyzed_query, pages):
        """Rank the pages"""
        results = []
        if not pages:
            return results
        for page in pages:
            score = 0.0
            for token in analyzed_query:
                tf = page.term_frequency(token)
                idf = self.inverse_page_frequency(token)
                score += tf * idf
            results.append((page, score))
        return sorted(results, key=lambda page: page[1], reverse=True)
