from array import array
from collections import Counter
from dataclasses import dataclass


@dataclass
class Page:
    id: int
    url: str
    data: array

    @property
    def fulltext(self):
        """Make the string from array"""
        return ' '.join(self.data)

    def analyze(self):
        """Set the count of tokens on page"""
        self.term_frequencies = Counter(self.data)

    def term_frequency(self, term):
        """Get the frequency of token on page"""
        return self.term_frequencies.get(term, 0)
