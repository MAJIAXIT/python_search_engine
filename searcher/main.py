from searcher.load_pages import load_pages
from searcher.index import Index


def index_pages(pages, index):
    """Make indexes of all pages"""
    for i, page in enumerate(pages):
        index.index_page(page)
        if i % 1000 == 0:
            print(f'Indexed {i} pages', end='\r')
    return index


def search_on_directory(PROJECT_NAME, query, search_type):
    """Make an index search"""
    index = index_pages(load_pages(PROJECT_NAME), Index())
    answer = []

    if len(index.pages) != 0:
        answer = [f'Index contains {len(index.pages)} pages']

        for link in index.search(query, search_type=search_type):
            dict_link = link[0].__dict__
            answer.append('id: ' + str(dict_link['id']) +
                          ' url: ' + str(dict_link['url']) + ' rating: ' + str(int(link[1])))

    if len(index.pages) == 0:
        answer = [f'There are no directory with name: `' +
                  PROJECT_NAME + '` or data.txt file is uncorrect.']
    return answer
