import os
import xml.etree.ElementTree as et


def create_directory_for_url(directory):
    """Making directory with the contents of site"""
    if not os.path.exists('directories/' + directory):
        print('Creating directory ' + directory)
        os.makedirs('directories/' + directory)


def create_data_files(project_name, base_url):
    """Making the files with queue and file with crawled urls"""
    queue = 'directories/' + project_name + '/queue.txt'
    crawled = 'directories/' + project_name + '/crawled.txt'
    data = 'directories/' + project_name + '/data.txt'
    if not os.path.isfile(queue):
        create_file(queue, base_url)
    if not os.path.isfile(crawled):
        create_file(crawled, '')
    if not os.path.isfile(data):
        create_file(data, '')


def create_file(file_path, data):
    """Create new data file"""
    with open(file_path, 'w') as file:
        file.write(data)


def append_to_file(file_path, data):
    """Append the data to the end of file"""
    with open(file_path, 'a') as file:
        file.write(str(data) + '\n')


def file_to_set(file_path):
    """Makes the set from strings in file"""
    results = set()
    with open(file_path, 'rt') as file:
        for line in file:
            results.add(line.replace('\n', ''))
        return results


def set_to_file(links, file_path):
    """Append the content of set to file"""
    with open(file_path, "w") as file:
        for link in sorted(links):
            file.write(link + "\n")
