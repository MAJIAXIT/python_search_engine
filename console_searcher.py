import os
from crawler.main import *
from searcher.main import *
import shutil


commands = ('/remove', '/dirs', '/crawl', '/search')


help_mes = '\n\
/dirs - Get crawled domains\n\
/remove - Remove directory of crawled domain\n\
/crawl - Crawl domain by homepage\n\
/search - Search in crawled domain.\n'

_open = open('open.txt').read()
print(_open)
print(help_mes)


def main():
    """Command explorer"""
    answer = input('$ ')

    if answer in commands:
        if '/dirs' in answer:
            print(get_directories())
            main()

        if '/crawl' in answer:
            url = input('Enter the homepage url to crawl it: $ ')
            crawl(url)
            main()

        if '/remove' in answer:
            if len(get_directories()) > 0:
                directory = input('Enter directory to remove: $ ')
                delete_directory(directory)
            else:
                print('There are no directories to remove.')
            main()

        if '/search' in answer:
            if len(get_directories()) > 0:
                search()
            else:
                print('There are no directories to search.')
            main()

    else:
        print(help_mes)
        main()


def get_directories():
    """Return already crawled directories"""
    directories = os.listdir('directories')
    return directories


def delete_directory(directory):
    """Remove already crawled directory"""
    if os.path.exists('directories/' + directory):
        shutil.rmtree('directories/' + directory)
        print('Directory removed successfuly.')
    else:
        print('There are no such directory')
        print(f'Available directories: {get_directories()}')


def crawl(url):
    """Crawl the url"""
    get_data_from_domain(url)
    print('\n')


def search():
    """Make search on directory"""
    directory = input('Enter directory: $ ')
    if directory in get_directories():
        text = input('Enter text to find: $ ')
        search_type = input('Enter search type (or, and): $ ')
        answer = search_on_directory(directory, text, search_type)
        if len(answer) > 1:
            for page in answer:
                print(page)
        else:
            print('\nNo search results.')
    else:
        print('There are no such directory')
        print(f'Available directories: {get_directories()}')
        search()


if __name__ == '__main__':
    if os.path.exists('directories'):
        pass
    else:
        os.makedirs('directories')
        print('Folder `directories` created.')
    main()
