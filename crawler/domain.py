from urllib.parse import urlparse


def get_domain_name(url):
    """Return the name of domain"""
    try:
        results = get_sub_domain_name(url).split('.')
        return results[-2] + '.' + results[-1]
    except:
        return ''


def get_project_name(url):
    """Return the name of project"""
    try:
        results = get_sub_domain_name(url).split('.')
        return results[-2]
    except:
        return ''


def get_sub_domain_name(url): 
    """Return the address of domain (netloc)"""
    try:
        return urlparse(url).netloc
    except:
        return ''
