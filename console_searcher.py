import os
from crawler.main import *
from searcher.main import *
import shutil


commands = {'/delete', '/dirs', '/crawl', '/search'}


help_mes = '\n\
/dirs - Get crawled domens\n\
/delete - Delete directory of crowled domen\n\
/crawl - Crawl the domen by homepage\n\
/search - Search on crawled domen.\n'

open = open('open.txt', 'r').read()
print(open)
print(help_mes)


def main():
    answer = input('$ ')

    if answer in commands:
        if '/dirs' in answer:
            print(get_directories())
            main()

        if '/crawl' in answer:
            url = input('Enter the homepage url to crawl: $ ')
            crawl(url)
            main()

        if '/delete' in answer:
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
    directories = os.listdir('directories')
    return directories


def delete_directory(directory):
    if os.path.exists('directories/' + directory):
        shutil.rmtree('directories/' + directory)
        print('Directory removed successfuly.')
    else:
        print('There are no such directory')
        print(f'Available directories: {get_directories()}')


def crawl(url):
    get_data_from_domen(url)
    print('\n')


def search():
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
        print('`directories` folder created.')
    main()
