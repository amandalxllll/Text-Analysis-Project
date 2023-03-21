import random
import string
import sys
from unicodedata import category

def process_file(filename, skip_header=False):
    """
    This process is adapted from session15
    Regenerate book that contains the words from a file.
    filename: string
    skip_header: boolean, whether to skip the Gutenberg header
    returns: map from each word to the number of times it appears.
    """
    book = {}
    fp = open(filename, encoding="UTF8")

    if skip_header:
        skip_gutenberg_header(fp)

    # strippables = string.punctuation + string.whitespace
    # via: https://stackoverflow.com/questions/60983836/complete-set-of-punctuation-marks-for-python-not-just-ascii

    strippables = "".join(
        [chr(i) for i in range(sys.maxunicode) if category(chr(i)).startswith("P")]
    )

    for line in fp:
        if line.startswith("*** END OF THIS PROJECT"):
            break

        line = line.replace("-", " ")
        line = line.replace(
            chr(8212), " "
        )  # Unicode 8212 is the HTML decimal entity for em dash

        for word in line.split():
            # word could be 'Sussex.'
            word = word.strip(strippables)
            word = word.lower()

            # update the dictionary
            book[word] = book.get(word, 0) + 1

    return book


def skip_gutenberg_header(fp):
    """Reads from fp until it finds the line that ends the header.
    fp: open file object
    """
    for line in fp:
        if line.startswith("*** START OF THIS PROJECT"):
            break


# Part2 : Analyzing the Text


def total_words(book):
    """Returns the total of the frequencies in a histogram."""
    return sum(book.values())

def most_common(book, excluding_stopwords=False):
    """Makes a list of word-freq pairs in descending order of frequency.
    hist: map from word to frequency
    returns: list of (frequency, word) pairs
    """
    t = []

    stopwords = process_file('stopwords.txt', False)

    stopwords = list(stopwords.keys())
    # print(stopwords)

    for word, freq in book.items():
        if excluding_stopwords:
            if word in stopwords:
                continue

        t.append((freq, word))

    t.sort(reverse=True)
    return t
    """res = []
    for word in book:
        if excluding_stopwords:
            if word in stopwords:
                continue
        freq = book[word]

        res.append((freq, word))

    res.sort(reverse=True)

    return res
    """
def top_10_words(book):
    """
    This sort the dictionary in desceding order and return the top 10 most appeared words in the book.
    """
    t = most_common(book,excluding_stopwords=True)
    result = {}
    for freq, word in t[:10]:
        result[word] = freq
    return result
def top_overlappingwords(book_1, book_2):
    b1 = top_10_words(book_1)
    b2 = top_10_words(book_2)
    lt = []
    for key in b1:
        if key in b2.keys():
            lt.append(key)
    for key in b2:
        if key in b1.keys():
            lt.append(key)
    list_overlapping = []
    for i in lt:
        if i not in list_overlapping:
            list_overlapping.append(i)
    return list_overlapping


def top_nonoverlappingwords(book_1, book_2):
    """
    Returns a dictionary with all keys that appear in book1 but not book2.
    d1, d2: dictionaries
    """
    b1 = top_10_words(book_1)
    b2 = top_10_words(book_2)
    lt = []
    for key in b1:
        if key not in b2.keys():
            lt.append(key)
    for key in b2:
        if key not in b1.keys():
            lt.append(key)
    list_nonoverlapping = []
    for i in lt:
        if i not in list_nonoverlapping:
            list_nonoverlapping.append(i)
    return list_nonoverlapping

def main():
    je = process_file('janeeyre.txt', skip_header=False)
    lw = process_file('littlewomen.txt', skip_header=False)
    print(f'The top 10 words in Jane Eyre are {top_10_words(je)}')
    print(f'The overlapping words in the top 10 common words in two books are:{top_nonoverlappingwords(je, lw)}')
    print(f'The overlapping words in the top 10 common words in two books are:{top_overlappingwords(je, lw)}')
if __name__ == '__main__':
    main()