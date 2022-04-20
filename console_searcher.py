import os
from crawler.main import *
from searcher.main import *
import shutil


commands = set(['/delete', '/dirs', '/crawl', '/search'])


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
            print(os.listdir('directories'))
            main()

        if '/crawl' in answer:
            url = input('Enter the homepage url to crawl: $ ')
            get_data_from_domen(url)
            main()

        if '/delete' in answer:
            directory = input('Enter directory to remove: $ ')
            if os.path.exists('directories/' + directory):
                shutil.rmtree('directories/' + directory)
                print('Directory removed successfuly.')
            else:
                print('There are no such directory.')
            main()

        if '/search' in answer:
            directory = input('Enter directory: $ ')
            text = input('Enter text to find: $ ')
            search_type = input('Enter search type (or, and): $ ')

            answer = search_on_directory(directory, text, search_type)
            if len(answer) > 0:
                for page in answer:
                    print(page)
            else:
                print('No search results.')
            main()

    else:
        print(help_mes)
        main()


if __name__ == '__main__':
    main()
