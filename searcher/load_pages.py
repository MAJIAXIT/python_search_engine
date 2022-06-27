from searcher.pages import Page


def load_pages(PROJECT_NAME):
    """Yield page objects from data.txt file"""
    try:
        with open('directories/' + PROJECT_NAME + '/data.txt', 'r') as file:
            page_id = 0
            for line in file:
                dictionary = eval(line)
                yield Page(id=page_id, url=dictionary['url'], data=dictionary['data'])
                page_id += 1
    except:
        pass
