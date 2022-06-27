import re
import string
import nltk

PUNCTUATION = re.compile('[%s]' % re.escape(string.punctuation))
STOPWORDS = set(['the', 'be', 'to', 'of', 'and', 'a', 'in', 'that', 'have',
                 'i', 'it', 'for', 'not', 'on', 'with', 'he', 'as', 'you',
                 'do', 'at', 'this', 'but', 'his', 'by', 'from', 'к', 'на',
                 'с', 'от', 'в', 'над', 'под', 'по', 'до', 'из', 'без', 'у',
                 'в', 'для', 'о', 'около', 'об', 'за', 'а'])

RUSTEM = nltk.stem.SnowballStemmer('russian')
ENSTEM = nltk.stem.SnowballStemmer('english')


def tokenize(text):
    """Parse a string into a list of words"""
    return text.split()


def stopword_filter(tokens):
    """Remove words from STOPWORDS"""
    return [token for token in tokens if token not in STOPWORDS]


def lowercase_filter(tokens):
    """Rewrite the words in lowercase"""
    return [token.lower() for token in tokens]


def punctuation_filter(tokens):
    """Remove all punctuation"""
    return [PUNCTUATION.sub('', token) for token in tokens]


def stem_filter(tokens):
    """Get stems from Russian and English words"""
    tokens = [RUSTEM.stem(token) for token in tokens]
    tokens = [ENSTEM.stem(token) for token in tokens]
    return tokens


def analyze(text):
    """Filter text"""
    tokens = tokenize(text)
    tokens = lowercase_filter(tokens)
    tokens = punctuation_filter(tokens)
    tokens = stopword_filter(tokens)
    tokens = stem_filter(tokens)

    return [token for token in tokens if token]
